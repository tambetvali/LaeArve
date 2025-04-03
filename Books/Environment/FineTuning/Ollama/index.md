# Ollama

You can download Ollama to fine-tune your models.

Downloading the model:

You have to "run" it: it will be automatically downloaded and kept.

Or you can use:
```bash
ollama pull <model_name>
```

It's funny it was the first one I tried to run chat models, but now I found it again :)

Training the model:

```bash
bash  
ollama train <input_model> <data_file> <output_model>
```

Running the model:

```bash
ollama run <model_name>
```

List models:

```bash
ollama list
```

Remove a model:

```bash
ollama rm <model_name>
```

Copy a model:

```bash
ollama cp <source_model> <new_model>
```

You can also serve the model.

A Python script like OllamaToGguf can help convert models from Ollama's format to GGUF. This script reads the model's manifest files and combines the layers stored in blob files into a unified GGUF file.