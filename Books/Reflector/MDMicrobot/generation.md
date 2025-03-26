# Generator of Content based on Database

## Database of Laegna Math Website

Database is the Source Code structure, where our users
are often Developers and they utilize the Source Code, which
is often meant to be generic.

## Folder and Documentation integration

__Source File Tree__ is read and parsed into _Documents_, where
folders are either _Documents_, _Chapters_, _Subdocuments_ or
_Nested Documents_. Each folder contains "_tree.md_" to instruct
this process. _Introduction chapter_ is "_index.md_" and other
files are parts of this chapter; folders are used to reflect
as subchapters.

Included md files are read and parsed into _Documents_, where
chapters are either _Documents_, _Chapters_, _Subdocuments_ or
_Nested Documents_. The first title is title of the book. _References_
create subdocuments and nested documents, which might appear
as parts of this document.

__Source folders__ and __md files__ are both parsed into same kind
of structure, visible as pages to users and developers. We call the resulting format Document Object Format, as it contains Documents in objects - it will be fed to user with Flask after preprocessing of these objects.