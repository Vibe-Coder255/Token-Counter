from __future__ import annotations

from typing import Iterable

try:
    import tiktoken
except ImportError:  # pragma: no cover - dependency error is handled clearly.
    tiktoken = None


def _get_encoding(model_name: str):
    if tiktoken is None:
        raise RuntimeError(
            "tiktoken is required. Install it with: pip install tiktoken"
        )

    try:
        return tiktoken.encoding_for_model(model_name)
    except KeyError:
        return tiktoken.get_encoding("cl100k_base")


class TokenCounter:
    """Count tokens for OpenAI-style GPT models using the matching tokenizer."""

    def __init__(self, model_name: str = "gpt-4o-mini") -> None:
        self.model_name = model_name
        self.encoding = _get_encoding(model_name)

    def count(self, text: str) -> int:
        if text is None or text == "":
            return 0
        return len(self.encoding.encode(text))

    def count_stream(self, chunks: Iterable[str]) -> int:
        total = 0
        for chunk in chunks:
            total += self.count(chunk)
        return total


def count_tokens(text: str, model_name: str = "gpt-4o-mini") -> int:
    return TokenCounter(model_name=model_name).count(text)
