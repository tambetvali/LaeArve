# Chapters (content index)

Use the same content for Left side menu and the actual Document content indexes - this, because the separation of things into same document and it's chapters, subdocuments or separate documents is rather a metatag than substantial difference in design; each of them links down and the links can be structurally followed - everything is in tree, and in order.

Exception to the absolute tree structure:
* If we have a class, which has same backend, but multiple possible frontends (as chapters), the child classes we inherit from same parent class might belong to different branches; sometimes we refer to another branch from the document, but it should be visibly different if it's not part of the same tree; also links, which get us back, should look different in the same or another way.

## Html Paradigm

Menu is the following:
* Main menus are always visible
** As you open them, top-level subitems of open branch become visible
** There are not too many of them - the menu is not too long

Chapters have the following structure:
* Parts open in current document are visible in navigation, where you can scroll
** Subdocuments are selectively visible, for example if there are 100 subdocuments of some chapter, there are only 3 or 5 visible, and the next link is for all the rest, it opens it in new document.
*** Other documents are sometimes visible, in limited amounts - space in content index should be considered, for example if the current document has only 5 chapters, but links to many, there might still be like 20 visible chapters; in long-term future this might even depend on AI to choose them based on user preferences.

## Markdown paradigm

More or less, every chapter you have in current Markdown document, is visible, and chapters you don't have are not visible - you cannot click on links, so it's useless to have the names in printed versions.

## Json paradigms

AI can have considerably longer content, if it asks for it: AI could have a special setting, for example, to download more or less the whole structure tree with metadata - then, it can decide on it's own, what and how to fetch (perhaps this comes even earlier as simpler functionality, than the autoselector, but we must assume an user does not know always what they want).