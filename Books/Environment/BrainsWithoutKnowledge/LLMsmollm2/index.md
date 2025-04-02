# LLM with Smollm

/ currently still does not work but it's closer to idea /

Smollm is especially developed for fine-tuning.

LLM-Smollm: LLM using that functionality.

- [llm-smollm2](https://github.com/simonw/llm-smollm2)

Fine-Tuning Process:
- llm supports plugins for local models, and some plugins (like llm-smollm2) allow fine-tuning directly.

## What worked

```bash
pip install llm
llm install llm-smollm2
```

> This aligns with my idea that model, once installed in standard way, should be able to download it's files. I'm disturbed that it again needs perceptrons and the package conflict: I don't like to resolve those, because they have a common reason.

## CoPilot

Steps:

1. Install the plugin:

        pip install llm-smollm2
        Prepare your dataset in a supported format (e.g., JSONL).

2. Use the CLI to fine-tune:

        llm fine-tune --model SmolLM2 --dataset path/to/dataset.jsonl

3. Save the fine-tuned model for deployment:

        llm save --model SmolLM2 --output path/to/output