# LAECLIENT

## Outer headers

Client will create the following structure:
- topbar, topbar.icons, topbar.title, topbar.menus{"DHTML": "?view=dhtml", "HTML": "?view=html", "Json": "?view=json", "Markdown": "?view=markdown"}, user None, sitemenu None.
- leftmenu Document, content Document, rightmenu Document
- Footer author="Tambet Väli", "Copyright Creative Commons", "All Rights Reserved"
- Custom Footer: on my page, your own credentials for the document, where the page will remain it's own; in case you are using a custom licence, perhaps you can warn users to not accidentially include your Document, but rather use something like GPL or CC or add a link.

```python
Class LaeClient:
    def __self__:
      self.topbar = topbar
      etc.
```

```python
mymodel = Download.ChatGPT("ChatGPT-4/mini")
mymodel.prepare()
```

```python
Class LaeSpider(LaeClient):
    # Input is your model and the initial topic
    def __self__:
      self.mymodel = mymodel
      self.mymodel.start_training(initialtopic)      
      etc.

    # Input is reason
    def onBreak:
      self.mymodel.stop_training(reason)

    # Question and Answer (Q&A) are the input
    def OnSpy:
      # On link existing under the book and marked spyable
      for qa in page.generate_qa():
        self.addQa(qa.question, qa.answer)

    def addQa:
      self.mymodel.fit([(question, answer)])      
```

This is the intented use of the calculator of my mathematics for an AI.

```python
Class LaeSpider(LaeClient):
    # Input is your model and the initial topic
    def __self__:
      self.autoincrementid = 0

    # Question and Answer (Q&A) are the input
    def OnSpy:
      # On link existing under the book and marked spyable
      for qa in page.generate_qa():
        self.addQa(qa.question, qa.answer)

    def addQa:
      self.autoincrementid += 1
      createfilefile(content=(question, answer), name=self.autoincrementid)
```

Imagine that the Spider is not sensitive to whether it's HTML, Json or Markdown, in each case doing at least something, and it receives "view" as input; DHTML page is not defined to be simple for AI, as this is the user default interface and not an additional source with specific information; the actual information is copy of HTML page with some design and effects if desired by me or my Authors, which could register in github to create some Content like books or additional algorithm for my Laegna mathematics, like generating some type of numbers or extension, or doing operation in different way.

## Our footers

My name, copyright and year or date would be applied; in case of collaboration, collaborator could add their footer text, for example in bottom of their page, like their name, the licence of their work etc.

TODO: Implement user footers. If you are an user, resolve the case of yours and make a contribution to github.

## GitHub awareness

We are keeping our code in version control system: the site should detect and use the version control system, and I plan to use GitHub for the main site as it's primary distribution.

So each format should be github-aware: for each part, it's history should be followed. For example, for dynamic study card, one could open it's history and see either the markdown history with the code blocks, or if it's a code block on it's own, the history of it's code block and perhaps the generated output in each case, with diffs and other github functionalities.