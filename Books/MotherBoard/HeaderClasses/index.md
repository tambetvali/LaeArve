# Header Classes

This is kind of "API", but rather a general structure with some rudimental level of implementation, for the filesystem reader. From this, the structure can be built to have the proper file access and database structure.

We remap the folder structure, based on tree.md files - there are two of them around.

While we can iterate over file tree and map it to Python structure, we don't want to completely break this structure - rather, the filesystem-relative treemap is a thing we want to have later, for example to return the original address in filesystem, or a link to original file.

We are going to use this library:
- __Anytree__: create tree structures and map them to variables.

First we do this:
- Iterate over whole folder structure and create it from dictionaries, which maps the filesystem structure of our files.
- Assign, on Anytree, a node to each file.
  - Map the same structure.
  - Where you see tree.md files, for both files have the current node marked in special variable of tree container; "root" and "reflector". Those two will set the root parent to None, still using the "root" variable to locate it (it's the root of the list, marked None in Anytree). When you set the parent to none for root, subsequently all the files _above_ it are disconnected from it: use use the "reflector" variable to set the parent of filesystem root, which differs from mapped root folder (the one you see at URL, in the browser address bar): you cannot backlink it as it does not have an address, but you need to set the *parent*, equal to parent of reflector.
    - "header.md" in the root folder should set: it's "Name" to "Source", it's "Unite" attribute to Reflector, so that the content would be mixed. "Delay" should be set to "LoadTree", where the header is not processed before the tree has been loaded.

Now, the filesystem should be mapped into Anytree, which is a better database for tree structures, where we might need one or another:
- RenderTree.ContStyle would actually display the item tree of what you can write at the address bar.
- It can process _paths_ in format "folder/file", both to find nodes or to describe them.
- With cache added, it could search by name.
