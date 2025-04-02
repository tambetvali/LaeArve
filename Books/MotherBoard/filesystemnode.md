# Filesystem Node

Let's imagine we have the name "wildnature" for our page.

Then, you can have the following files:
- "wildnature" folder: this is where the structured files reside.
- "wildnature.md" file: this is where the document resides.
- "wildnature.py" file: this is the main code file
  - By having "`#§ run; main=MainClass; if='attr(\"view\", \"html\")'`" command in the comments in the beginning, the file is run if view=html and MainClass is used as an entry point. You must manage to have the function "`attr`".

For the script:
- The filesystem node is read as one unit, where the script melts them together.
- `wildnature.md` defines the chapter structure; the chapter structure is initially build based on the order of chapters there.
  - Chapter tag "_name_: name" gives it a file name, thus associating the file with continuation of that chapter or the script associated with the file, as generating output as it's content.
- `wildnature` Folder defines chapters and attachments, where images, sounds etc. are simply attached to it and script files without md files and folders, attached as well.
- `wildnature.py` is attached to the parent folder, and if it has `#§ run` it will be simply executed. We might want to process the imports so that the script could import from the current and it's own directory trivially.
  - If the script is visible, it creates a chapter "Script".
- When there are more mediums with the same name, the file can contain chapters like "Image", "Sound" etc. Separate files also easily open such page.
- If `md` file or Folder is not available: the script is considered an attachment, added to attachment list of the page and not linked automatically as a chapter.
  - `index.md`, `readme.md` or other name in the importance list will be applied as "index.html", and other md files in the folder are chapters of this file.
  - it's folder: it adds chapters directly under the title, creating a title-associated dataset.
  - files without folder or `md` are attachments for parent folders of folders, where they would otherwise be visible.
