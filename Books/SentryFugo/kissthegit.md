# KISS the Git

We utilize the KISS principle in several areas of programming.

First: let's try to create a version of distribution of editor such as VSCode, choosing the one, which allows by licence.
- Let's modify the language files to allow _Documentation Editors_ to utilize the following:
  - It's _Document Explorer_ rather than _Code Explorer_.
  - There is _Document Control_ rather than _Code Control_.
  - We add _media editors_ and _media viewers_ to _code editors_.
- Let's modify an Open Source AI Assistant:
  - It's not just Instruct to allow Code Assistance, but a _General Assistant_, which is _Aware of the Context_.

What we get:
- File tree management, structured document tree.
- Source control, version control.
- Extensibility.

> We can safely leave this work to programmers of those systems, but we can experiment with language files and adding modulable or open source components, such as GIMP, Visual HTML Editor, Tkinter or Qt Visual Editors etc. For example, user could create APIs as Forms, then ask the AI to implement the described backend. In era of an AI, the user learns APIs, because a good API might not require technical thinking! Users _are_ able to create forms and describe, how to fill them - even for an AI.

-------

We have Git Source Control.

We need to implement the following to use it:
- Wikipedia could move it's history entirely to Git, given it has Open Source Database Format; the latter could be _virtualized_ to Git - it could be aware of database items. Rather create Git extensions than do it yourself, leaving the hard work to where it belongs - until then, at least we have our Documentation format like Handmade Database, favoured in era of an AI, where we valuate manually created content to be _intelligent_, even manually structured formats.
- We need to associate files with their Git items, where the user features to view history of generated content, pages and documents, or parts of documents, and their Diff, should be based on functions of Git. We don't want to double-do this work and we rather assume, VSCode is very good editor to work on our _Structured Documents_, and we got Markdown, UTF-8, several simple, but brilliant things to start from; plain Txt is now structured!
- We need to make our pages _statically accessible_, which means the dynamic aspect can happen entirely at user's side - as we develop the Spider, it should also be able to start server and to process the content.
- Thus, our linking system becomes such: old versions from Git can be awakened, and the user can either work with, or refer to older versions.

Where we need it:
- When user links Wikipages to fix our content of certain generation, it should work against proper versions, should the actual generator lose compability; for example fixes of user are somehow generalized and accepted.
- When Models and Embeddings are created, this can be hard and valuable work and becomes useless, when the documentation being embedded does not exist any more, in the same form. There could be an AI, which is able to provide efficient context for an _older version_ of our docs, and this could be the most trained and intelligent generation for it's users, who want to stick with that until a major update.
- We don't want to program Source Control: we would just replicate functions of Git.
- Our users, KISSing the simplicity, do not want to implement anything, but we are more or less utilizing the existing standard, libraries and frameworks to achieve our results.
