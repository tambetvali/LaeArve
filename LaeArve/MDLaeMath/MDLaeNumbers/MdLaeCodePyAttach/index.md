# Explanation
__Summary__: This is the Md folder of Python and other Code Attachments.

Here we create basic, primitive implementations of what is described in Docs, or provide the files mentioned in the Docs.

Notice: while this might be directly copied to code files, what matters:
- The implementation is essential, such as given mathematical truth and nothing more.
- We dont add any complexities; for example it's not about good design if you create HTML here, it's not about having each method implemented such as browser-specific trivia.

Code representation structure:
- Code files in Documentation either represent mathematical ideal, implementation algorithm or specific, given, complex detail of implementation such as "How to implement scrollbars properly in this browser".
- They do not provide complete implementations, where users might get lost in 500-line files getting around all types of firewalls, solving some conditions for clients with special needs, and resolve how to make appear red in every browser. Nobody would be able to understand - if we have the case of not being able to show red in every browser, we can create documentation item for it, or if it's not our own specifics pehaps some research might require us to create additional parts of the library, such as well-documented little library to just print study cards for an AI or to parse Markdown.

## Code Tree itself

Let's keep all code in the main folder, mixing all 4 packages and freely using objects and classes in one, from the other.

It's better if the list is short:
- One can view in VSCode or other editor, open some documentation folders and still see all files at once.
- This means while here in Docs each thing with a purpose has separate file or separate chapter in documentation, let's combine the classes together if they work closely together and have related functionality. To search them in this file is more easy than to search each time in the Explorer list: rather, our "Left menu" should have given number of items and not more to appear properly, and the item can have subitems in a way that you scroll specific files, where you need to relate the combined classes anyway.
