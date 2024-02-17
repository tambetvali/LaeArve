# App.py
File: LaeArve/App.py

Let's define the app.py file:
- It has the root element, where everything starts
- It has the page element with following URL structure:
-- It can have class name in first part of url, http://127.0.0.1:5000/ClassName
--- the class needs to be declared as a page so that the user would not invoke internals
-- It has chapter structure following the class:
--- Parent chapters, each has document name (not title), such as doc/subdoc/subdoc
--- Currently open document, everything marked to belong there (it's chapters and subdocuments) have part "/in/", after which come the chapter and subdocument names, not titles. It still directly knows it's leaves, last-level links, which all have unique name inside the document, so it safely removes "/in/" part of the url, once another level is opened, and adds it's name *before* where /in/ was.

## Formats

### HTML

Everything scrolls, there are no absolutely positioned items or we get into complexities of code and implementation, which we won't do for design, for example maybe we have long menus.

Top: a bar, where there are buttons: DHTML (for human web), HTML (for AI, human print), Markdown (for AI, human print), Json (for AI database). Write: DHTML / HTML / Txt / Json - we have markdown, but let's write Txt as Markdown is a formatted case of it and Txt could be more easy to understand.

#### Dynamic HTML
view=dhtml

Here, changes of content are allowed. This is not very machine-readable, for example you might not know your exact position.

! DHTML Template. Use static templates wherever there is no dynamics - initially, just use the same templates, but in separate if and with separate format.

#### Static HTML

Machine readable and automatically browseable, for AI's which do not follow our standards, but surf the normal web and handle the HTML.

AI is not distracted by some HTML, like disabling a textbox, when "Other" is not chosen from the dropdown. We might add such feats later.

> Links have format easy to follow.

> Text is formatted by HTML and CSS, no magic. Simple parser should understand it.

! HTML Template. Each element is repeated.

### Markdown

Machine readable, autobrowseable, printable, and makes sense by format.

> Clicking on "Properties", page with Link menu and Properties appears, which come straight from static(!) HTML, but use simpler page template with the window divided into two: left and right; "Submit" and "Cancel" are the buttons - submit and back are their functions.

> Links have written links after the links themselves.

> No menus, but only content table and links after each chapter, also written out.

> No top, left and right panels and bars, only the content.

> Text, tables and chapters are easily formatted: I don't use if I cannot format.

### Json

Machine readable, autobrowseable, but makes sense only for computer.

> Links appear as objects with metadata, where each link can be added metadata; other formats ignore it completely. All links and labels can be iterated in one go, as they are flat list.

> Links have preview mode, where user will be able to set the properties without preview, based on their names, labels and metadata, without downloading anything; it might be expensive to download too much.

> Text, tables and chapters form an object tree.