# Developer Books, Tools and Installation

<big color="red">If you don't want to join my project, this is the general plan for AI-based development, documentation control and scientific work, where you can modify my document to allow contributors to join your own effort; questions are welcome and you can add them to my GitHub Issues, if you cannot create your project based on my work. Using our effort is based on CC (creative commons) licence of this project, which is indeed supportive for general scientific work and open source programs.</big>

> __Developer Notice__: The _user_ software and the _developer_ software are not contained on separate pages for __Laegna Math Website__ or __Laegna__ and _SpiReason_. We live in era of AI, and this standard coding here can be successfully done by an AI - so you should not be shamed when facing a classical development environment, which now is becoming rather AI-assisted tool to control AI systems and environments, where the AI is able to put your simpler ideas or standard behaviors into textual format of Code, introduce you where to put this code and how to execute it, and finally as AI is going to do several mistakes - you can, running the software, copy back the terminal output of errors and successful runs, and describe the working program in terms of it's behavior etc.

- Your mission is to keep a good, strong documentation about what you want to program.
- Object Oriented programs are contained in structured system of files, and they have basic structure in which we call "Class Names". Each class contains some functionality. You need to study class and variable name conventions and with AI and docs, set up your naming standards.

    > __Example__: you want a program, which for your woodwork, takes all block materials and multiplies the width, height and depth (x, y, z), then adds the volume for every size. You can tell it: by class name convention, files and classes for calculations start with "WoodCalc" prefix - where you use _CamelCase_ -, user interface or input/output is in classes with "WoodTerminal" prefix and all the other classes start with "WoodMisc", where the filenames correspondinly start with "wc", "wt" and "wm", where it's visible for other developers that you particularly don't like math, but you can do with poetry. Once you got all this documentation - in one md  in your docs folder (in my case their names start with "MD-") that you want to calculate the volume of wood blocks, in other that you want colored output and in third that you want this filename and class name - API - conventions. Standardizing API positioning in files is rather standard bookkeeping and library work - the result is called a "library" as it has some nice naming convention and outside-structured look, especially if you package it to library and give others also standard naming convention to get the volume where input is list of blocks. After done all that, you just express your AI system of editor, such as VSCode, that you want it to implement the described project; after this you have some cycle of error and success feedback and you should document this: when error is solved or you are happy with something, you add this information to md files of documentation so that the AI would not forget, but learn your argument.

If you follow these instructions and also read the books, you should be:
- A.I. Developer or User (user listing of programs and content is also here, developers can instruct where needed).
- Developer and User for Laegna Spireason and it's related materials.

You can view materials at YouTube:
- Download 3d, 12h, 10, 6h, 4h or 1h video from known University such as Oxford or Cambridge, or from public free university such as Edureka.
- Download "... from Scratch", where it's programmed withou using a library: instead, you see the base mathematics in code (low-leve)
- Download the ones for PyTorch, for powerful interface.
- Download the ones for SciLib, in videos you find some easy-to-use Science and AI kits.
  - ChatGPT in 5 Minutes
  - ChatGPT Tutorial ｜ Chat GPT Explained ｜ What is Chat GPT ？ ｜ Edureka
  - In Linux, you can use YouTube Downloaders to watch them offline or use as separate CD; there are also online pages, where you need to enter the link to download.

I think I would have copyright issue by submitting those free books here as document files - so I have the content listing instead. If the book is not available, just use the title to search a book with such content.

Given we want you A.I. to know each related technology, you need to download these books into your
folder, which in my computer is named "Library4all" and added as GPT4All collection "All the books
in the World", which might mean that the A.I. would have vague memory of all the other books,
but know these in order. You don't have to read the books in this purpose, this is only A.I. educational
material to be added like this:

* Download GPT4All in you Linux subsystem
* Install it and let it download all the files
* It creates a folder somewhere, almost hidden
  - __GPT4All Folder__: /home/tvali/gpt4all/bin/ in my case.
  - __tvali__: just my name on each and any of my systems.
  - _GPT$All Models Folder_, __Bonus__: /home/tvali/.local/share/nomic.ai/GPT4All/
  - _In models folder_: Delete "localdocs_v<x>.db" if your Book Collection gets broken
