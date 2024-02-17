# Page parameters

Once an user has selected a general page from the right menu, on the left side they can specify the parameters, for example:
- How many items to display
- Which format to use for numbers
- Are they interested in compact list, or more detailed information

There are three paradigms:
* The HTML paradigm. In this paradigm, user is navigating with visual elements; they navigate the web page, which is dynamic and responsive, and they do it visually and with the mouse, so it's UI-centric view of the elements.
* The Markdown paradigm. In this paradigm, print version is static and the user can only switch the pages. In this paradigm, they see the properties as important information about the content: after a link called Properties, and a colon, labels are associated with their values.
* The Json paradigm. This is for Spiders, AI's, computer programs which use this information. It's not visual, but labels are represented in a list or dictionary, where name of a property is dictionary key and it's first element as well, like an ID in SQL table, and not divided into blocks, but the list is flat - block name is property of each element, being repeated. Both names and some values can have metadata.

## Content types

Classificators - Single Value Selectors from Indexed List:
* Visual type (HTML): dropdown, radio buttons represent a selection from given list
* Informative type (Markdown): we are interested in label and value, the current selection, but cannot use the static information dynamically. In web version, when we click on link "Properties", standard HTML menu is rendered in full page.
* API type (Json): The same content is list of indexed values, and an AI can study the strict documentation, such as how big model would need content exactly this advanced. An AI will then know the GET attribute by name, and not by label, and instead of using visual elements it will create the get parameter by assigning a value - user cannot do this directly.

The element behind: GET parameter, it's type and value, are the same; user like an AI is visually creating a GET query, but AI is doing this on different basis.

Sets (Multiselectors from Indexed List):
* Visual: Checkboxes or multiselect dropdowns or value lists.
* Informative: label and value.
* API: a Set, such as {"Q", "A", "D"} would require question, answer and documentation.

Text and numbers:
* Visual: Textbox, Text area.
* Informative: String, Numeric type.
* API: A list item, which is labelled numeric and has some labelled values, for example if there is temperature 0-100, it can have 20 marked as negative extreme, where 80 is marked as positive extreme, and values from 40-60 can be marked as the middle way, safe choice.

## Content Structure

LaeConfigurator contains List of LaeParameterBox, and each LaeParameterBox with Label and Content has list of elements as a content. In visual version or markdown version, thus there are labels between elements, but in API version elements are classified and have something like an ID - in "table of elements", dict or list of dicts or lists, each element has a "parameterBox" property in output, but a single one-level iterator can be used for convience (AI can handle the properties as particulars).