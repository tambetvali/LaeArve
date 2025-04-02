# Motherboard Architecture

This is the explanation about how to parse file trees:

Associate the root node:
- Scan filesystem
  - There is always one tree.md, which marks a virtual root folder, as displayed in web.
  - There is always one tree.md, which marks where the real root folder, with exception
    to virtual folder, is to be projected.

This way, programmers see the code project, while the users, with free access to the code as it's rather important part of documents and imaginations: I prefer that we bring examples to AI, about how to solve subsets of problems, perhaps for different websites: sometimes, architecture pieces appear in code.

Now we have the http output format for Flask, about where to project.

It now equates the three classes:
- File with different suffixes
- Folder with same name, but without extension
- All those items, when the name part is same, form an entangled collection.

Thus, you can instantly add attachments and things _inside file_, where the file with all the same-folder attributions (to become a parent node reflector for given directory, with little surroundings of the parent nodes and "<- Follow Back" links, backshift in time again for space).

Titles need to have associated file names:
- Then they become the little supercards to show top left above the main menu, displaying the first 512 characters or something with "->" link.
- Under this:
  - Subtitle group on card: show previous docs in books.
  - Free title group, top-level content without indent: show the content of current book.
  - Subtitle group, again a yellow card contained: the following chapters.
  - The higher-level chapters are garbage-collected: depending on screen size, always also in GET input, chapters are left out and the list is compressed, other parts are relatively nesting the chapters into common, shorter content. It should be what it seems: shorter by that degree by some comparing unit.

These titles exist in higher-level documents, which are not visible, but contain a little chapter with content index and some introducing sentences where needed: it can project the chapters in low-level titles, such as "########", which by our preprocessor is a command: project this two levels down, the title, but try to reduce the level for this file to show it anyway, so that it uses the first free "title slot".

For this compression purpose:
- We remember the strict overness and underness of the title, along with it's preferred position; it's rather a tensor than constant, so if we lack space we should compress more levels into 6 levels by using the level number, which is not used. If we lack space, we need subdocument link: while this contains good amount in parent, the higher level can be broken away here. The subdocument mainly needs a file name, and given these names in list, not content of nameless chapter levels, the URL in the web server, and position in Document Collection, which the Spider can do: necessarily being able to use Garbage Collectors, as some generators need to be infinitely long and have to be collected immediately when training has been completed, moreover sometimes you need only verified and double-checked content, for example humans have verified collection of random samples and continue with small amounts per time unit.

## Order

Higher level orders should generally override lower-level orders: where two chapters have fixed order in higher level, it's projected to lower levels for the same titles. This is not necessary as the algorithm is complex, also the syntax for then-special cases.

Alternatively: ml file associated is strongest in chapter order (I currently use this as it started to make more sense).

## Title

# Title

The order shown puts the smaller title _behind_ the bigger title, and to the end from _behind first h1 title_ where h1 can be replaced with absolute mostleft title with smallest h number.

This executes several layers of logic:
- Last chapter contains the title, but _closer_ to it, such as personal notes rather than treelike continuation.
- The chapter, then, can have immediate headers, which relate it to it's immediate content: for example, study cards are contained in it's ending blocks, but not in the lower tree.

Sometimes, a title can be imagined in a tree, where immediate elements are forming tree in _right_ side of it, or appear in menu when it's opened from button after the title.

Sometimes, and usually in less compact and interactive form, those are cards and direct content under the chapter, while the actual lower levels might contain completely different logic. In the same chapter, logic is integrated by it's creator.

## Linking and Backlinking

_Notice_: backlinking works for all sites it's _aware_, but spider is free to add links itself is aware of: like contained link to local user profile, such as _localProfile_, which will be rendered by spider instead and shown in proxy, where user can even use their own document folder and process their own dynamic content. Given, perhaps if no protection is used, that standard scripts are ran, but some safe collections can be added.

@@ [LinkName](http:linkurl)

This would add the page to the target link, synchronizing all chapters with known orders and having target-first order of links contained only in one or another. Links would be recognized by title, even if this behavior can have exceptions by headers, initially small mistakes of rendering.

@ [LinkName](http:linkurl)

This creates forwards link: the other page will be contained here.

## Other parsed elements

> ! This will be parsed into a lamp block.

> ? This will be parsed into a question block.

> . This is the more neutral notice

For example to be used for "read more" links; autogenerator only generates the links user lacks in this purpose.

Referred material would appear inside a card:

> @@ [LinkName](http:linkurl)

> @ [LinkName](http:linkurl)

> # Title

The chapter, in case of such Title, would appear inside a (yellow) card (all Study cards are yellow), without using the block quote again: I think we make a small exception here, but it's not considerable.

So outside the card there is the chapter, but it rather does not have it's own title structure unless it's a suitable format: the chapter is white of blueish.

The yellowish and blueish colors are very close to light.

## Nested Documents

> $$@@$$ [LinkName](http:linkurl)

> $@$ [LinkName](http:linkurl)

Contain the document:
- Chapter index in position of nesting, where is the introductory part.
- Document itself, along with deeper content index with rather more chapters, above it; usually all human-created chapters are shown and AI-generated chapters are generalized under some name, which might also appear as discerner of them at the positions of this curve.
  - Generated content must take care of it's links, where the links must refer to equal content, possibly with version number.

It's rather better if the version numbers are updated manually, and their users would need to synchronize: they create objects with different versions, where another version might not recognize the properties.
- Notice that initially we might not have power over version control.

## Garbage collector

It now has like 4 dimensions, to collect the garbage generally.

It let's user to open the "subdocuments", where for example a subchapter can still be associated with a large folder, which comes out itself. On higher levels, small md files containing shorts of some chapter sets can be displayed only, and appear as symbolic icon inside the folder, when opened from there (parents _can_ yield, but the connection can be rather static).

It knows the good sizes for any bot, any view and any machine or index. It can generate random content to train the index embedder bot.

> . Continue with: ...

Here would be link to go deeper to garbage collected document, where those parts are not collected.

