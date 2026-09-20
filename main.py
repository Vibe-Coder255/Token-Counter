from __future__ import annotations

import argparse
import sys

from Services.token_counter import TokenCounter


def read_text(args: argparse.Namespace) -> str:
    if args.file:
        with open(args.file, "r", encoding="utf-8") as file:
            return file.read()

    if args.text is not None:
        return args.text

    if not sys.stdin.isatty():
        return sys.stdin.read()

    return input("Enter the text to count: ")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Count tokens in text using a model-specific tokenizer."
    )
    parser.add_argument("text", nargs="?", help="Text to count.")
    parser.add_argument(
        "--file",
        help="Read the text to count from a file instead of the command line.",
    )
    parser.add_argument(
        "--model",
        default="gpt-4o-mini",
        help="Model name used to select the tokenizer (default: gpt-4o-mini).",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    try:
        text = read_text(args)
        token_counter = TokenCounter(model_name=args.model)
        count = token_counter.count(text)
        print(f"Token count for model '{args.model}': {count}")
    except FileNotFoundError:
        print(f"File not found: {args.file}")
        raise SystemExit(1)
    except RuntimeError as exc:
        print(str(exc))
        raise SystemExit(1)


if __name__ == "__main__":
    main()
