
# How to use the Laegna Math trainer for an AI
This doc is about how an AI uses the website - content, certantly, can also be used by humans.

This website is meant to contain the following over time:
- To provide some static pages or dictionaries for an AI to learn, where perhaps I create some dictionaries, which have minimal dynamics.
- - For example, each Laegna number is associated with a color, but basically there are 4 base colors, or six if black and white are included, so this means rather a small, static dictionary.
- To provide pages of certain criteria, such as list of first 100 Laegna numbers or 3-digit numbers, where an AI could use them directly for most important studies. Perhaps, in addition to one-time training you would feed the most important pages randomly to an AI.
- - This kind of page will contain the list of numbers in a table, with some additional information. Json format for an AI would have the table available in easily accessible Python version, where some rows or columns can be marked as questions, others as answers, others as additional information, tags or additional links related to this number, to follow or not (such as the number E or a list of possible enumerations of Chakras might refer a page of chakras).
- To provide random, dynamically generated lists or pages of numbers and their information.
- - Link can be used to open a list of random numbers. This needs to be cached as it's different each time, so possibly it would redirect into a page containing random number seed or it would generate a temporary static page to survive a certain time (we don't use databases).
- - Each number has similar associations to static number lists, in sense that it has a table and links open specific numbers.
- - The spider downloads the list, processes each link, which meets it's criteria, and regenerates the page.
- - Alternatively, the link can be used for direct access of dynamic page with random number, for example by choosing a dropdown.

# The Laegna Math Programmer website

Each page has an address and normally, the addresses are structured in such way:
- The address of a more general page is shorter.
- The page, which should be followed to learn this topic is marked with "follow" metatag.
