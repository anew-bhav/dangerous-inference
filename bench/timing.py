"""Latency metrics for generation: TTFT, TPOT, throughput, peak memory.

TTFT  = time to first token (≈ prefill + one sampling step)
TPOT  = time per output token after the first (≈ decode step)
"""

import time
from dataclasses import asdict, dataclass

import torch
from transformers.generation.streamers import BaseStreamer


@dataclass
class GenResult:
    prompt_tokens: int
    new_tokens: int
    batch_size: int
    ttft_ms: float
    tpot_ms: float
    total_ms: float
    tokens_per_s: float  # all new tokens across the batch / total time
    peak_mem_gb: float

    def to_dict(self) -> dict:
        return asdict(self)


class _TokenClock(BaseStreamer):
    """Timestamps each decode step. generate() calls put() once with the prompt,
    then once per new token (after .cpu(), which forces a GPU sync)."""

    def __init__(self):
        self.times: list[float] = []
        self._seen_prompt = False

    def put(self, value):
        if not self._seen_prompt:
            self._seen_prompt = True
            return
        self.times.append(time.perf_counter())

    def end(self):
        pass


@torch.inference_mode()
def time_generate(model, input_ids: torch.Tensor, max_new_tokens: int, **gen_kwargs) -> GenResult:
    """Time one HF generate() call. input_ids: [batch, seq] on the model's device.

    Streamers only support batch size 1 in HF, so for batch > 1 we fall back to
    total time only (ttft/tpot = nan).
    """
    batch, prompt_len = input_ids.shape
    if torch.cuda.is_available():
        torch.cuda.synchronize()
        torch.cuda.reset_peak_memory_stats()

    clock = _TokenClock() if batch == 1 else None
    start = time.perf_counter()
    out = model.generate(
        input_ids,
        attention_mask=torch.ones_like(input_ids),
        max_new_tokens=max_new_tokens,
        min_new_tokens=max_new_tokens,
        do_sample=False,
        streamer=clock,
        **gen_kwargs,
    )
    if torch.cuda.is_available():
        torch.cuda.synchronize()
    end = time.perf_counter()

    new_tokens = out.shape[1] - prompt_len
    total = end - start
    if clock and clock.times:
        ttft = clock.times[0] - start
        tpot = (clock.times[-1] - clock.times[0]) / max(len(clock.times) - 1, 1)
    else:
        ttft = tpot = float("nan")

    peak = torch.cuda.max_memory_allocated() / 1e9 if torch.cuda.is_available() else 0.0
    return GenResult(
        prompt_tokens=prompt_len,
        new_tokens=new_tokens,
        batch_size=batch,
        ttft_ms=ttft * 1e3,
        tpot_ms=tpot * 1e3,
        total_ms=total * 1e3,
        tokens_per_s=batch * new_tokens / total,
        peak_mem_gb=round(peak, 3),
    )


def warmup(model, input_ids: torch.Tensor, n: int = 2) -> None:
    """Run a few short generations so CUDA kernels/allocator are warm before timing."""
    for _ in range(n):
        time_generate(model, input_ids, max_new_tokens=8)
