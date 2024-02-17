# Pages (as in "Webpage")
File: LaeArve/LuiPages.py

The following is what we have inside a page. Each page has a top-level menu item.

## Documents, Chapters and Subdocuments

Let's have a list of Documents:
- Main Title - Document has H1, Chapters and Subdocuments have next levels of H
- Subtitle
- - Chapters and Subdocuments (Subdocuments do not have the first level title)
- - - Each has a button to open on separate page
- - - Contain list of Blocks: BlockLists; each chapter is a blocklist followed by subchapters.

Documents, chapters and subchapters are internally separated only by single variable.

In menu, first document appears; also the page title contains the name of the first document. Others are follow-ups (this is often my style) with first-level titles.

## Structural breaks

Structural breaks can be manipulated with properties.

The navigational breaks:
* Documents with Chapters break:
** After first two, three, four paragraphs, under every title there is the "read further" link, unless user configures it to full view or it's marked as worth longer display.
** After some subchapters, there is the content index for more subchapters, which open separately.
** First paragraphs and chapters can be marked important: the system tries to preserve them, but it does not show too complex structure at once, so it might break them.
* Many documents or first-level chapters break:
** They break into pages (1, 2, 3, 4, ...)

## Internal structure

Document is a list of Blocks.
Each Document is a Block.
Document is contained within class.
Blocks can be read automatically from Markdown files, in which case the Markdown view preserves them; othewise they are converted to HTML. Markdown files are easier to manage - each paragraph is a Block, empty line is a special Block called separator and not counted as a block.

## Representation

### DHTML

Document is contained in canvas.

### HTML

Document is contained in canvas.

### Markdown

Canvas exists, but it's practically empty, having perhaps a footer.

### Json

Canvas exists, but it does not create a Json object, rather it controls how all the objects are added - it has rather visual purpose or controller purpose, and Json does not need such controller.