# Wiki format for Laegna Math Website

We have the Laegna Math Website, which contains Documents - defined in folders, Markdown files or files, which can be converted to Markdown files if done:
- Folder structure appears as chapter structure.
- Inside Markdown files, the chapter structure appears as chapter structure.

With this, we have the input and output format - the filesystem in server, and the webpage hierarchy as it's served. Within client, another structure is formed for the webpage as it's downloaded (noticeably at some point, one would not use "http" webpage links, but rather converts them to local links - we should initially use rather relative links).

## Redaction format

Each wikichange has something like a following structure:
- Original page: this is an object, which is referred
- Wikipage: this is the referrer
  - There is a link back, to which page is referred; if needed, this can go back all the way to original page, through the Spider folder, and if not needed, then not
  - There is the ping instruction, which instructs the server to ping back to notice existance of this page
- Prolog tags: prolog sentences, which can refer to original and wikipage, can create a relation: this creates a Prolog  object, which can be queried
- Cache folder can be created with root name of the md file for wikipage, which contains copy of the original page; Spider snapshot would contain this anyway. If page is removed or versions change, it's good to have comparison to this original page. Spider can download all related items in forward-structure, and the licence for cache pages should consider this differently from served pages (it should be somewhat hidden)
- Template: template is generated for the new md file, which creates a wiki object

Template structure:
- It can duplicate the chapter structure of referred page with proper metadata. Then, each duplicated chapter refers to some original chapter; for example it can be instruction to generate this chapter or question to be answered by it
- It can be copy of the original md file, to be changed so that there will be an update; for example, errors are fixed

Metadata - such as the wiki page is an update, question list or instructions, will be contained in Prolog statements; Prolog programs for given clients can process this: for example, their Prolog library can create Q&A pair knowledge for the case that this is question to be answered.

The wiki format should be easy and usable:
- If needed, each chapter can initially contain a summary, which is known to be a summary
