import mistune

class AdvancedMarkdownBlock:
    def __init__(self, content, start, stop, linenumber, charnumber, byte_position, utf8_position, tags=None, submodules=None):
        self.content = content
        self.start = start
        self.stop = stop
        self.linenumber = linenumber
        self.charnumber = charnumber
        self.byte_position = byte_position
        self.utf8_position = utf8_position
        self.tags = tags or []
        self.submodules = submodules or {}

    def add_tag(self, tag):
        self.tags.append(tag)

    def add_submodule(self, name, module):
        self.submodules[name] = module

    def __repr__(self):
        return f"<AdvancedMarkdownBlock tags={self.tags} content={self.content[:30]}... submodules={len(self.submodules)}>"

class AdvancedMarkdownParser:
    def __init__(self, markdown_text):
        self.markdown_text = markdown_text
        self.blocks = []
        self.parse()

    def parse(self):
        parser = mistune.create_markdown()
        lines = self.markdown_text.split("\n")
        char_position = 0
        byte_position = 0
        nested_levels = []

        for lineno, line in enumerate(lines, start=1):
            if line.strip():  # Skip empty lines
                utf8_position = byte_position

                # Special syntax processing
                if line.startswith("@") or line.startswith("@@"):
                    tags = ["link"] if line.startswith("@") else ["linked_markdown"]
                elif line.startswith("§"):  # Special code block symbol
                    tags = ["special_code_block"]
                elif line.startswith(">"):
                    tags = ["block"]
                elif line.startswith("#"):
                    tags = self.process_heading(line, nested_levels)

                else:
                    tags = []

                content = parser.parse(line)
                block = AdvancedMarkdownBlock(
                    content=content,
                    start=char_position,
                    stop=char_position + len(line),
                    linenumber=lineno,
                    charnumber=char_position,
                    byte_position=byte_position,
                    utf8_position=utf8_position,
                    tags=tags
                )
                self.blocks.append(block)

                char_position += len(line) + 1  # +1 for newline character
                byte_position += len(line.encode("utf-8")) + 1

    def process_heading(self, line, nested_levels):
        level = line.count("#")
        if level > 6:  # Subdocument
            nested_levels.append(level)
            return ["subdocument"]
        elif nested_levels and level < nested_levels[-1]:
            nested_levels.pop()  # Reduce levels backward
            return ["heading_backwards"]
        else:
            nested_levels.append(level)
            return ["heading"]

    def add_block(self, content, position="end", reference_block=None):
        new_block = AdvancedMarkdownBlock(content, start=None, stop=None, linenumber=None, charnumber=None, byte_position=None, utf8_position=None)
        
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
            reference_block.add_submodule("nested_block", new_block)
        else:
            raise ValueError("Invalid position or missing reference_block.")

    def garbage_collect(self, max_levels=6):
        to_remove = []
        for block in self.blocks:
            if block.tags and "subdocument" in block.tags:
                if len(block.submodules) > max_levels:
                    block.submodules = {"link": "Too many nested levels, see detailed structure."}
                    to_remove.append(block)

        for block in to_remove:
            self.blocks.remove(block)

    def display_blocks(self):
        for block in self.blocks:
            print(block)

# Example usage
markdown_text = """
# Chapter 1

This is a paragraph.

###### Subdocument Level

Another paragraph here.

@linked Markdown

§ Special Code Block
"""

parser = AdvancedMarkdownParser(markdown_text)
parser.display_blocks()
parser.garbage_collect()
parser.display_blocks()
