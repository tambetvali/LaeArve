# Markcode

_This is just an unrelated idea - I keep it a little bit like an idea database; while some parts and generators are enough for AI's to develop, it should contain all inspiration for the years of following._

Let's define a subset of Laegna Programming Language we might want to create:
- Let's use the Markdown definition as basis.
- Code Blocks contain "Assembly" code, which is made of low-level structures. They work with data, which can be high-level analyzed.
- Instructions are sentences, such as "Move the Turtle up."
- They can be defined in headers, such as "# Moving the Turtle up."

Consider the following:

# Moving the Turtle up

Command: Move the Turtle up.

Subtract ten from position of the Turtle.

## Subtracting <x> from position of the Turtle

Command: Subtract <x> from position of the Turtle

```python
  turtle = Turtle.get_contextual_instance()
  turtle.X -= Laegna.getVariable("<x>")
```

My question:
- Can we create specific data formats based on Markdown, where one can contain data trees, but associate with names and variables?
- Can we standardize, a bit, such AI-interpretative language, which has strong syntax, but with little exceptions made by an AI?

For example, under each general name, there will be a command in case of doubt; the "Command" itself would be defined as AI-learnable, which would associate this with proper grammar.

AI would also interpet an aspect of the code:
- For example, what you mean if you request "Laegna" about a variable? What you mean by "contextual instance" of the Turtle?
- It would have a given set of commands, mostly, but it would associate it in different ways.
