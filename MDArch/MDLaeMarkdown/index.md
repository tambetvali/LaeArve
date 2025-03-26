# Laegna Markdown

Markdown, similarly to ASCII, can be extended to create new types, which utilize the power of Markdown, but create both higher semantic and also syntax rules.

Markdown format of ours is like a Txt used to be - for every component of our systems, it's meant to be solid and available, without creating dependencies into other parts of the system, such as Spider depending on whole Client (rather, one should be able to copy some files of a Spider, and include with full code into their separate project - they can change and modify it then, for example removing our base classes, which depend on our project, and detecting important parts of the document themselves; we consider ways to refactor our code, including someone else creating a really tiny library of only one part, under CC or suitable licence - I am not so sure about the licence, even collaborators should mind if someone is having GPL instead of CC, or wants to buy something from us - I think this means each developer, including the people they rely on, based on the licence, to be supportive in this).

## Use of __\*...\* vs. \_...\___ and __\*\*...\*\* vs. \_\_...\_\___

Rules:
- We use *strong*, *emphasis* and *italic* equally where it's invisible, such as in titles. Because it's _meaningful_, we can parse this.
- We use asterisk to relate to a term, two asterisks to define a term, underscore to emphasize a term not introduced, thus rather a value than the term; meaning rather than text itself. We use two underscores to emphasize things such as "cats are smart", where we don't introduce cats neither smartness; but two asterisks to say "laemath is the name of our system", where we introduce laemath; or to say "continuous fractal systems" as _we are going to use_ this term for a specific meaning.

This follows Markdown: while visually invisible, as both ways are easily readable, we make a clear distinction between the two. We also apply that we are happy how it looks like, when rendered - it's invisible, rather metadata, but for user or reader, rather trivial, which one is meant.

TODO: I personally fail, in many cases, to use the right one: I will reread the texts on this site over time, and replace things.

## Laegna Numbers

To separate them from words, specific font is expected. We format them as code: `A`.

It's hard to separate from variables, but if you need to, use perhaps you can use ``A`` as variable despite I did not see this in standard - it works.

## Processors of the site

Processors of the site, based on the syntax, would add metadata to the elements; for example, __definitions__ would be formatted.

Consideration: we live in an age of AI, and we rather _break_ our rules - it's enough, almost a validation set vs. training set, if some of the definitions are left out, or if you see in standard __definition__:, but add comma and braces. If we don't implement this in any way, we might proofread, edit and fix it somehow, but if you would fail a style - it's more important and more readable. We can apply not only more rules, but also an AI to detect such cases, and we can work on the case of discretely checking everything. I think the AI does not fail if there are mistakes, it's just a noise - noise is sometimes deliberately added to AIs, and they can also understand if some files are *better formatted* (for example I did not introduce "better formatting", because here I add nothing and select nothing to / from it's original meaning, so I'm not instantiating global or local term).

For example, an AI, wherever it meets __word__ form, it would register the word and try to attach it as attachment where it needs examples of use; where it meets **word**, it's rather thinking something else.

Failing the standards: for example, __definition__ here is example, not a new word - but I don't think I would fail the standard; rather the standard would fail me otherwise. If "definition" goes to a dictionary as getting important evidence from here, we can resolve the case slowly; but we don't keep it all 100% consistent all the time, but rather we can proof-read certain versions of the dictionaries, for example, and set them as human example including the fix (before and after, and the considerations).