* Add your own Documentation to your own folders
  - It has one main folder, like "Documents", and 2-3 or 3-5 or perhaps 10 subfolders.
  - GPT4All can only see subfolders as separate units, "Documents" cannot be library itself
    or you break your logic or turning slow collections on or off.
* You can download Laegna in each format, and use Microbot as separate collection
  - This is exception to not including, because related to parent folders Midrobot is very
    small and not visible there in terms of resources it uses.
  - _This is optional_, __DIY__: because basically you want to do something yourself.
* Install Jan, another A.I. chat you configure to be stupid, but answer fast questions. It cannot have access to your documents and do research, but it can remember some of the chat.
  - If it starts to answer previous question instead of the current one, create a new chat.
* Use of resources of each model size is exponential (square)
  - So the 2 times smaller model is actually exponentially smaller, especially somehow.
* Now download "LM-Studio-0.3.13-2-x64.AppImage" from LM Studio, and copy it to "Applications" folder in your home.

Install the models. In this reference, very weak computer is assumed; each model has alternatives of bigger size.

- __Jan__:
  - Install model "qwen2.5:0,5b"
  "llama3.2:1b"
    You see the llama model is 2 times bigger, so 4 times slower.
- __GPT4All__:
  - Install model "Llama 3.2 1B Instruct"
  - Install model "Qwen2-1.5B-Instruct"
- __LM Studio__:
  - Model "smollm-360m-instruct-v0.2"

Each of those models is able to properly talk, but they are at different speed and intelligence level, balanced to how advanced the programs are and what they do - a robot, which cannot have access to your own documents, can subsequently play the more stupid role, but answer questions in moments; for bigger model you wait, but your knowledge base gets analyzed so it needs attention - it has 2-8 times more and is subsequently 4-64 times slower.
- LM Studio is rather for doing advanced work.

From Hugging Face, you can download your own models to train, and perhaps it's documentation-aware (needs question, answer and context instead of question and answer).

You check the licence of each model and program.

Now you should have Free Access to your documentation, and one simple robot, which has wide knowledge base but gets confused when thinking. Some other robots wait a long, analyze your knowledge, and answer a little more properly.

While you can also download ChatGPT for advanced conversations, and give it your files you assume it to read.

Also, for accessing all development files in GitHub in additional environment, download VSCode programming environment and install Continue, download the documents.

And download Windsurf: while you might get a trial of code editing, you get more working copy of conversational bot; initially it was available offline, but not any more - but now it still works in VSCode. You don't have this problem if you pay them - in each case, "Cursor" did something meaningless: it destroyed my files so that I could not access the project any more, running automated script on each file; other bots don't want to do this at all, rather they ask you to save it into Git and keep histories.

In VsCode, also, add my GitHub page of bot, and you get a conversational interface in each case; able to create you most interface code by docs probably, but not all content code - I want to basically implement some numbers.

Create Notion.so page and Zapir account to test a bot on it; you get some experience but the bot will run out of trial time unless you pay. Notion.so has some space for limited set of documentation, and intially it has some bot, with renewed time probably sometimes.
- Give the Link to Laegna Notion.so collection as you create one chatbot "Elise and Daisy chat" where you intruct the bot to express only things it can scientifically confirm, in direct assertions, and the rest in choice of same-meaning words, intonations and poetic speak to express "it's intuitions".

There are not many free tools for that, so you can consider the trials and probably use the products somewhere in the office conditions.

In your editors, install:
- Python: Programming, both 2 and 3
  - Flask _We bage library descibed in A.I. book, ask __GTP4All__ for reference_
  - PyTorch _Artificial Intelligence Library_
    - It guides you to things like openCV, ask ChapGPT additional tools.
  - Numpy _Advanced Mathematics Library_
  - Mdmath _Mathematics Library_
  - Mistune _Mathematics Library_
  - This is science programming language
