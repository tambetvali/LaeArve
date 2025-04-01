# Reference Index

While you have an AI, you have the following:
- Collection of Documents
- Chat Logs

## Processing the Documents

Most definitely, the documents need embeddings:
- Texts and their parts can be embedded, having them in complex space of an AI.

Other users can have:
- Embeddings and finetuned AI's backlinking to your page.
- Comments and in-document comments backlinking, where they choose a snippet of your text and write their comments and understandings; it should let to fix comments when the page has been changed.
- Wiki content backlogging to your page: they backlink with things, which can: fix the page (Wiki modification) or the page after given Wiki processing, rephrase the page (for example, different wording for same Q&A) or associate the page (for example, other Q&A, but having some reason to be seen together).

Based on this, we can:
- Verify that AI models we train have the following components:
  - They are able to control their _windows_ to Documents, using their API
    - So they can somewhat control the process by which they _load documents_
    - Another model can do this, like an embedder
  - Otherwise we create just embeddings to Documents
- Have the finetuner version of the Documents
  - Based on Documents, an AI is able to generate Q&A Cards
    - There are numerous trivialities, for example Q: "Give a random quote of Chapter 7" and A contains the quote.
    - AI would be able to check the case, for example, that if a chapter about a car can be properly quoted to be fast, it might associate to the case that this car is fast.
  - If generated Documents have Context of being generated documents, they can contain some typical mistakes: an AI would learn rather the objective connection between generated documents and it's output.
- AI Document Navigator
  - Document Navigator is it's internal or external purpose.
  - We need to utilize AI Callout page, which gives tasks to AI's: create summaries of all pages; create summary of 500-page dynamic creation etc.
  - Embedders should be able to learn parameters of dynamic creation
  - Document navigator should be able to create complete environment for the bot; I think it should be able to update the context: let's try to assign dynamic context, which is constantly reflecting the current and a few last states of generation.
  - Multi-pass AI would create basic answer with smaller model, then fix and extend it with larger model, we need more realtime AI: for example, it already generates initial title for an answer, first version of link collection, and some other elements of it's window.
  - Purpose of the navidator: create, update and reflect back the Context area of an AI; have learnable parameters to read back.
  - If we could get many emulations of things like little GitHubs with almost abstract code, where one line is changed or extended and there is a "standard programming language", which can create a set of customized code for five lines; the tasks are similar: they appear, and the code is changing. For some models, it could be 20-line emulated code, where the result is determined semantically, and simulated tasklists, github pages etc. This would measure the response to issues and reflections of GitHub changes; it would need to keep the current context of these lines - an AI, when operating, would have documentation based on it's feedback.
    - Real-time ability: user Would be able to focus documents and change the selection while it's answering, where really small models could reflect the current situation (I have some math for this).

# Chat log feedback

We collect the chat logs automatically, process them and feed back.

# Documentation and Chat log activists

There are bots, which generate:
- Summaries of both
- Explanations of parts
- Structured reference to documental materials

This allows:
- Users to work on this in Wiki

This is also Git-compatible:
- Pages being referred can remain in past Git versions
- Each worker has references to proper version
- For example, each time an AI has proper set of information, it might be already outdated

# Creating an ultimate shortification

The document AI would seek to reach only the _very small context_:
- It tries to summarize also that, where it can have two-paragraph context for an AI.
- It's output gets loss functions and gradients, so an AI would learn, starting perhaps from simulated environments with variable similarity mapping, how to keep the best context with the little set of parameters it got.
- It has some modifications of short context of the whole site: so, whatever is being searched from the library, it start with the description of the general book, and reaches that book then.
- We should figure out, how much we can cache our intelligent information, for example how many passes of Documentation verification would happen automatically, or for example writing reference to current selection, but the reference could be already done.
