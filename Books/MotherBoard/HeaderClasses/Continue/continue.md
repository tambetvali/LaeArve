# Task to Continue: the VS-Code chatbot and separate application in Windsurf, where
I use the free version here, as Windsurf was only some trial they have no functions outside. VS-Code somehow even works in GitHub, where you can use it online if you do limited use.

I gave this task to __Continue__: (notice if I would not like an encyclopedic item, I would put the colon inside the bold mark, or make it personal for this file by using parenthesis)

_Notice_: the code is not tested, because if AI does not complain, you can fix errors with them; the Cascade AI with CodeLlama because it's aspect of code, which should make sense by it's model, and my task as I have some experience with it.

__Notice that some folders, which contain versions of app.py: you can try them with "`flask run`", to run them in Python server and use with http.__

_Create this code_: _in python file, convert each line starting with "#" into markdown line, and when there is whitespace empty code lines between them, ensure there is the whitespace. It's a class which takes in "\*.py" file and returns Markdown string when asked by \_\_str\_\_(self) function. Rest of the code, along with comments, which are right before code lines without empty lines between, will go into "\`\`\`python ... \`\`\`" multiline blocks, so that if only the code from the blocks is copied - it should work. Also create flask app, which prints list of *.py files in current folder, and uses the parser to display them if they are opened with "*.py.html" extension; then, "download" is after the link and inside file display in markdown conversion: from there, the original source will be downloaded with original file name, and *.py is the extension instead of *.py.html, in browser bar from flask. Two files are generated: app.py and markdownclient.py, where the client is like server, but it's later using the architecture from client side of the main server, which could be directly used by spider somehow, with local copy. You can also give code for Spider: given the url, it crawls each code file by it's link in given format, and creates folder with each *.py.html, and each *.py file._

##

Notice: it's for the free model CodeLlama-13b, while you can be more detailed for larger model should you pay to the provider.

It creates code, which is more or less free to use: task, definitely, is under my licence. I would refer to their better work if they one day, reverse-engineer this to mention the authors of prototype code (T), and authors of search space (R), including the authors of search and modellization.

I don't have this as priority task, but those code lines should also exequte given that comment starting with paragraph mark is on the first line, or first and right following lines. If somebody is back-linking to you, their source is reflected by your server and you can use this as database with Spider; somehow we should be able to create intelligent embedder bot, which learns which documents to serve: getting score for how well it's docs are used, in early phases and later, and which also explores dynamic search space, where
we generate Q&A. The AI should learn from examples of conversion, which give a book of
tasks and conversions of Laegna numbers into those tasks with explanation; additionally,
an automate can randomly replace integers with Laegna numbers, leaving their expressions intact. The bot should learn to say "ten", but write Laegna number, which either reflects the digit-mapping, where it's digit-wise converted, or the written form, where value space for decimal digits is preserved safe. I convert in some free math data cards, just randomly the integers into laegna numbers and create a feed of either the converted cards, or also the conversion information. Manually created documentations should refer to this format.

