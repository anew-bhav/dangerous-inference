# Roadmap

> Owned by the teacher. This is a draft arc. Order and contents will change as I learn.

## Phase 1: Foundations (days ~1–15)
- [ ] Baseline: HF `generate`, measure TTFT / TPOT / tokens/s
- [ ] Prefill vs decode: why they behave differently
- [ ] Memory-bound vs compute-bound, roofline model
- [ ] Anatomy of a forward pass: where time and memory go

## Phase 2: Core optimizations, by hand (days ~16–35)
- [ ] KV cache from scratch
- [ ] Static batching
- [ ] Continuous batching
- [ ] Sampling strategies and their cost

## Phase 3: Memory & kernels (days ~36–55)
- [ ] Paged attention
- [ ] FlashAttention
- [ ] Quantization: int8 / int4, AWQ / GPTQ
- [ ] First Triton kernel

## Phase 4: Real engines (days ~56–75)
- [ ] vLLM internals and benchmarks
- [ ] SGLang
- [ ] Speculative decoding
- [ ] Prefix caching

## Phase 5: Scale & capstone (days ~76–100)
- [ ] Tensor parallelism / multi-GPU
- [ ] Disaggregated prefill/decode
- [ ] **Capstone:** my own mini inference engine, benchmarked against vLLM
- [ ] Final write-up
