# Cards

Under documents, there are Cards.

Cards are the blocks for automated learning and they behave like dictionaries, tables and Q&A elements, so the following types exist:

* **Table**: Row and Column headers are optional, and they contain cells. Inside document, first n*n rows and columns are visible, followed by link to see whole table.

* * **Tables** are static or dynamic, and static tables can read CSV/Excel by Pandas or another format., while dynamic tables and other static tables are classes, inheriting from LaeStudyCard.

* * * **Links** in tables associate them with cards, they are made like normal card links: once you add link to the cell, it will be followed by Json.

* * **Dictionaries** contain dictionary item name and paragraphs, which are text. They can come from a class, but the class can also read a file. In Markdown, it's specified as such: Dictionary item names are with special formatting, for example if paragraph starts with bold, colon-ended part.

* * **DocumentCards** contain one informative piece of text, made in Markdown, which should not be long, and they look like cards. They have very similar format to dictionary items, where their headers/titles are of the same font, but on separate line, and Markdown is formatted similarly.

* * **DialogCards** contain dialogs, which an AI can read, and dialogs are composed as follows:

* * * **Context**: introduction element can be the context. If first block is "Context", it's regarded specially; other introductions such as "Topic" could also be detected; links inside this are special - for example if they point to other card, this card is the context.

* * * **Questions**, **Answers** and **Definitions** / **Contexts**:

* * * * Item type such as Context is in beginning of Markdown block, in bold and ending with Colon.

* * * * It's allowed to have any types of elements, for example "**Exclamations**" or "**Monologues**" could be added by user; system does not complain of unknown things.

* * * * An **AI** would easily recognize some types, such as Q&A or Q&A&D.

* * * * **Links to cards** are included in Json set, so that if the Card links another card, Json file would contain one or two levels of such inclusions, and manage to pass it to AI unless token window is too small.

Shortly:
* **Tables**: Contain datasets.
* **Dictionaries**: Contain definitions.
* **DocumentCards**: Contain long definitions.
* **DialogCards**: Contain time-sequential typed text blocks.

Features:
* **Links**: First levels of links are easily included in the same Json.
* **Markdown**: They are made most typically in markdown, even if generated automatically; showing them in markdown is easy.

# Automation

Automation:
* Cards are made for automation.
* AI student can easily follow it's structure.
* It can be converted to format of another AI.

Internal Automation:
* Along with generating a Card, list of other cards can be added inside.
* Autogenerator creates them with markdown.

# Indexing

Each Card contains index to all cards inside, which should be available at top bar; from Json link to index can be easily followed, indexing all cards in same document, same and subdocuments, or to the end of the tree.

Dynamic and Static cards are generated automatically.

For Dynamic cards, show a few examples and keep them static for a while; the rest comes with a link, which is able to generate them one-by-one or as a list (for AI lists are good).

A card can have a module to automatically generate invariants or inherited content - this is seen as automated flow of the same card.

AI can generate the cards from the whole system.

The rest of the system is also for an AI to learn!