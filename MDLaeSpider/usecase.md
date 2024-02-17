# Use case

This is the througout use case for the end user; I hope the AI would understand what I want to do with Flask - rather than messing with HTML and the templates and other standard cases with "millions of pages of documentation", I would be happy if I get ready with 100 pages with my own math, where the ChatGPT has only studied for now that sensitivity might be based on Synesthesia, a case I described some 10 yrs ago; after me documenting it more, GPT-3 suddenly "knew" it :) But I would like to go on with my math..

## User Story

User story is this that they implemented this AI fine-tuner in CoLab, perhaps even in their home computer:

``` python
import json
from pathlib import Path

# Download simple AI model
tokenizer = GPT2Tokenizer.from_pretrained('gpt2-mini')
model = GPT2Model.from_pretrained('gpt2-mini', tokenizer=tokenizer)

# Load Q&A pairs from local JSON files
def load_qa_pairs(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)
    return [(q['question'], q['answer']) for q in data]

# Iterate over Q&A pairs and feed them to the AI fine-tuner
def train_ai_model(qa_pairs):
    global model
    for q, a in qa_pairs:
        # Fine-tune the AI model with each Q&A pair
        model.fit(q, a)
```

Done this, they started to search for mathematical training materials, especially for infinities ..where they found our system, when it was ready.

## Our story

We got a system, which was able to produce millions of pages of infinity math by randomization of numbers, exactly what the user needed. They had time and will to feed millions of pages of documents to their AI.

Thus, finding a small and simple manual at our website, they basically implemented this in 10 minutes to fill their day with glory and joy:

We made the following web page:

``` python
import numpy as np

@app.route("/math/additionTask", methods=["GET"])
def main():
    a = np.random.randint(10)
    b = np.random.randint(10)
    c = a + b
    type = np.random.randint(3)
    # Develop question answering skills
    if type == 0: puzzle = json.dumps({"Q": str(a) + " + " + str(b), "A": str(c), "D": None})
    # Develop skills to find additional materials in documentation
    if type == 1: puzzle = json.dumps({"Q": "a + b", "A": "3",
                                     "D": "In early days of Microsoft, a used to be " + str(a) +
                                          " and b, no surprise, used to equal with " + str(b)})
    if type == 2: puzzle = json.dumps({"Q": None, "A": None, "D": str(a) + " + " + str(b) +
                                                                " is " + str(c) + ", unless there is Major Force, in which case you are not responsible."})
    template.set_body(puzzle)
```

This was our proof of concept using classical math, whereas we planned to implement our own math.

## Where user found us

From out documentation they found:

To teach your AI some simple addition and substraction, you can use our web page trivialmath.ai, whose code was given in "Our story".

They also found even simpler parser than ours, with this example:
``` python
import trivialmath as tm
tm.connect("http://www.trivialmath.ai/")
for Q, A, D in tm.fetch("/math/additionTask"):
    print("Question: " + str(Q), "Answer: " + str(A), "Context: " + str(D))
```

The user felt this one was really trivial, unlike anything they had seen - perhaps, they thought, they would still make it more trivial by setting 6 as upper bound for a and b ..but since they did not want to waste their valuable time to non-trivialities, they decided to use it as it is.

They implemented their code and reached this, based on two examples of them, to get their AI to really help them with addition problems they used to solve every day:

``` python
import json
from pathlib import Path
import trivialmath as tm

# Download simple AI model
tokenizer = GPT2Tokenizer.from_pretrained('gpt2-mini')
model = GPT2Model.from_pretrained('gpt2-mini', tokenizer=tokenizer)

# Load Q&A pairs from local JSON files
def load_qa_pairs(filepath):
    tm.connect("http://www.trivialmath.ai/")
    for Q, A, D in tm.fetch("/math/additionTask"):
        bQ = bool(Q)
        bA = bool(A)
        bD = bool(D)
        if bQ and bA and not bD: yield Q, A
        if bQ and bA and bD: yield Q + " considering that " + D, A
        if not (bQ or bA) and bD: yield "Is this true: " + D, "Yes!"
    
# Iterate over Q&A pairs and feed them to the AI fine-tuner
def train_ai_model(qa_pairs):
    global model
    for q, a in qa_pairs:
        # Fine-tune the AI model with each Q&A pair
        model.fit([(q, a)])
```

Now, they could happily reach back the dice game with an AI assistant able to sum the counts on the dices; they did never program again, but happily lived from the dice games.

# Our experience

One ending: Analysing our usage statistics, we slowly reached the results ourselves: the better maximum of a and b would be 6 and 6.

The true story: indeed, actually we implemented Laegna math, and many complex problems got trivial.
