import os
import requests
import tarfile

def download_and_prepare_model(model_name, url, output_dir):
    """
    Download and extract a model from the given URL.
    """
    print(f"Downloading {model_name} from {url}...")
    compressed_file = os.path.join(output_dir, f"{model_name.replace(' ', '_')}.tar.gz")
    
    # Download the file
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open(compressed_file, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    print(f"Downloaded {model_name} to {compressed_file}")

    # Extract the file
    print(f"Extracting {compressed_file}...")
    with tarfile.open(compressed_file, "r:gz") as tar:
        tar.extractall(path=output_dir)
    print(f"Extracted {model_name} in {output_dir}")

# Models and their download links
models = {
    "StarCoder 0.5B": "https://huggingface.co/bigcode/starcoder-0.5B/resolve/main/model.tar.gz",
    "StarCoder 3B": "https://huggingface.co/bigcode/starcoder-3B/resolve/main/model.tar.gz",
    "CodeLlama 0.5B": "https://huggingface.co/meta/codellama-0.5B/resolve/main/model.tar.gz",
    "CodeLlama 3B": "https://huggingface.co/meta/codellama-3B/resolve/main/model.tar.gz",
    "OpenCoder 0.5B": "https://huggingface.co/opencoder/opencoder-0.5B/resolve/main/model.tar.gz",
    "OpenCoder 3B": "https://huggingface.co/opencoder/opencoder-3B/resolve/main/model.tar.gz"
}

# Let user select a model to download
print("Available models:")
for idx, model_name in enumerate(models.keys(), start=1):
    print(f"{idx}. {model_name}")

choice = int(input("Select a model to download (1-6): "))
selected_model = list(models.keys())[choice - 1]
output_folder = os.path.join(os.getcwd(), selected_model.replace(" ", "_"))
os.makedirs(output_folder, exist_ok=True)

# Download and prepare the selected model
download_and_prepare_model(selected_model, models[selected_model], output_folder)
