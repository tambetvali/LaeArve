# LLM with Smollm

Smollm is especially developed for fine-tuning.

LLM-Smollm: LLM using that functionality.

- [llm-smollm2](https://github.com/simonw/llm-smollm2)

Fine-Tuning Process:
- llm supports plugins for local models, and some plugins (like llm-smollm2) allow fine-tuning directly.

Steps:

1. Install the plugin:

        pip install llm-smollm2
        Prepare your dataset in a supported format (e.g., JSONL).

2. Use the CLI to fine-tune:

        llm fine-tune --model SmolLM2 --dataset path/to/dataset.jsonl

3. Save the fine-tuned model for deployment:

        llm save --model SmolLM2 --output path/to/output