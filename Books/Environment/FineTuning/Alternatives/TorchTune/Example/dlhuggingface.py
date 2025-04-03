import os
import requests

def download_file(url, output_path):
    """
    Download a file from a URL and save it to the specified location.
    """
    print(f"Downloading from {url}...")
    response = requests.get(url, stream=True)
    response.raise_for_status()  # Ensure successful download
    with open(output_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    print(f"Saved to {output_path}")

def download_qwen_model(model_name, base_url, output_dir):
    """
    Download Qwen model files (config, tokenizer, and weights) from Hugging Face.
    """
    os.makedirs(output_dir, exist_ok=True)

    files_to_download = [
        "config.json",  # Model configuration
        "tokenizer_config.json",  # Tokenizer configuration
        "vocab.txt",  # Vocabulary file
        "pytorch_model.bin"  # Model weights
    ]

    for file_name in files_to_download:
        file_url = f"{base_url}/{file_name}"
        output_path = os.path.join(output_dir, file_name)
        download_file(file_url, output_path)

    print(f"Completed downloading {model_name} to {output_dir}")

# Define Qwen models and their Hugging Face URLs
qwen_models = {
    "Qwen 0.5B": "https://huggingface.co/Qwen/Qwen-0.5B/resolve/main",  # Update to the actual path
    "Qwen 3B": "https://huggingface.co/Qwen/Qwen-3B/resolve/main"  # Update to the actual path
}

# Allow user to select a model to download
print("Available Qwen models:")
for idx, model_name in enumerate(qwen_models.keys(), start=1):
    print(f"{idx}. {model_name}")

choice = int(input("Select a model to download (1 or 2): "))
selected_model = list(qwen_models.keys())[choice - 1]
base_url = qwen_models[selected_model]

# Define output folder for the model
output_folder = os.path.join(os.getcwd(), selected_model.replace(" ", "_"))
download_qwen_model(selected_model, base_url, output_folder)
