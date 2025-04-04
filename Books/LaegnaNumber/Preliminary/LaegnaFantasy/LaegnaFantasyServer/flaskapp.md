# ☕ The Laegna Fantasy contains complete Flask Server, which outputs

The server has /Preliminary/LaegnaFantasy/ in it's address, which is the book name: it might seem like it reflects some part of the site.

Flask is running the following service:
- It connects to set of existing Math Study cards and documents
- It replaces each number with equivalent Laegna number
- It serves the resulting cards in format, which is compatible with Markdown and Anki, and each request has ?view=Markdown GET request query, despite we won't use it.
- Other versions _may_ serve also DHTML, HTML and Json or directly Anki sets. The menu would be at standard position, and the design would _reflect_ the design papers of Laegna Math Website. It needs to be uploaded at "LaegnaFantasyDevelopments", where at the original page the simple idea it has, it rather needs to be made simpler, more explanative and easier to understand as a first lesson of Laegna, coming from the world of decimals and simple programs.

It is able to return only Markdown, while you can add some HTML template to resemble Laegna site with less links: we need to have one version, which only returns Markdown, because it's the simple one to start with, to program something oneself (where one needs one, two, three classes in very logical disposition, not more, given it's not their job).

We use:
- _Python_ - Programming
- _Flask_ - HTTP Service
- _Markdown_ - Text Format

And we also create one small client called "spider.py":

It uses:
- _Python_ - Programming
- _Requests_ - HTTP Client
- _Genanki_ - Study Cards

You additionally do your own AI fine-tuner, where you use
- AI model to be finetuned, you can get it from Hugging Face or perhaps Kaggle.
- Set of cards from it's original training or rather new data of the same value and logic, because you want the optimization to _interact_, so that it's original parameters won't get _outdated_. You give random probability to those cards, in relation to yours, and you create a random seed, which can keep the linear list repetitive so that you have your original task, for example to measure performance under same conditions with other AI, which is a partial solution to the task given that there might be a random factor.
- Genanki class I gave to read the cards
- GPT-generated class (it's where it's in it's best flow) to take your cards and feed them to the AI, where you can use anki's graphical interface, and other anki tools for an AI, for previews and advanced control, each compatible with your Python and Markdown view.
