# 🔼 AI database

An additional development server is an "AI"; a server, which collects tasks for the AI. Normally, one would commit to Flask and an AI at the same time, but might include different content: AI's, and there are different AI databases, different scopes and versions of the same data.

I think the data could go into:
- Collections
  - Batches
    - Indexed by ordering: while initial training of an AI would use like 50% of it's database, the following fine-tuning contains random items from additional database from the previous training; as compiled into the format of model it finally has: perhaps some of the weights are developed to the end. It could have a memory AI of statically fixed biases, but it could map this to different position in it's own work, but then use for some feedback.

Our dream:
- We can create intermediate fine-tuning collections, where we use Git add-on to merge the trained brains, which asks for brains to merge, and to upload the merged brain. It would collect information about knowledge bases "copied" from one AI to another etc.
- We want to create a _relative_ system of R and T, if we don't find a solution: _R_ is the _solution space_ and _T_ is the _solution_. Where we have old output, it maps to specific solution space it had: we will update it's base _in correlation_ to this solution space.
  - We can fix the old patches, where the correct answer was given, but it's now changed; either affecting the new truth value, or affecting the actual truth back then, where "Truth" is what you have to say and what you have to learn to say; I think this is multidigit number, because it's in aspect one and in aspects another.
    - For example given an implementation appeared after an Issue to git watched by an AI. It would use implementation details, which do not need to be referred like this back then, when the solution was not implemented. It could have been a free selection.
    - For example the architecture, which was among the list of solutions probably back then as well, and should influence the AI in _intitial state_ with the old status and now as one probable future at the best; where the implementation details influence the _target state_.
    - In label set, the _version_ would appear as mutable variable for an AI, where it can always learn the version for some penalty (it should be able to see it in history).
- We want to create statistical solutions of the content. For example, having a set of truth values from different probability sets, in different areas as well: but united, the random samples of different statistical scopes still create the effect, where the united result can be reflected and probabilities of the correct answer would reflect back. If Laegna variable types are used in an AI: I hope to create a switch, which would reflect PyTorch, including Tensors and Matrices and Differential calculation, in Laegna numbers in way that each of the operations can be included.
  - Possibly, I rather need a _simpler_ AI system to start from, but one where some GPT models are still implemented.
  - Ideally, I have hooks for 4 basic math operations, class to operate with number, it's display and input in different conditions (some code would contain Latin numbers, but each use of __str__ could output visible Laegna number, and input boxes and to-number conversions could easily reflect the change; if the program works itself with string representations, it might need a little bit of manual work or automation). Herein, I would change the number containers and associated operational spaces, for example having Tensors to contain each dimension of the number.
  - Perhaps I could affect the input and the output of the gradient calculation, and some number mappings, to still utilize the existing theories and not be required to write them; for example, provers could be mapped statically available Laegna numbers in way that they always relate to existing proofs. We can use some decimal number space to contain all necessary properties: Laegna system is designed to exist inside space and time.

## AIDB in our server

  - We can associate documents, generators, generated pages and their summaries with embedders, which can create embeddings to the whole set. We can encode generators to several subsequent levels of tree map pieces, each being a dimension instead of 4 levels of subfolders; we could actually give it a set of possible content items of this, and it would generalize the resulting link into something we can use.
  - We could create a bot, which interacts with folder queries and learns some important properties of folder trees, typical positions etc. It would just let the bot navigate in space of pieces of this information, mapped into some matrix space of request and response space, and related queries to filesystem and dynamic content; it should generate some tokens of that information at the same time when AI generates it's tokens; I don't know how much stability these systems need, but probably there could be layers of time (and space thereof). Thus, when in vision of this bot you change your context lines and items, the content would change dynamically, and the AI could see dimensions in document and it's goal with it, whereas the librarian bot would change it's projection of hard information properly.
  
## Forum pages

A Question:
- A question could be entered:
  - I paragraph reference for small bots.
  - Text with the question
  - Different versions of it

The question appears under version control as well.
- Form would be filled with WYSIWYG, created in Markdown HTML block
- Form Template would convert this into Markdown (resulting GET and POST items as template input), and use another template, which contains the output Markdown. It has a header that it's a Database item, and the identificator: in which target, with which initial id it should be added; id can get additional number if it's not unique.
- The generated database item is a named target for code for modifications. "Named target" would be a whole http link of another target on another page, as a target: the other page contains template for changing the form content, given the original form as input.
  - The summary or target summaries should give some input, which chapters are Db inputs and which one is the source form page, which could also be read with Json: in case you add hidden properties from Python script, this would be visible in Json; for example you invoke a Python template, but it's not visible in HTML form when attributes are added to content.
