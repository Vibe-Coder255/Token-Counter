# Token Counter

A small Python utility for counting tokens in text using a real LLM tokenizer.

## Install

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py "Hello world, this is a test."
python main.py --file sample.txt --model gpt-4o-mini
```

The project uses `tiktoken`, which matches the tokenizer used by GPT-style models and gives a realistic token count for generated output.
