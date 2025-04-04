# 💻 Laegna Terminal

The first title is H1:
- \# Title

(and we need one parser, which makes sense of only titles and blocks, connecting to Mistune: I think we can hook the title block on input, and store the start and end of the line).

Before that title, there can be lower-level titles.

Those lower-level titles are _applied to the end_ of chapters, so you can write for example, a summary into the beginning:

```markdown
## The Terminal

This part is added to the end.

Scripts you put inside, will be executed at the end as well.

# Index

Here the file starts.