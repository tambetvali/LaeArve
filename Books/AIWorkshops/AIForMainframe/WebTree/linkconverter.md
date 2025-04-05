# Task to CoPilot

Result is in the Py file with same name as this file.

How to code this thing:

My source tree of files on hard drive is mapped to target drive at web.
- Source root folder is the same root folder as usual; a folder 1 is given.
- Target root folder is mapped on the source tree; a folder 2 is given.
- Anything above, from the root, but excluding the target root folder (it will not reflect inside itself, and it's physically inside the root), is mapped to _reflection folder_, where folder 3 is given (reflector).

I need two functions, which can convert links in both directions:
- Given the source path and file, they convert to target
- Given the target, they convert to source
- If source contains http://, it will not be converted, so in the source text links can exist, which are using the web format.

The source: physical code tree of mine, where code files are the root.
The target: webpage, where another folder is the source, but it reflects code folders in position of folder 3 (in source coordinates), where code folders start from root, but it start itself from folder 2: the reflected.

Terms:
- Root folder: the actual file tree
- Reflected folder: the web-visible file tree
- Reflection folder: where it mirrors the actual file tre inside reflected folder, excluding the reflected folder and anything above.

Given strings, the functions must do:
- For relative links, starting from letters for example, no conversion is done: they are properly relative to this content, and might refer to converted format as well as to local format (return the input in both directions).
- For root-relative links, starting from "/", the conversion is done: root, at server and client is different, while the relative part either exists or not, but it's otherwise indifferent.
- For web links starting with "http://" they are already proper, outside-visible links and not affected by conversion (return the input in both directions).

The Python file would contain code for testing, and surrounding Markdown explanation text is with each markdown line preceded by "# " and containing Markdown: the Markdown display format would render this into Markdown with python code blocks to be connected to the same file. Each class, function etc. is in the same file.

## Followup task

__Notice:__ it might give other variable names, if you don't like them, you have to clarify. You can also give this all as one task.

Instead of Link, Folder1 and Folder2: - Each is a link, and keep the format: if "/" is added or not added to the end, keep the convention. Test would show that when it's converted back, it's digitwise the same link. - Link is the "link" in input - Source folder: "sourcefolder" - Target folder: "webaddress" This way it makes sense, what it's doing.