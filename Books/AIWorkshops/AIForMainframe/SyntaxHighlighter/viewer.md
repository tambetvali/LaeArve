# Write this file viewer:

For your disappointment, it could not recognize the whole task, so I incorporate the pieces instead.

## Task

- Flask page allows to open Md files with extension directly, and each file directly with it's extension, but the browser would render Md to HTML with also folder content on side and other files into Source Views, where it adds virtual ".html" at the end
- In source view there is also download link

- Pygments hook is used to detect start and end positions of each comment in the file.
- API headers in """ and """ comments, standard to Python, get highlighted the function names and other keywords, as in normal syntax highlighting.

- Comment blocks, where positions are known now: hook should be used to understand, where the content starts and ends; for multiline comments, they start from beginning of line if first line starts from there. All those are rendered to HTML.

- Inside code blocks, comment rendering is detected as well, using the information already available (where you detected all the blocks), or new one if you detected specifically one type of blocks. They are rendered with _Markdown syntax highlighting_ using Pygments, where they are applied more highlighting.

- In this Flask server, one could browser files in current folder:
  - Md files: render to HTML, but have "Source View" available, and "Web view" in the "Source view", also there is "Download".
  - Other files, which are recognized by Pygments: have "Source view" by default, but allow "Download".
- For Web and Source view, there will be side panel to navigate the subfolders.

## Addon

Have the docs in code so that it could be seen by itself:
- Top level MD comments and chapters
- Inside comments use bold and italic or links in Markdown way.
- There are python help strings.
- That way, it could be also tested!
