# Task for Flask service

I want another class, which would do the following:
- It receives the link
- It creates a group of files in flask side of the url, which map together: files with same name and different extension, folders with same name, and the ones backlinking with @@ blocks are nested inside as similar chunks (their nesting links, when approached, are given with each part). If backlinking target exists in one Md file, and this or existing nodes are backlinked, the backlinker page will be nested in this one, currenly only from local server.
- It builds on top of existing structure in your generated class

You need to build Flask interface for this conversion:
- It has interface for parsers of .py, .md and other non-html files; parsers can register, they get the source file and provide a version with ".htm" or ".html" attached, where I use them for HTML and DHTML: this can be given, is it HTML or DHTML. It will generate Markdown version of this file, which is processed like other Markdown files: to refer to folders (you need to hook into your previous class: do you need to change that, if so, write a task for this only)
- The flask interface uses the folder tree you built, but it "melts" the folders.
- Flask output, not correlating to original input types, can be attached input types by plugins: markdown, html, dhtml and json view, and for specific files like py and sh, their view and source, where the view has additional ".htm" suffic or optionally, ".html" suffix (not default).
  - Melted folder: if there is folder "test", md file "test.md" and py file "test.py", the py will be preprocessed into Md, and the folder test: each file is a chapter, will be processed as well. If the chapters come in same order in some possible part, they are merged together: if they cannot be merged this way, other means are used. Folder content: markdown files go as chapters, subfolders go as chapters containing subchapters, and the same file parser is used with different input, which is used to show custom files. There can be hook to set priorities of each: in chapter lists, you put the priority ones first. There is also a hook for garbage collector, which would search with too many nested chapters or continuous blocks, and stop the processing, returning a "Continue" link for each: if you "Continue" the whole text, using the link not in the end of it's last chapter, but before the first, you would get it all with garbage collector removing only big numbers and leaving "pages".

Solve the architecture and give a list of tasks you would implement subsequently. I would add some to each.

### My correction

Flask interface:
- Use a markdown code in each _main-level_ # comment: but not inside heading of a class or function, but before that. Otherwise, the standard api-defining """ blocks.
- This will be rendered: first-level "#" blocks into markdown, but the "#" must start from first letter, where comments into classes can be Markdown if we get such python highlighter, but they cannot be outside code blocks.

## Architecture Summary and Subsequent Tasks

CoPilot-generated list of subsequent tasks.

1. **Create the Melted Tree and Flask Interface:**
   - **Task 1:** Design the `MeltedTreeFlaskInterface` class that wraps the `FileTreeMapper`.
   - **Task 2:** Implement the method that “melts” or groups nodes with the same base name.
     - *Subtask:* Define a clear merging strategy for files, folders, and backlinking items (using the @@ blocks).

2. **Implement a Plugin System for File Parsers:**
   - **Task 3:** Define an abstract interface (or a simple registry) for parser plugins.
     - *Subtask:* Create sample plugin functions for converting `.py`, `.sh`, and other file types to Markdown/HTML.
   - **Task 4:** Enable these parsers to register themselves with the `MeltedTreeFlaskInterface` so that when a file is requested, the proper transformation is applied.

3. **Flask Routes and Views:**
   - **Task 5:** Set up Flask routes that receive a URL (or a link) and delegate the request to the melted interface, rendering the specified view type (HTML, DHTML, JSON, or raw source).
   - **Task 6:** Create templated views (or use API responses) that allow users to navigate the melted folder structure, read the processed file content, and view nested backlinked chapters.

4. **Prioritization and Garbage Collection Hooks:**
   - **Task 7:** Define hooks for reordering chapters or merging items when multiple content pieces (files/folders) occur with the same base name.
   - **Task 8:** Implement a hook (garbage collector) that detects excessive nesting or overly large chapter lists, then truncates the output and provides “Continue” links for on-demand loading of more content.

5. **Integration with the Existing FileTreeMapper:**
   - **Task 9:** Enhance or extend the existing file tree mapper to support additional metadata that aids in merging (such as storing backlink references or parsing @@ blocks).
   - **Task 10:** Write tests that cover:
     - The “melting” logic (merging files with the same base name, handling nested backlinks, etc.).
     - The parser plugin system.
     - The Flask routes for each view type.

6. **Documentation and Configuration:**
   - **Task 11:** Document the expected folder conventions, merging behavior, parser registration, and hook usage.
   - **Task 12:** Create configuration options (via environment variables or a config file) for adjusting priorities, view types, and garbage collection thresholds.

7. **Optional Enhancements:**
   - **Task 13:** Allow for dynamic reloading in the Flask application if the file tree changes.
   - **Task 14:** Build a simple administration page to manage plugins and monitor the processing (e.g., list cached metadata from MongoDB).
   - **Task 15:** Evaluate and improve performance for very large file trees or deep nesting.