- Julia
  - Look at the videos at it's web page and documentation
  - Download the single PDF book of the documentation
  - This is mathematical programming language
- Google Go "GoLang"
  - This is Google's real-time programming language, replacing C
- You can use classical web editors
  - You can try Emacs, Vi, Vim for insane experience
  - There are a few graphical GUI editors (WYSIWYG linux _your desktop_), where you search by your interface: KDE, Gnome etc., where each is available for each linux like Ubuntu, Mint (my favourite) etc.
- You don't need Linux for everything, for example on Windows you have ChatGPT Desktop, VsCode, and the Programming Languages in Native Interface; while I suggest a Linux Box for all the tools. You get some advantage from using Linux. KDE is the more functional, Gnome is very beautiful, and there are some others for different purposes, like having 3D effects on Desktop Environment.

For Documentation, install Zeal.

## Python: PIP Installer

Make sure the "pip" command works at terminal (you see one in VSCode at bottom of the window or View->Terminal).

Each time it complains about "missing library", such as "ModuleNotFoundError: No module named '<module_name>'" in the same terminal when you try to run your program, your first step is to write "pip install <module_name> in the same terminal.

> Once you download a code file for an AI, create one with ChatGPT or access one from my code base, it needs to be in VSCode, where you can open it and see in nice format, where keywords and content is colored by syntactic meaning.
 - You have some tools:
   - You need to make sure Cascade or Continue is installed, from "Extensions" pane, which you can open from left.
   - You can install Intellisense for AI awareness of code.
   - Once you see errors, you can click on chat icon related to the error, and ask an AI.
   - With attachment sign "@", when you talk to AI, or attachment button "@", you can add your code files and context to discuss and find errors; some chatbots are code-aware if you enter you message with "Ctrl-Enter", where they have this hint like __"Ctrl</@codebase"__ msg at __"</ Enter"__ button.

## For Accessibility

- Move Application for LM Studio to /home/Applications, create this folder if you need to.
- Add Favorites to panel of file explorer:
  - GPT4All bin folder, where you can start it
  - Applications folder to start LM Studio
  - Gpt4All model folder, where you can copy models downloaded from Hugging Face
  - LM Studio model folder if you want
  - You can download to Jan at it's connection to Hugging Face and model sources
  - Spireason Databases
- Other programs you can start from programs menu

You should now have complete access.

