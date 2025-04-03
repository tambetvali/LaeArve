# TorchTune

Currently, I found this:
- With "pip install torchtune torchao", install Torch Tune (before you might need to install PyTorch).
- [Model download manual](https://pytorch.org/torchtune/0.5/tutorials/e2e_flow.html)

So the manual tells the whole story, but I was troubled with Model download.

Well let's see whether it works without introducing the Hugging Face version conflict: a free tool which knows it's own models, would package proper versions along with their software perhaps.

You still need to accept the licence on their page of this model at hugging face.

You need to provide access to token of Hugging Face, where you need an account:

```bash
huggingface-cli login
```

Then you can download the model with torch:
```bash
tune download meta-llama/Llama-3.2-3B-Instruct --ignore-patterns "original/consolidated.00.pth" --hf-token <YOUR_API_TOKEN>
```

Let's see in the next days whether I can finetune it a little.
