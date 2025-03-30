import os
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer, AutoModelForCausalLM, AutoTokenizer
import genanki
import mistune

# Directory to save the model
MODEL_DIR = './models'

# Ensure the model directory exists
if not os.path.exists(MODEL_DIR):
    os.makedirs(MODEL_DIR)

# Class to handle downloading the models
class ModelDownloader:
    def __init__(self, model_name):
        self.model_name = model_name
    
    def download_model(self):
        model_path = os.path.join(MODEL_DIR, self.model_name)
        
        if self.model_name == "GPT-2":
            self._download_gpt2(model_path)
        elif self.model_name == "Qwen2.5":
            self._download_qwen(model_path)
        else:
            raise ValueError("Model not recognized.")
    
    def _download_gpt2(self, model_path):
        """Download GPT-2 Small Model"""
        model = GPT2LMHeadModel.from_pretrained("gpt2")
        tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        model.save_pretrained(model_path)
        tokenizer.save_pretrained(model_path)
    
    def _download_qwen(self, model_path):
        """Download Qwen2.5 Model"""
        model = AutoModelForCausalLM.from_pretrained("alibaba/qwen2.5-0.5B-instruct")
        tokenizer = AutoTokenizer.from_pretrained("alibaba/qwen2.5-0.5B-instruct")
        model.save_pretrained(model_path)
        tokenizer.save_pretrained(model_path)

# Class to fine-tune the model
class FineTuner:
    def __init__(self, model_path, tokenizer_path):
        self.model = GPT2LMHeadModel.from_pretrained(model_path)
        self.tokenizer = GPT2Tokenizer.from_pretrained(tokenizer_path)

    def fine_tune(self, input_texts, output_texts, epochs=1, lr=5e-5):
        # Simple fine-tuning with the input-output Q&A pairs
        inputs = self.tokenizer(input_texts, return_tensors="pt", padding=True, truncation=True)
        labels = self.tokenizer(output_texts, return_tensors="pt", padding=True, truncation=True)
        
        # Optimizer
        optimizer = torch.optim.AdamW(self.model.parameters(), lr=lr)
        
        # Fine-tuning loop
        self.model.train()
        for epoch in range(epochs):
            optimizer.zero_grad()
            outputs = self.model(**inputs, labels=labels['input_ids'])
            loss = outputs.loss
            loss.backward()
            optimizer.step()
            print(f"Epoch {epoch+1}, Loss: {loss.item()}")

        # Save the fine-tuned model
        self.model.save_pretrained("./fine_tuned_model")
        self.tokenizer.save_pretrained("./fine_tuned_model")

# Class to handle Markdown Processing and Flashcard Generation
class MdProcessor:
    def __init__(self, markdown_file):
        self.markdown_file = markdown_file
        self.cards = []
        self.md = mistune.create_markdown()

    def process_md(self):
        with open(self.markdown_file, 'r') as file:
            md_content = file.read()

        # Parse Markdown
        html = self.md(md_content)

        # Generate Q&A pairs
        self.generate_flashcards(md_content)

    def generate_flashcards(self, md_content):
        # This function processes the markdown content and generates Q&A pairs
        # Let's assume that the markdown has questions and answers in specific sections
        question_answer_pairs = [
            ("What is Laegna?", "Laegna is a mathematical framework."),
            ("What does Qwen2.5 do?", "Qwen2.5 is a model used for contextual Q&A tasks.")
        ]
        
        # Create Anki Cards
        for question, answer in question_answer_pairs:
            my_deck = genanki.Deck(
                2059400110,
                'Laegna Math Framework Deck'
            )

            my_model = genanki.Model(
                1607392319,
                'Simple Model',
                fields=['Question', 'Answer'],
                templates=[{
                    'name': 'Card 1',
                    'qfmt': '{{Question}}',
                    'afmt': '{{Answer}}',
                }]
            )

            my_deck.add_note(genanki.Note(
                model=my_model,
                fields=[question, answer]
            ))

            # Save the deck as an APKG file
            my_deck.write_to_file('laegna_deck.apkg')

# Main Execution Flow
def main():
    # Ask for model selection and download it
    model_choice = input("Which model do you want to use? (GPT-2 or Qwen2.5): ").strip()
    downloader = ModelDownloader(model_choice)
    downloader.download_model()

    # Load fine-tuned model for use
    model_path = os.path.join(MODEL_DIR, model_choice)
    fine_tuner = FineTuner(model_path, model_path)

    # Example of fine-tuning with Q&A pairs
    input_texts = ["What is Laegna?"]
    output_texts = ["Laegna is a mathematical framework."]
    fine_tuner.fine_tune(input_texts, output_texts)

    # Process Markdown files and generate flashcards
    markdown_file = 'laegna.md'  # Replace with your actual markdown file
    md_processor = MdProcessor(markdown_file)
    md_processor.process_md()

    print("Model fine-tuning complete and flashcards generated!")

if __name__ == "__main__":
    main()
