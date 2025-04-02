# A processor

Each node, when it's loaded, eventually gets a processor:
- The Markdown parsing is initiated
- It will be associated with some chapter:
  - It's the attachment
  - It's the subchapter
  - It's the text to be added to chapter text
  - It's containing all these elements

Before getting a processor:
- The node accepts the commands to add other nodes to it's parse tree; for example it does not know yet about a chapter, but it accepts adding element in beginning of the chapter.
  - So it's in kind of lazy mode, where properties can be already given values, but the values concretize once it's loaded.

So it has two attributes:
- "src" is the Markdown source, where important points are identified:
  - Chapters, including their end point, can be selected; added subnodes will be registered to appear there.
  - Code blocks and inline pieces of code are also identified in Md and can be replaced.
  - Also, the places where exterior resources can be loaded, for example a place marked for backlinking: other pages can add content there, and it's also marked so that it can be replaced.
- "blocks" is the BlockList. Here, each block can be associated metadata: as it's not converted back, the metadata would be permanent for each page load, where it's destroyed once the page loading is finished and page is fed to the user, or when it's dynamic process is finished.
- When adding content to blocks, they can be "replaced", content can be "added to end" or "added to beginning" of this block. It has to find this place in Markdown and HTML: those two are changed in parallel.
  - If content is set "dynamic" or "html-only", Markdown file is not affected. For example, one can add an animation only to DHTML.

Processor, then:
  - Has a preparation mode, where it does not know it's exact content, but defers the calls.
  - Has a contentInitialization mode, where it can preprocess each file or folder.
  - Has a block mode, where it's made of blocks, and Markdown is associated, where it creates compies of changes known to Markdown (runs Markdown commands).
    - Data can be added to blocks: but original Markdown content must not be touched, even deleting just adds "delete" property and the block structure is static, one can remember positions for the load.

When this load is done, it's still not added to HTML:
  - It gets part of HTML processing, being able to replace the processor etc. It has separate rendered rest from other files, so each file controls their HTML template.
    - Optional DHTML is generated
    - Optional HTML is generated
  - Json, now, is generated based on blocklist with all metadata.
  - Modified Markdown is generated.

Site will be rendered once everything is collected.
  - It can generate each version of the static page at once and cache them.
