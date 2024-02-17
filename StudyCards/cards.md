# Cards

Cards are:
* **Dictionaries**: Connections to identifiers to their values, words and general attributions to their data or longer content.
* **DocumentCards**: They are like stand-alone dictionary items, encyclopedic documents. *DocumentCard* defines one term, for example a sentence or word, to one page textual content, so where you have dictionary, in it's own folder, it could have subfolder *Cards* to connect it with Cards. Using the word "Cards" without explanation, but in specific meaning, we mean *DocumentCards*.
* **Tables**: Table is a two-dimensional dictionary with less space for an item, often it associates very short content with two-dimensional labels and interrelations with other contents of the *Table*. Primary elements are often links - in our system, it would connect them to the *Tables* as integral elements.
* **DialogCards**: *DialogCards* connect, equal in size with *Dictionaries*, definitions to their identifiers in timebound manner, thus separating not only by identifier, but also by position. Then, we repeat the same identifiers, but get different content elements, such as several questions and answers, with contextual items.

## Examples of Format and Content

### Dictionary

Dictionary is made of such items:

**Word**: It's meaning.

### DocumentCard

DocumentCard is similar:

**Word**:

    It's meaning.

or:

**Word**:

It's *meaning*.

Where the basic thing is to have them on separate lines; document length is comparative to article of encyclopedia, where word and it's description length in dictionary is shorter.

### DialogCard

**Word**@*time*:
an event.

**Actor**@*time*:
an event.

### Relation to titles

In each of these, we use titles. For an AI, if a single element is given, title is given as a context.

For example, if word "Money" is under "Theft", which is under "Good and Bad", context would be:

Dictionary item:
* _Context_: *Good and Bad* => **Theft**
* _Article_: **Money**; is the object being stolen.

(notice I used semicolon to not break the sentence - I want to create a reliable syntax for the system to read all md files in certain directories and to be able to serve them under pages; my own contribution, anyway, is quite small in relation to how much is needed for an AI to learn).