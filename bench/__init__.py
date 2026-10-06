"""Shared benchmark harness. Every lesson measures through here so numbers are comparable."""

from bench.env import collect_env
from bench.results import save
from bench.timing import GenResult, time_generate

__all__ = ["collect_env", "save", "GenResult", "time_generate"]
