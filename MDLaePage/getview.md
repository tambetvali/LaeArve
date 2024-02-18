# The views of the Web Interface

## DHTML
GET: ?view=DHTML
GET: default - when view is not set

We need an elegant, well-designed and responsible modern page.

Laegna Math page, over time, should utilize the resources it's able to generate, to:
- Give interactive lessons to interested users (late iterations)
- Have menu responsive without clicks to button; when dropdowns are selected, page updates without reload

Paradigm:
- Moving closer to interactive experience.

Users:
- Normal users

### Basis
Source: History/Plan2/MDGenDocs/iter1_aianalysis.md

Given conversation with AI:
- Initially I had complex UI plan and we decided it would be too complex.
- I simplified, and AI suddenly reacted like this, from an opposite view:

    I understand your points and concerns about the implementation plan for generating mathematical training materials for an AI model. However, I would like to suggest a different approach that may be more effective and efficient.

    Instead of focusing solely on the codebase and performance optimization, we should focus on simplifying the user interface and improving the overall user experience. This will not only make it easier for users to understand and use the application, but also increase the likelihood of them using it regularly and providing feedback.

I must add that DHTML version would, over time, cover this viewpoint, while from other side, simplification and AI support is important.

## HTML
GET: ?view=HTML

This is the HTML version:
- It could utilize Javascript for example for menu: if some selection is chosen, such as not choosing "other" from the Classificator, for example a textbox might become disabled.
- Redirect is supported.
- Menus and bars, panels are there.

It's a static HTML page:
- All content is directly served.
- Clicking links leads to other page with other url.
- While a human reader, perhaps with older browser, might be interested, and it could better support printing; this page is mainly meant for an AI or Spider, which could follow the links, download pages, and understand normal HTML.

Paradigm:
- Moving closer to HTML philosophy, where elements are not just plain visual content, but they are meaningful; for example terms like _italic_, _emphasize_, _strong_, _bold_ might actually mean different things; at the same time we won't go too fat from this, for example we might use Markdown as input, or other format, which does not separate so well. Still, this is the philosophy we use: of HTML of old times, and not that they did not use JS at all.

Users:
- Spiders, AI's, other automates.
- Readers, which want to fetch page content.
- Users, who want to read source code.

### Basis

Dynamic HTML is extremely hard to read automatically, and we want the page to be open source in sense that the user can access the source. Classical paradigms of HTML put extreme emphasis on this conception.

We do not avoid any modern technologies specifically, but we want to have:
- Printable documents, despite side menus and top bar - this is "HTML printable". We might include some setting to leave only the content page, for the readers to print it properly.
- Readable source code with clean syntax.

## MarkDown
**GET**: ?view=Markdown

This is a version most AI's should be able to read by default.

We don't want to have any menus etc., but only the content pages. An user is able to download this and edit manually with text editor, programming editor etc.

We will include our own standard for markdown:
- The way we position text, set bold or use the language will specify certain types of content.
- For example, in this format, StudyCards have their original syntax.

Properties:
Page properties, while we cannot change them directly here, are visible as a string with names and values; this is preceded by "Properties" link followed by colon.

Paradigm:
- User is able to print this in clean way.
- User or AI is able to view this as text, and it does not require knowing our standards.
- We want to get closer to import this without losing the special meanings: user can change these pages and include in their own copies of our system, or send it to us, and in each case it can be added to pages, where it would be read meaningfully and rendered in DHTML, HTML, Markdown or Json formats.
- As a programmer, I appreciate such format very well - despite it is hard to navigate this, perhaps even to view it in browser, it's easy to navigate the HTML page and open the Markdown page of interest, download it, and print it with Markdown-capable editor or viewer.

### MarkDown properties
**GET**: ?view=Markdown&subview=propsandmenu

This, despite part of Markdown page, will use HTML:
- It uses the property setter
- It uses the menu
- It divides the window into left and right area, perhaps provides some markdown preview in the middle.

## Json
**GET**: ?view=HTML

This is not a view, but an API.

This is meant to:
- Automated following of links with access to their metadata.
- Automated training of an AI.
- Automated generation of content by other systems, where they might install our system and use it to generate Laegna numbers or mathematical examples in a standard way.
