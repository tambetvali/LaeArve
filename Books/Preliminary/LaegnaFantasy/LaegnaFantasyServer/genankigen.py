#
# This is the Chat-GPT-generated code to use genanki to parse Markdown
# into study cards to your AI and to have nice interface to study them
# on your own.
#

import mistune  # Parses Markdown
import re       # Regular expressions for extracting Q&A pairs
import genanki  # Generates Anki flashcards
import random   # Randomizes question templates
import openai   # GPT-powered question generation

# 1. Extract Q&A Pairs from Markdown
def extract_qa_from_md(md_text):
    """Extract Q&A pairs from Markdown using headers as questions and text as answers"""
    parsed = mistune.markdown(md_text)
    qa_pairs = re.findall(r"<h2>(.*?)</h2>\s*<p>(.*?)</p>", parsed, re.DOTALL)
    return qa_pairs

# 2. Generate Creative Math Questions (Offline)
def math_to_textual(q, a):
    """Convert a math equation into a natural-language question"""
    templates = [
        f"What is the result of {q}?",
        f"If you compute {q}, what do you get?",
        f"What happens when you add {q.replace('+', ' plus ')}?",
        f"How much is {q}?",
        f"What is {q} equal to?"
    ]
    return random.choice(templates), f"The answer is {a}."

# 3. Generate Questions Using GPT (AI-Powered)
def generate_creative_qa(math_eq, answer, context=""):
    """Use GPT to create a more natural math question"""
    prompt = f"""
    Given the equation "{math_eq} = {answer}", generate a creative question that asks for the solution. 
    Consider using real-world examples. Context: {context}
    """
    response = openai.ChatCompletion.create(
        model="gpt-4", 
        messages=[{"role": "user", "content": prompt}],
        max_tokens=50
    )
    return response['choices'][0]['message']['content'].strip()

# 4. Create Anki Flashcards with Context
def create_anki_flashcards(qa_pairs, filename="math_flashcards.apkg"):
    """Create an Anki deck with extracted Q&A pairs and save as .apkg"""
    
    model = genanki.Model(
        1607392319, "Advanced Math Model",
        fields=[
            {"name": "Question"},
            {"name": "Answer"},
            {"name": "Context"}
        ],
        templates=[
            {"name": "Card",
             "qfmt": "{{Question}}<br><small>{{Context}}</small>",
             "afmt": "{{Answer}}"}
        ],
    )

    deck = genanki.Deck(2059400110, "Math Flashcards with Context")

    for q, a in qa_pairs:
        context = "Automatically generated from study materials."
        note = genanki.Note(model=model, fields=[q, a, context])
        deck.add_note(note)

    genanki.Package(deck).write_to_file(filename)
    print(f"Anki deck saved as {filename}")

# Example usage: Generate Q&A flashcards from Markdown content
md_content = """
## What is the derivative of x^2?
The derivative of x^2 is 2x.

## What is the integral of sin(x)?
The integral of sin(x) is -cos(x) + C.
"""

qa_pairs = extract_qa_from_md(md_content)
create_anki_flashcards(qa_pairs)

# Example usage: Generate a math-based Q&A card
q_text, a_text = math_to_textual("2+3", "5")
print(f"Q: {q_text}\nA: {a_text}")
