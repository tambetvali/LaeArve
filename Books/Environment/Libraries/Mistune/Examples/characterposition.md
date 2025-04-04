# Character Positions

I think the py file with the same name should be automatically appended to it's md counterpart, which does not refer properly :)

AI task to have character positions in mistune-parsed blocks, to refer back to original content and process right parts of our other, simpler parser:

```
Can I have a class which does just that:
- Markdown Mistune blocklist is contained -
Each paragraph is associated to original content so that it's added the property: start, stop, linenumber, characternumber, position in source text in bytes and position in utf-8 characters
- Blocklist content can be seen as objects, which contain primarily all the tags added through the script (where it registers them), and inside that the block itself.
- Blocks can be added, where batch is generated: to end of list, before list, before block, after block, or to inside of block.
```