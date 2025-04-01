import os
import shutil

def fine_tune_model(model_folder, fine_tune_folder="finetune.tmp"):
    print(f"Preparing fine-tuning environment in {fine_tune_folder}...")

    # Create subfolder for fine-tuning
    fine_tune_dir = os.path.join(os.getcwd(), fine_tune_folder)
    os.makedirs(fine_tune_dir, exist_ok=True)

    # Copy model files into the fine-tuning folder
    for item in os.listdir(model_folder):
        source = os.path.join(model_folder, item)
        destination = os.path.join(fine_tune_dir, item)
        if os.path.isfile(source):
            shutil.copy2(source, destination)
    print(f"Model copied to {fine_tune_dir}")

    # Fine-tuning logic (replace with actual process)
    print(f"Starting fine-tuning in {fine_tune_dir}...")
    # Example: Training logic goes here
    # subprocess.run(["python", "train.py", "--model_dir", fine_tune_dir], cwd=fine_tune_dir)

    print(f"Fine-tuning completed. Results saved in {fine_tune_dir}")

# Specify model folder and fine-tune
model_folder = input("Enter the model folder prepared by the first script: ").strip()
fine_tune_model(model_folder)
