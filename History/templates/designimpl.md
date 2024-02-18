# Laegna Math Webpage - DHTML, HTML, Markdown and Json implementation and Flask template and Python class

## Python classes

## Class MarkdownTemplate

Algorithm for creating the class:
1. Implement Class MarkdownTemplate, which is Flask template.
2. It takes input arguments to "def __init__(self, view, getDict)", where "view" is extracted from request.args, such as ?view=Json, and getDict is request.args converted into dictionary of get variables as keys and their values as values.
3. It parses the Markdown file using instance of ClassMarkdownReaderTemplate
4. * **DHTML**: First level header is converted to title, under the title there is dictionary of commands, such as additional style sheets (line "__style__: stylesheet.name"), header options and other head elements, but also window title and subtitle such as dictionary items of lines "__page name__: Laegna Spireason" or "__subtitle__: Text directly under main header"; content of this header until next subheader is converted into static head content available on all pages, such as small legend or term dictionary; AI would learn this as context of every page; dictionary values would be meaningful, not mime types but for example something like "include in Google". Second level chapters are Menu, Content, Tools, which are converted to three cells of the middle row of the Content Table as described in HTML Template. Rest of titles until 6 are converted into 4 levels of actual titles. "-----" on one line, but not other sequences of minuses, create new pages for pager.
    * **HTML**: Is equal to DHTML, but with different template, where each second-level title is presented as \<h1> instead of as table cell, and each link has it's actual address after the link in braces. This can be even copy-pasted to an AI with either formatting or without, and it can be read in print version without looking ugly. SubDocuments come later with more 1st level headings and they are linked with link jumping downwards, and it would help if they would link to page numbers in print, but it will definitely contain the names and content would be included here and additionally in main content, maybe divided into parts if complexity is bigger than 16 or 24 levels, as "books" of the content index; they are not included in chapter structure.
    * **Markdown**: The document is present without modification. SubDocuments are included, or they are moved below with separate 1'st level headings and linked.
    * **Json**: The document would be present in structured way, and with ?lessons=True or ?lessons=False, StudyCards would be included or not, and with ?documentation=True or ?documentation=False, all the rest would be turned off. Json is divided into pages.

    Dynamic generation:
    - Dynamically generated Markdown content, which is added as Markdown entities with one Markdown file contained, would in-positionally replace all the repeated chapters, excluding the higher-level elements containing only whitespace between title and first subtitle, but not empty last-level titles where you could make them empty in advance by including the same position in nested header tree twice; static documents can contain several headers with same name in same branch, but dynamic content would override them, for example changing the topic.

    