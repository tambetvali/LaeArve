# Complete tool

Complete tool for fine-tuning of models.

- [Axolotl](https://axolotl.ai/)
- On Ubuntu, install with nix (`install nix-bin`):
  - `sudo nix profile install nixpkgs#llama-cpp --extra-experimental-features nix-command --extra-experimental-features flakes`

The Llama.cpp package would convert the result into gguf format.

## AI

Yes, there are open alternatives to Torchtune that you can use without waiting for gated access. Here are a couple of options:

__Axolotl__:
- __Axolotl__ is a user-friendly framework for fine-tuning large language models (LLMs). It simplifies the process by wrapping lower-level libraries like Hugging Face Transformers, allowing you to focus on your data rather than technical configurations.
- It supports open models like LLaMA 3, Pythia, and Falcon, which are readily available on Hugging Face