## Training for an AI
Other words: fine-tuning, optimizing, fitting, training; prepared by collecting the documentation and generators and cleaning and normalizing them to be in a standard format of AI input, or otherwise synchronized (AI is intelligent like you, so the "standard format" might not be precisely described, but also involves some common sense and allowance of creative approach, except if it's a variable type convention, which is interpreted by Python not by AI - Python is the strong back bone which keeps some standard formats in your otherwise free thought and expression so that you keep some sanity in this free world).

Selection of Tools:
- You can do this in _Programming Environment_ (IDE) such as VSCode (default and preferred here as it's relatively free, the basic functions are free to start) and Windsurf.
- You can do this in _Notebook_, such as Jupyter Notebook for Python, Julia and other involved languages. Go is not so dynamic, so perhaps you don't want to do it there.
- You can also do this in a _Lab_, such as Google CoLab: this involves Jupyter Notebook, but also all the devices and technologies you are going to use.

> In each case, while you are doing this for free, you have to find small and cheap models of AI's along with quite small models to embed the documentation - this one also is going to spend time at every query of yours, as it normally won't go without getting an embedding of what you said, to compare this with the document embeddings and write related contexts and content in multidimensional space position analysis methodology. With embeddings, you get 2-3 existing materials, "snippets", to be attached automatically to each question; you can configure the exact quantities, but in normal speed and effort, including resources, you won't get much more: theoretically, you can create questions it's going to answer several days, and give it different sets of docs along with the question, and ask it to generalize it's multiple answers and consider each point, rereading now relevant parts - with some efforts, you can get it to do further research; for example scan your documents, write summary for each, and then write a specification based on summaries, how to select documents to ask and answer questions.
- As an end user, you would preferrably be KISS developer: this means, you don't want to write much code, but you try to understand, what library headers are doing - for example, calculations with big numbers - and explain your Cascade or other Code Assistant, what you want to do with them then.

## Setup of Environment

_VSCode_, _Windsurf_ or an __IDE__ in general:
- Download the __IDE__, such as _VSCode_.
- Go to _Extensions_ from the left side button bar or menu, where normal search dialog opens.
- Seach for Python, Cascade, Code Assistants and install a selection of few; also perhaps IntelliCode.
- Create your own project by creating Workspace (where you work and where your projects are, it's rather kept open when you close and open the projects); and to create a project, you create one folder and select "File -> Add Folder to Workspace"; then, each time you open the VSCode, you can continue with this project. Inside project you create many modules, such as the code files to train your AI or download it's data; when you get more advanced, you can connect them with Common UI and a central system or architecture, which is going to integrate and unite your _Programs_ into a more common _Application_, which you could sell or distribute to more people.
  - Once this is done, go to "Source Control" from left button pane and add it to Repository: each time you have made a change to your project, you submit it here; this is going to keep track of each version, back-up your code, integrate with teamwork of others and also help you if you mess it up and break everything, or find an aggressive AI who makes many automatic contributions in delusional method, such as replacing your structure with something more logical.
- Instead of creating your own project, you can open "Source Control" from left button bar, and do checkout, which sounds like "Co" - enter my GitHub repository link, when asked what to check out, and it creates my whole folder tree; you can add documents and change them, and _commit_ - I will look at your commitment and decide, whether to put it to main branch, open your own branch where you can continue or finish your work, or do some changes before accepting; I might also reject irrelevant or biased content. In case you are rejected and feel right, you can clone the project and allow others to use your developments from your own GitHub repository.

## Executive Training
Assuming you use VSCode, here is the task to actually execute the AI training. You might use CoLab or Jupyter Notebook instead, which are more user friendly, but less advanced for structured code in many files (very good for one specific task with also taking notes and creating a mnemonic to be used later or by others, such as actual manual or documentation paper).

Character: You describe an AI, in English, it's character (including role, such as "_you are on a ship at Atlantic_"), and some additional features or conditions.

Document Collections: you give it documents, and it will be aware of them using it's existing knowledge base. This is rather Awareness.

Fine-tuning: this is like meditating or contemplating on a topic for an AI: it will be deeply Conscious in it's own terms. This basically means that by a matrix, it rather creates space of all the possible connections, rather than searching by index and reading in parts - this is kind of holistic presence in signle set of transformation matrices perhaps, able to create some curvature in space using activation functions and tensors, which are rather objects now responding to different tensions. This is very different from index search and originally, an AI model has a wide amount of data in this method, and is using this to understand your documents.

Create Accounts:
- Hugging Face
- Kaggle

There you see:
- __Models__: _AI brains_ you can download
- __Knowledge Bases__: called _Datasets_, they are dictionaries, image collections with descriptions (labels, in most mathematical form), collections and encyclopedias for an AI to automatically study and reference.

Install ChatGPT Desktop for Windows or Linux.

- Ask it to become your Assistant to download a decent AI model from Hugging Face or Kaggle, download some knowledge bases perhaps if your model does not know them, and train yout model.

Ask specifically, how to use _context awareness_ and _document embedding_ to automatically attach related documents as context: the model can have, for example, one mode for Q&A input, and other mode for Q&A input with context.

Programming the context:
- Imagine you have table of prices, products and qualities called SimpleList
- Program sets of Q&A&D entries in Python, such as
  - Q: "Is this product good?"
  - A: "Good" if quality > 0.5 else "Bad"
  - D: "Document with Id: " + id + "."

### _Programming with ChatAI, VSCode and Python_

You have to remember that you are using _libraries_, which are the _modules of additional functionality_ in Python. Sometimes, GPT does not note you about the "import" statement, where you search web, ask ChatGPT or use the automatic import button in your editor to add the proper line.

Use VSCode:
- When online, use CoPilot or some online tool if your computer is slow.
- When offline, use Continue, the Open Source AI Coding Assistant
  - download models such as CodeLlama 7b and CodeLlama 13b

Windsurf mighght have better Context Awareness and ability to change code everywhere, but it's not free. VSCode is free and quality software; on Windows, you might be interested in Microsoft Visual Studio Express, which often gives some unlimited access to restricted Visual Environment for Coding; for Linux you might try Mono or other _clones_ of this Environment (for _classical coding_, if you are interested in more classical programming, you might try also "_Free Pascal Compiler_" and "_Free Pascal IDE_").

_Programming Process_:
- Ask Continue about specific things in code, implementation; ask it to follow a task.
  - For online use, you can install CoPilot as well, using Continue rather when offline.
- Ask ChatGPT things, which need more contemplation and deeper understanding, where it's much more intelligent and creative, but cannot see your files so easily, while online.
  - Use bing.com to access CoPilot, and chatgpt.com to access chatgpt web interface.

You need to ask, in context of your program, which python files and where to put, and what code to enter. You try to run the programs, and if there are errors instead of successful run, you copy-paste the errors back from the _terminal_ or _console_ of your execution, for example in VSCode there are "Terminal" and "Debug Console".

In VSCode, install Python, Julia and Google Go environments. You can try to create an AI in each of them. You already got browsers.

You can program the following aspects:
1. Fine-tune one of the Hugging Face Models (Brains) using local or public Knowledge Base (Dataset). Both can be cached: you copy-pase, from ChatGPT, the model and knowledge base download code, or it will generate one to use you own knowledge base.
   - It generally, very much, wants to use the Q&A format.
2. Generate code to make the model to answer questions.
3. Export the model into gguf.
4. Talk to it in GPT programs, such as Jan, GPT4All or LM Studio.

If you want to put it online, you need Flask: create app.py in python, add a function with web address target for Flask, and the function needs to parse html, css, png and other web media with your attachments and downloadable content. It will understand each material given the url, as a web content to add mime tags and handle the POST and GET queries: user requests, such as requesting a web page or a document from your dynamic database, or supporting a link with a specific configuration.
- Use HTML, Javascript and CSS references from W3C to create web interface.
- Use TkInter, Qt or other UI Library, which are primarly for Linux, but you can port to Windows.
- Use Matplotlib for mathematical visualization.

Putting your model online:
- In Flask, create webpage of your files, databases etc.
- Create a server to serve your bot online, so that your website can acces it.
- On website, you need some HTML+JS+CSS solution to display the bot visually.

## Using your bank account

To have AI training hardware, where you can train and run your models:
- Buy one computer from HP omen family, where you analyze your needs, such as model and whether it's only for you or to serve to many people, in which case the same machine is for smaller models.

To have the software:
- Buy VSCode and some of it's code assistants, such as CoPilot or Tabnine, in full versions.
- Pay for CoLab full account, and for Hugging Face services.
- Use Clouds to train (fine-tune) larger AI's, which can get to thousands of euros, days, or even weeks.

### Where and how you can use my data to set up

Using Laegna Databases:
- Some AI systems are happy with Notion.so link.
- You can download Dataset from Hugging Face and clean it to have only one file type (not each pdf, md, html like many files there) or several supported file types; GPT4All supports them, but is slower.
- You can also download the Project from GitHub either as zip or by cloning it.
  - As zip, you might download it as Document Folder for your AI
  - As Repo Clone, you can click "Source Control" in VSCode, create GitHub account and download or update it with one click; also you can add your own files and resolve conflicts, if two people changed the same file.
  - __LaeArve/Books/Reflector/MDMicrobot/__ - download this folder separately, or add it as separate collection to GPT4All; when you want it to answer faster, you have only this one active.
    - I will keep it very small: perhaps in future, there is smaller version with only 5 infinity theorems with background and 1 introduction theorem (well quite much with all the related definitions), and bigger version with 9 infinity theorems and all, perhaps 3, 6 or 9 of tautologies for Spireason (the Alchemy Stone: theorems about longer life and vitality, which you can apply to your programs for example, and which should keep you from falling into pure philosophy).
- Download my Hugging Face Database and give some folders to GPT4All to make it understand some of the Laegna.
  - LaegnaWiki is not Wiki, but somehow you can convert it to Wiki with Notion.so if you don't like this folder name otherwise. It contains rather titles and content. Also there are all original Laegna and Spireason texts in orgiginal format of OpenOffice, also all conversions; in Buddhism there are some free open books of Buddhism for it to gather some background.

Using LM Studio as a server:
- Select that you are "Developer" and go to developer view: This is the server and you could use it to be physically at your web server (AI-capable powerful computer at your home, office or special position); initially you mean just a program in your computer to provide standard API to other programs by server.
  - You can add chatbots, for example you can serve the smollm model you have: other chat programs, now, have access to the bot and they can simply talk, not work with the model names, which means you can find simple chatbots and robots dels, who work only with their own files otherwise. You can "load" several bots for them to be served and chat online or in your computer, and "eject" to unload them.
    - You can start any chatbot capable for this service format and in that, enter url to connect the bot.
  - You can add embedding models, which are similar to bots
    - Embedding model takes text input and generates it's position in mental map of texts.
    - Like GPT4All with it's Document collections
      - Write a Python script, which got all the documents one after another, reads each file and feeds it to embedder; it gets back some cryptic, encoded thing, which is an embedding.
      - When user is talking, each time you have to say something, you embed the chat, last few pages or last question of yours, and iterate over your documents to check the embedding distance with your own loss function - are the numbers similar.
      - Your bot, for example, gets the files or parts of it, depending on what you embed, as context of each question - for example, have a powerful bot in LM Studio, for each document ask it for a summary automatically, and then with simple bot feed it the summaries not whole files. It would know your general background if you ask, such as that you are programming in Python.

Training and Embedding is very expensive, so you can:
- Select a Git version or version of data or generators, as we get ready with some.
  - Train your bot on Laegna data.
  - Generate embeddings for Laegna pages and views.
  - Upload this with embedder or model information etc., to Hugging Face or Kaggle
  - Incorporate the links at our GitHub, where it could be used.

- We need embeddings to have the Documentation and Generators (with their output being static if you have one specific random seed) searchable, accessible to bots etc. More complex embedders, which are DL models themselves, take more time to create embeddings, but for us would be more worth for large bots.
- We need trained bots to introduce Laegna to people, where they can use embeddings to access Document Base, Chat Context and wherever you do embeddings - those let the bot to mentally map the external or internal data.

Test the bots (brains):
- Are they intelligent.
- Are they fast or slow?
  - If fast, try bigger models
  - If slow, try smaller models with options for smaller number types etc.

You can also train the same model based on Laegna content, and upload the result - for example, base model in Hugging Face and where the licences support it and fit, the gguf file here to be used in all 3 given chatbots, and with some effort in VSCode and Windsurf.

### Optional Software

Some of the programs I have installed, which might inspire you.

__Freemat__
- Mathematics
- For test: start it and enter "1+5", then line feed (enter).

__Gimp__
- Image Processing

__GNU Octave__
- Mathematics
- Also ask something like "6+4" from it.

__Julia Documentation__
- You can install the web link into Applications

__Python AI Toolbox__
- Graphical Application to Python to Design AI

__PyPlane__
- Tensor fields
- Vague association with AI

__SWI-Prolog__ or other _Prolog_
- Logical analysis of facts and it's relations

__Isabelle__, __Coq__:
- Advanced use
- Theorem proving

__exMaxima__:
- Visual Mathematics Formulas

__xCas__:
- Calculator-like interface to Math

__xCos__:
- Visual Diagrams and Circuits

__Scilab__:
- Some science expressions, I don't use it but it could be useful as calculator, sometimes.

__Celestia__:
- Space maps, I am interested in stars
- Usually you can download Chemical Element Tables and basic views to physics, chemistry etc. for things like chemicals. You can, in linux distributions, view each science as separate collection, where you can see long listings of programs - separate programs, and packages, which collect a set of programs to do this.
  - This functionality is not always the default and you might like other methods more.

__Genius Math Tool__

__KAlgebra__: for _K_: for Gnome or other Linux interfaces, there might be better choices.

__KLatexFormula__: you can enter Advanced Text in Latex and view the result.

__Mathomatic__: Terminal mathematics program: enter "2+5" as well.

__R Commander__:
- Statistical Programming Interface.

__Visual Studio Code__:
- Programming Environment VSCode

__Visual Studio Code - Insiders__:
- Almost equal alternative
- I don't know, why is this

__Standard Deviance Calculator__:
- Very simple calculator using list of numbers

__Sublime Text Editor__:
- While this will be "UNREGISTERED", it's still useful program with full functionality; with registering you get some add-ons or something.

# In folders, download the Books (or free alternatives should anything happen to book); in my case the folder is named "Library4All" to nocide I want to give it to "GPT4All", in some cases the only library:

It's optional to use each library - there is list in panel and you can switch them on and off any time, so that your bot might see those books or not, see other things or not, and in any combination. This is absolutely dynamic and affects it's speed and attention - more things, less attention on detail or perhaps the wholes.

I had long list of files, but the problem - it would do embeddings for weeks and not reliably add the folder each time even if it gets broken.

__AI_FreeBook.pdf__: _Explorations in Artificial
Intelligence and Machine
Learning_ CRC Press Taylor & Francis Group

__AI-with-Python.pdf__ _Artificial Intelligence with Python_ Your complete guide to building intelligent apps using
Python 3.x and TensorFlow 2

__Bardo.pdf__: _BARDO_
INTERVAL OF POSSIBILITY
KHENPO KARTHAR RINPOCHE’S
Commentary on Aspiration for the Bardo
by Chökyi Wangchuk
translated by Lama Yeshe Gyamtso

__Deep.Learning.for.Coders.with.fastai.and.PyTorch.Howard.Gugger.OReilly.9781492045526.EBooksWorld.ir.pdf__ _Praise for Deep Learning for Coders
with fastai and PyTorch_ Jeremy Howard &
Sylvain Gugger
Foreword by Soumith Chintala

__deeplearningbook.pdf__ Deep Learning
Ian Goodfellow
Yoshua Bengio
Aaron Courville

__Deep learning: Technical introduction.pdf__:
_Deep learning:
Technical introduction_
Thomas Epelbaum

__Deep-Learning-with-PyTorch.pdf__: _Deep Learning
with PyTorch_
ELI STEVENS, LUCA ANTIGA,
AND THOMAS VIEHMANN
FOREWORD BY SOUMITH CHINTALA

__Dive into Deep Learning.pdf__: _Dive into Deep Learning_
Release 0.17.6
Aston Zhang, Zachary C. Lipton, Mu Li, and Alexander J. Smola

__dokumen.pub_essential-math-for-ai-next-level-mathematics-for-efficient-and-successful-ai-systems-1nbsped-1098107632-9781098107635.pdf__ O'REILLY' _Essential Math for AI_

__Gradient Expectations.pdf__:
_Gradient Expectations_
Structure, Origins, and Synthesis of Predictive Neural Networks

__Handbook_of_Mathematical_and_Digital_Engineering_F.pdf__: _Handbook of Mathematical and
Digital Engineering Foundations
for Artificial Intelligence_
CRC Press
Taylor & Francis Group

__infinity.pdf__: https://www.researchgate.net/publication/346967755 The TRUE Mathematics of Inﬁnity for Scientists and Engineers Leslie Green
- Altough this applies under certain conditions

__kybalion.pdf__: _The Kybalion_ The Three Initiates

__machine-learning-absolute-beginners-introduction-2nd.pdf__: Machine Learning For Absolute
Beginners
Oliver Theobald

__Machine Learning - A Probabilistic Perspective.pdf__: _Machine Learning
A Probabilistic Perspective_
Kevin P. Murphy

__Machine Learning for Hackers - Case Studies and Algorithms to Get You Started 2012.pdf__: O'REILLY' _Machine Learning for Hackers_

__Mathematical Introduction to Deep Learning: Methods, Implementations, and Theory.pdf__: _Mathematical
Introduction to
Deep Learning:
Methods,
Implementations,
and Theory_
Arnulf Jentzen
Benno Kuckuck
Philippe von Wurstemberger

__Mathematical_Introduction_to_Logic_Herbe.pdf__: _A Mathematical
Introduction to Logic_ Second Edition
Herbert B. Enderton
University of California, Los Angeles

__NothingInfinite_Aug2023.pdf__: Nothing Infinite: A Summary of Forever Finite
Kip K. Sewell
August 2023

__numpy-ref.pdf__ _NumPy Reference
Release_ __1.23.0__
Written by the NumPy community

__numpy-user.pdf__: _NumPy User Guide_
Release 1.23.0
Written by the NumPy community

__O.Reilly.-.Natural.Language.Processing.with.Python.pdf__: O'REILLY' _Natural Language Processing with Python_

__Survey_AI.pdf__: _The Mathematics of Artiﬁcial Intelligence_ Gitta Kutyniok

__sympy.pdf__: _SymPy Documentation_
__Release 1.4__
SymPy Development Team
April 10, 2019

__Theory of Deep Learning.pdf__: _THEORY OF DEEP
LEARNING_ CONTRIBUTORS: RAMAN ARORA, SANJEEV ARORA, JOAN BRUNA, NADAV COHEN, RONG
GE, SURIYA GUNASEKAR, CHI JIN, JASON LEE, TENGYU MA, BEHNAM NEYSHABUR, ZHAO
SONG,...

__Y_2020_Barukciczeroandinfinity.pdf__: _Zero and inﬁnity. Mathematics without frontiers_ Ilija Barukčić
GIM Wittmund (Ost-Fiesland; Lower Saxony; Germany)

_Zero books are included as they are basically the only books on quantitative infinity I found_

__programming-pytorch-for-deep-learning-creating-and-deploying-deep-learning-applications.pdf__: O'REILLY' _Programming PyTorch for Deep Learning_

_Creating and Deploying Deep Learning Applications_

Ian Pointer

__Deep Learning with Python.pdf__: _Deep Learning with Python_ SECOND EDITION
FRANÇOIS CHOLLET - MANNING
_SHELTER ISLAND_

__model_theory_seams.pdf__: _AN INTRODUCTION TO MODEL THEORY_ by Pablo Cubides Kovacsics

# Additional books

Some repeat: you can read them yourself.

## Artificial Intelligence with Python
Second Edition

Your complete guide to building intelligent apps using
__Python 3.x__ and __TensorFlow 2__

- __You need to download additional materials from it's Webpage__ and GitHub. Tensorflow versions easily break backwards compability, but you can get some idea.

sympy-docs-html-1.12.zip

sympy-docs-pdf-1.12.pdf

# D2L: __Dive Into Deep Learning__

_Dive into Deep Learning_

__Release 0.17.6__

Aston Zhang, Zachary C. Lipton, Mu Li, and Alexander J. Smola

- __Download materials d2l-en from it's website__

# Deep Learning for Coders with fastai & PyTorch
O'REILLY': _AI Applications Without a PhD_

powered by: jupyter

# Deep learning:
_Technical introduction_

Thomas Epelbaum

# Deep Learning with PyTorch

ELI STEVENS, LUCA ANTIGA,
AND THOMAS VIEHMANN
FOREWORD BY SOUMITH CHINTALA

# Mathematical Introduction to Deep Learning: Methods, Implementations, and Theory

Arnulf Jentzen
Benno Kuckuck
Philippe von Wurstemberger
