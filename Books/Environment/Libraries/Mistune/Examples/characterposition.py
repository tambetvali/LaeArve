# In this file, CoPilot is attempting to connect mistune parser with letter position. It extends the parser.

import mistune

class MarkdownBlock:
    def __init__(self, content, start, stop, linenumber, charnumber, byte_position, utf8_position, tags=None):
        self.content = content
        self.start = start
        self.stop = stop
        self.linenumber = linenumber
        self.charnumber = charnumber
        self.byte_position = byte_position
        self.utf8_position = utf8_position
        self.tags = tags or []

    def add_tag(self, tag):
        self.tags.append(tag)

    def __repr__(self):
        return f"<MarkdownBlock tags={self.tags} content={self.content[:30]}...>"

class MarkdownParser:
    def __init__(self, markdown_text):
        self.markdown_text = markdown_text
        self.blocks = []
        self.parse()

    def parse(self):
        parser = mistune.create_markdown()
        lines = self.markdown_text.split("\n")
        char_position = 0
        byte_position = 0

        for lineno, line in enumerate(lines, start=1):
            if line.strip():  # Skip empty lines
                utf8_position = byte_position
                content = parser.parse(line)
                block = MarkdownBlock(
                    content=content,
                    start=char_position,
                    stop=char_position + len(line),
                    linenumber=lineno,
                    charnumber=char_position,
                    byte_position=byte_position,
                    utf8_position=utf8_position
                )
                self.blocks.append(block)

                char_position += len(line) + 1  # +1 for newline character
                byte_position += len(line.encode("utf-8")) + 1

    def add_block(self, content, position="end", reference_block=None):
        new_block = MarkdownBlock(content, start=None, stop=None, linenumber=None, charnumber=None, byte_position=None, utf8_position=None)
        
        if position == "end":
            self.blocks.append(new_block)
        elif position == "beginning":
            self.blocks.insert(0, new_block)
        elif position == "before" and reference_block:
            index = self.blocks.index(reference_block)
            self.blocks.insert(index, new_block)
        elif position == "after" and reference_block:
            index = self.blocks.index(reference_block)
            self.blocks.insert(index + 1, new_block)
        elif position == "inside" and reference_block:
            reference_block.add_tag(new_block)
        else:
            raise ValueError("Invalid position or missing reference_block.")

    def display_blocks(self):
        for block in self.blocks:
            print(block)

# Example usage
markdown_text = """
# Heading

This is a paragraph.

Another paragraph here.
"""

parser = MarkdownParser(markdown_text)
parser.display_blocks()
