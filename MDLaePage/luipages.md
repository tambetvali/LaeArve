# Pages

First level of organization is LuiDocument, which has the following structure
- Title
---- Subtitle
--- Summary
--- Index of Chapters, where the main chapters are definitely in the same page, but subchapters can have blocks in the same page (with the same link), but full content opens by link at the end of the chapter - their own subchapters are not visible, but they can have their own content; in Index they are all mixed. Look at luichapters.md in this directory.
-- Next order Title
---- It's subtitle
--- It's Blocks
--- While the first blocks might be on same physical page, starting from a certaint blocks, the rest can be replaced with a link; the actual blocks are in separate html page - once user clicks the link at the end of partial chapter with introduction or for example first 20 rows of the table; once you click the link, the introduction is repeated in the beginning, and you jump to the position where you left off reading (if it's not very short, you have to scroll up to see the beginning)

OOP structure:
* Titles, summaries, chapter elements can have a common style, but they can be customized if the class is inherited. Possibly?
* Blocks, definitely, have their own rendering.

From the properties panel:
* One can choose short view, where only the high-level data or outline is visible on the same page.
* One can choose longer view, where very long lists appear on subpages.
* If available, one can also choose the longest view, where the lists appear in-place.
* Possibly, one can combine higher level documents with partial representation of lower-level documents. Lower level documents, therefore, are linked from higher level, where *the link is a separate block*. Inline links can be added, but each page is contained. If the link is to: Subdocument or separate Document, it does not need to be inline.

## Menu

Menu has short list of main elements:
* Once you click a link, you open a Document
* More important chapters of a Document appear inside.

## Configurable

To decide, whether to appear on the same page or subpage:
* One can create a class, which decides this based on the properties at right side.
* Each chapter can have a "cut-off block", which is an instance of this more generic class; it has set of initialization parameters in a dictionary, while it cannot control all of them. From this cut-off block, this chapter and all lower level chapters are cut off into separate page with separate URL, which copies the beginning of the same chapter, but continues from the cut-off block until reaching the next higher-level title.
* If chapter content is invisible, nothing will be done with it - it can be expensive calculation, not only static content, so it's lazy and it does not load what is not displayed, and it does not list that content, but immediately stops.

## Generational

Function can yield chapters with title, subtitle, blocks and the cut-off block (where the iterator might be break'ed by client); if it's not halted with "break" statement by the client, it will continue.

## Paradigms

* HTML: This is the visual paradigm, where chapters and blocks are visual.
* Json: Chapters create a structured Tree, whereas Blocks render Json separately, so the content can be meaningful and have metadata or lables, including the chapter titles (tree branches, not only nodes) can have this machine-readability, and they are rendered separately.
* Markdown: Markdown structure is used - "#" for title, "*" for list item etc. This is for printing, so instead of link label only, each link in Markdown has label, and then the visible link - you cannot click it, but you need to see it. For example "Full content (http://.**.com)".

# Sub- and separate Documents

Subdocuments:
* For example table can be generated, each row containing a number, and when you click on it, number card will open with Q&A, or list of number cards open, each is a link to Q&A.
* * In Json, it's especially important that Q&A is separate page, object containing at least the properties "Question" and "Answer", perhaps also "Context". This is important consideration, whether your AI would allow the Context - otherwise, context can be in beginning of the Question, such as { Question: "Division context is whole numbers, always rounded down\\lfHow much is 3/2", Answer: "3/2 is 1." }, with original form: { Question: "How much is 3/2?", Answer: "1", Context: "Integer types, rounded down." }
* * Based on the same card, Q&A's can be generated automatically - especially, I might later implement a simple AI such as spaCy, which will have a list of example forms for given question or answer or context, such as "3+2", "How much is 3+2?", "Add 2 to 3 and give the answer.", "2 apples are added to 3 apples. How many apples are there?" - this will remove some of the hitbacks from the fact that AI cannot train well if the form is static, it would fall into very certain tracks. In such case, the card will give a default form, and link to dynamic generator of Q&A pairs.

Separate documents:
* Links can be given to separate documents, which come down in the tree.

# Automatic selection

From properties, an user, especially an AI with some additional options might be able to choose to iterate over all cards either in given document, or in given document and it's subdocuments, or subdocuments starting from given chapter, or also the other documents down from the tree.

# Strictness of the Structural Tree

Structural Tree is strict:
* Documents
* * Subdocuments
* * * Documents down in the tree

User can have each chapter in separate page, not only the ones with link.

This is visible in link structure:
* The user, when changing documents by parameters, is redirected to correct link, or they open them directly.
* Each subchapter, subdocument etc. will have a structural element: new part is generated to the link. There is slight paradox that the tree is not really consistent given that we change the chapter structure, and it is changing even dynamically - we won't add part to the link in such case. Rather, some part of it is logical: lets use another separator inside document, not "/", but another encoding would separate the in-document structure tree; for example /doc/subchapter/subsubchapter is added when navigating *inside* the doc, and the Spider does not count "/doc/" in a way that subdocuments must add new parts - instead, leaving the document, only it's first part is left and anything after the "doc" part is gone, only containing the next level of documents; subdocument separator can be "/sub/" and also, one we are gone from the document and it's subdocuments, "/sub/" is gone but it's still automatically verifyable that we are down in the tree.

# Why we need all this?

We need, especially clearly, the AI to be able to learn given content:
* Either by higher-level position of the whole topic.
* Or by lower-level chapters, such as studying specific topic.

# Autogenerator

Finally:

From user's perspective, they add to their AI:
* Specific chapters to learn
* Whether they also learn subdocuments or only branches of the given document; other documents downtree or only this document with it's subdocuments.

Given that their AI can learn only specific formats, such as Q&A, but not D (document), they can specify a search criteria:
* For their chosen branch of the tree, with chosen subbranches:
* * They decide the card format: where there are multiple formats contained in the links, only cards of this format will be selected.
* * The page can always find them a new card to learn.
* * They can assign probabilities to branches, documents and card types and card branches, as cards are also in branches.

The result: while Spider would be very slow to do all this, the Laegna Math Website is able to give them, from given branch, cards with specific types and content with specific probabilities, for example branch x is opened each time with 10% probability, and two types of cards inside with 50%:50% probability - users can add any numbers, but we use softmax to have the final probability associated with branch links (there are not too many branches) and configurations, for example:
* 70% probability to get numbers up to 5 digits.
* 15% probability to get numbers from 6 to 100 digits.
* 15% probability to get numbers from 100 to 1000 digits.
