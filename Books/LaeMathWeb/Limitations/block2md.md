# We keep only structured data in inside-cycle

The generator only stores it's data in json files: for md files themselves to be generated, we use simpler parser and remain with support to it: until the Mistune would support it, they have their own complexity/feature balance and I rather started to like what was initially a "workaround":

- We store the subblocks in json format, in which they go to the client.
- We scan for titles in md files, hoping they start with something like "#" and we also react to proper paragraph calls of code, when it's executed with the law sign. In our system this needs a law, to understand what we can execute: it's not automatic, and outside any automation we leave it like this.

## Limitation solution

We generate each Markdown page to Json only once:
- The final client output has only HTML renderer.
- The final Json output consists of this data, which cannot be converted back: instead, we use all the tags we apply, containing all the metadata and other elements, connected back to source. Very different kinds of Markdown pages could be generated based on this. _Who adds to content in this mode, does not know of limitations of Markdown, so if we need Markdown, it needs to be generated on this content_.
  - Mistune allows: create _template_, which generates Markdown.

We can add classes _under_ the produced object tree, and parse new Markdown back to the block content before it's rendered.

No level would render anything unless the client directly wants it, in which case it's unreturnable.

Solution to Markdown view:
- Without parsing, the links and backlinks are in normal link format.
- We can do simplistic parsing of titles and our own block types, where we leave Markdown intact, so in parsing mode they are referred back.
- The Spider would also know, what to do with them.
- Basically we need nested documents to show them one after other, but perhaps the subdocuments can be replaced by links: if we contain long materials rather locally, they are cut somewhere.
- We could use "@@@" linking, which simply and unconsciously includes that content of the link, indeed in Markdown.
- Finally, we can execute the paragraph marked code, where it can _decline_ it's execution: if None is returned, the code block is displayed. The Markdown can also contain some of the output and link. If code can not reproduce itself and cannot create reliable cache, it might not want to leave link: it leaves generator input instead or link to such, a page where you can generate such content.

__Appearance of Intent:__ this is actually _intentful_ to have the Markdown view actually closer to original Markdown, where it also generates a title tree, connects it to content positioning and also to Mistune; it could, given the tree up and down, detect whether it can contain the given content in 6 levels of titles: otherwise, it would make use of "subdocument" titles, which can be moved partially under separate link and page: in case enough subdocuments are found, in the HTML page the title levels won't render to anything but text, and so small level headers probably are. We have the Markdown generated in such way: using all this, it generates the proper tree, but you get less guarantee that code is executed instead of being in blocks, with the execution at given link by author themselves: it will not be parsed, while DHTML might remove such inside-looking elements and generate something appealing out of it. The user, instead, can check the links that automated content remains.

When aligning titles, we beautify Markdown with these positionings: manual scan revealed the start and end points in actual files, which are under "debug" property of the Json, output of which can be easily deduced from the Markdown output: we don't remove the blocks or change anything about their order, but we add metadata to Json object container, actually to local object tree of Python. 4-format submitter will clearly not lose anything. To include a file in this standard, we add it to the _last_ block, and thus we have "zero" block which can always be the first or last as required, knowing some of it's metaposition: let's make the first and last blocks of something "meta".

## Backlinks

Our preprocessor is able to read backlinks, which need to be at beginning of line and properly formatted, the same requirement appears to titles if you want them special meaning in regards to our site; they will display anyway, even if we otherwise hack some levels perhaps, or rather styles.

__Lets use "&&" as target definitor__:
&& goes to end of last sentence if block support is not active, and activates the block afterwise: followed, for example, by link which is used to activate the block itself: even on dumb servers, it shows the rather dynamic page of the link, a document backlinked.

__Lets use "@@" as backlink__:
Backlinking to "&&-defined" blocks will contain the backlinker's content inside theirs, especially for trusting users, or ones who want to see the local content perhaps or use Spiders to connect sources; but in case: the backlinker is accepted upwards in the folder tree and able to link their public passport, along with the query, in the proper line, and there might be protection level required, such as admin owns the file and others dont write, or other passport units. In case local block or it's parents accept the backlink, possibly from that server or trusted community, or even who your AI trusts or who is in your special list if the page author does not trust this contributor: this emulates Git, where it needs to create a local branch based on theirs, if you need to locally serve and they are not the service provider.

__Lets use "@" as normal link__: This creates a subdocument, which can be visible starting from the link. Let's use "@!" to nest a document, which means it becomes a main-level heading within your own document, appearing at end of this file. DHTML will make them more compact, while in HTML and Markdown they are all visible: it's a book format ..but book can be limited by size and by default, rather than 50 page books, there will be a "pager". One can decide, for example 200 page books, but where it cannot nest or create subdocuments inside limit, it breaks.

For example: AI-generated lists are like tables classically were in calculation books, with pages of values for sin and cos, so they can be useful for a human, who learns: tables and diagrams can be made, but carefully checked. When the generator creates meaningful cards, such as using other example set of Q&A[&D], where I would have pieces of history rather in D, and expect requests there perhaps if even :).


## The Wall

Related to positioning, a page can state it's invisible; it can do this dynamically, including after the POST and GET for passwords.

These are the states:
- Invisible (not in the web address tree)
- Visible (visible in local views to local systems, for example might consider Standard Internal Link within some acceptance level or community belonging /treasure or trait/).
- Public (others can access the web link)
  - This does not make it open: it can ask for password, and become _hidden_ without it, or to show some _cover_. To build the latter is to add "Fire" before the programmatic entity, which initially is just a simple and dumb property.

If there is user-programmed page with custom routing of some links, they can be "hidden" and report the same status: this is not very clear what is "hidden" in this case, they can also easily backlink and become part of the page tree.