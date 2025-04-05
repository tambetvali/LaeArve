## The AI task

The next task:

My source tree of files on hard drive is mapped to target drive at web.
- Source root folder is the same root folder as usual; a folder 1 is given.
- Target root folder is mapped on the source tree; a folder 2 is given.
- Anything above, from the root, but excluding the target root folder (it will not reflect inside itself, and it's physically inside the root), is mapped to _reflection folder_, where folder 3 is given (reflector).

The source: physical code tree of mine, where code files are the root.
The target: webpage, where another folder is the source, but it reflects code folders in position of folder 3 (in source coordinates), where code folders start from root, but it start itself from folder 2: the reflected.

Terms:
- Root folder: the actual file tree
- Reflected folder: the web-visible file tree
- Reflection folder: where it mirrors the actual file tre inside reflected folder, excluding the reflected folder and anything above.

Variables: link is link, source is sourcefolder, web url (target) is webaddress.

I need the following mapper:
- Hard drive url is given to the mapper
- It uses MongoDB to store the file/folder hashes/timestamps together with the original and mapped tree and Anytree for the connections between nodes.
- It uses the functions you gave before if it needs them to convert between mappings, but it implements stronger conversion with real files.
- MongoDB database will cache mainly the chapter trees of markdown files.
- Markdown files would be parsed, and if in no-empty-blocks-in-between, under title, is block "__name:__ <filenamemapping>" the block is mapped to file name, or if there is "a target" or block stating with "@ __self:__ <link target>" will be mapped as specific position, which can be identified in this file with link, and "a target" means "#" link is also registered as a sublink, equivalent to "/" piece in our server and it's registration, it should also follow "/" links to "#" targets. Chapter tree of Markdown file, preferrably using Mistune or simpler MD library supporting limited functions like chapter gathering, or even regexp would do: simpler impl is better.
- With "@@" at beginning of block and followed by "__<name>:__", space and a link, where <name> is the last part of the link, it would remove the block and create an accessor, but here we only create accessor as we parse them more, and we store to attributes that this name is parsed.
- Files with name+extension, together with folder with name (extension is not considered), where extension is last part of filename, or last part followed by ".htm" or ".html", where we show preview and extension should be part before html, and "preview" set to true. Files with the same name are under common group, and melted.
- Under chapter titles can be "__target:__" specifiers, where the chapter will remain here, but be merged with targets.
- If the part is requested, it could be under any node: a chapter, a file, or an equal position from folder to inside file, or file to inside folder. The tree must melt all this, be able to list the positions, and give the chapter list.
- It will have preprocessors, hook support, where the hooks are between requests and between initialization of the tree (two instances of same class with different calls). It would have a hook to class, which clarifies, whether it's chapter, or named or unnamed block or chapter, and whether it's target or a link.
- Backlinks: block like "@@ <link with text>" would create a subchapter with this text.
- Some chapters and tree nodes could be made "subdocuments", in which case in case of more than 6 levels of titles, the content would be broken at there.

Finally, the client: can use Extended Anytree Objects (like SourceNode(Anytree Node) and TargetNode(Anytree Node), where source and target can share a common parent or be the same class) for Source or Target view, and identify, with our class, the respective object to access a single Node.

The Python file would contain code for testing, and surrounding Markdown explanation text is with each markdown line preceded by "# " and containing Markdown: the Markdown display format would render this into Markdown with python code blocks to be connected to the same file. Each class, function etc. is in the same file.

Main interest: implement a way to access the file tree items properly, reach from original to target url and vice versa and keep an object for each node, such as chapter or folder item. Use Anytree functions, such as list etc., and primary view is the weburl, while the local view is used to find sources and attachments etc.