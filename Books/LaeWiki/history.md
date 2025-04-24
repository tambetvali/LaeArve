# Wikidata history

We assume that our pages are mostly contained in version control systems. If not, caching the source should be enough to emulate this - it can be compared and links and selections can be updated to newer versions of the pages.

We need to create full access to the Git functionality:
- Given the page, the server, if asked, will use git history to give older versions of the pages.
  - Over time, we solve serving with older, incompatible servers or ones working with those versions of programming languages, which are not there any more; perhaps, the Spider snapshots can be used
- Some older versions can be copied to alternative folders; the Git system is able to connect them if present; those are basically cache folders, and perhaps only the ones from the latest version are used

For training of A.I., the following is used:
- Issue and discussion history
- Version history in version control system

It could be used also to create training cards for the AI to study the following:
- Which Issues demand updates, which discussions give ideas
- Which are the initial generations of the AI
- Which are the final versions
- When the final versions were decided, which updates were used to create which versions

The AI should learn the process of updating and time, and understand when enough decisions are given for each update, and which are the evolving solutions inculding which ones are following later decisions, and which proposals should have be made to reach unavidable decisions, or which questions should have been asked to have possible advancement tracks.