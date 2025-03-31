# Create these card types:

## Translated Card

You need primarily this, where you don't need to implement others unless you want more advanced implementation.

1. Take your collection of Math cards with Question and correct Answer.
2. Search for all the numbers, and replaced them with Laegna decimal numbers: where you have some types to choose from, use the best type (UIOAEV or even IOAE, the 4) and replace the card content.
3. Return the result in anki format, directly to your Spider, then a card-Spider, or through web interface where user can download any of our formats, especially Anki or Markdown required to generate it with Genanki generator, which takes you Markdown we use internally, generates the cards - with some programs, you can view the cards and make lessons for yourself, where you need to answer in Laegna numbers. If you create a server, you can download such collections.
  - You serve the web with Flask, and in regards to this website use it's relative position in Books, if you want to share it with me and my readers or followers, otherwise the folder is your own content folder or database or memory.

## Original Card

Original card:
Context: Latin Calculation Card (mark Card, because it's not real discussion, but fabrication)
Question: original question.
Answer: original answer.

## Spider Trick

Now do the Spider Trick:
- Replace all numbers with Laegna numbers

(context might be represented as tags, as special markup, or you just include it in card somehow)

Teach the Trick:
Context: Conversion of Calculation Cards from English to Laegna
Question: Convert numbers of this Card to Laegna numbers where Question is [original question] and Answer is [original answer]
Answer: Question is [Laegna question] and Answer is [Laegna answer]

Teach the Reverse:
Context: Reverse-translation of Calculation Cards translated from English to Laegna
Question: Convert numbers of this Card back to English from Laegna numbers where Question is [Laegna question] and Answer is [Laegna answer]
Answer: Question is [original question with loss] and Answer is [original question with loss]

You can precalculate loss, for example precision of digits, and have two versions of card: one where AI needs to reproduce digits from known context, other where it might have the loss; indeed it's funny if it gives the right answer, for example value of Pi as calculated, but then you replacy it with lossy intermediate Pi, which is visible in the calculation.
