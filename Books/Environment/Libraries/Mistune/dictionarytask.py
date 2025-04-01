import mistune

class DocumentPreprocessor:
    def __init__(self, markdown_text):
        self.markdown_text = markdown_text
        self.definitions = {}
        self.index_instances = {}
        self.small_definitions = {}
        self.blocks = []
        self.parse()

    def parse(self):
        """Processes the Markdown text and applies transformations."""
        lines = self.markdown_text.split("\n")
        current_encyclopedic_item = None

        for lineno, line in enumerate(lines, start=1):
            # Check for block markers (! or ?)
            if line.startswith(">!"):
                self.blocks.append(("callout", "💡", line[2:].strip()))
            elif line.startswith(">?"):
                self.blocks.append(("rewarded_problem", "❓", line[2:].strip()))
            
            # Handle definitions based on bold/italic formats
            elif "__" in line or "_" in line:
                if "__" in line:  # Bold text
                    bold_text = self.extract_bold_text(line)
                    if bold_text.endswith(":"):
                        # Add to index and instance collection
                        element_name = bold_text[:-1]
                        self.index_instances[element_name] = lineno
                        current_encyclopedic_item = element_name
                    else:
                        # Add as a candidate for dictionary
                        self.definitions[bold_text] = lineno

                if "_" in line:  # Italic text
                    italic_text = self.extract_italic_text(line)
                    if current_encyclopedic_item:
                        # Link to the current encyclopedic item
                        self.small_definitions[italic_text] = current_encyclopedic_item

            # Handle "@ links"
            elif "@" in line:
                self.process_links(line)

    def extract_bold_text(self, line):
        """Extracts bold text enclosed in __ from a line."""
        start = line.find("__") + 2
        end = line.find("__", start)
        return line[start:end]

    def extract_italic_text(self, line):
        """Extracts italic text enclosed in _ from a line."""
        start = line.find("_") + 1
        end = line.find("_", start)
        return line[start:end]

    def process_links(self, line):
        """Processes @ links in the line."""
        words = line.split()
        for word in words:
            if word.startswith("@"):
                # Simple linking logic (expandable for real linking)
                link_target = word[1:]
                if link_target in self.definitions:
                    print(f"Linking @{link_target} to definition at line {self.definitions[link_target]}")
                else:
                    print(f"Link @{link_target} not found in definitions")

    def display_summary(self):
        """Displays a summary of processed data."""
        print("Definitions:")
        for key, value in self.definitions.items():
            print(f"  {key} (defined at line {value})")
        print("\nIndex Instances:")
        for key, value in self.index_instances.items():
            print(f"  {key} (appears at line {value})")
        print("\nSmall Definitions:")
        for key, value in self.small_definitions.items():
            print(f"  {key} (linked to encyclopedic item '{value}')")
        print("\nBlocks:")
        for block_type, symbol, content in self.blocks:
            print(f"  {symbol} [{block_type}]: {content}")

# Example Usage
markdown_text = """
>! This is a callout block with important information.

> ? This is a question block that prompts users to solve something.

__Encyclopedic Item__:
This is an encyclopedic entry that spans multiple paragraphs.

This next paragraph is still part of the encyclopedic entry.

__Dictionary Term__: Defined and used for indexing purposes.

_Small Term_ is used here as a reference to a small AI-friendly dictionary.

@linked_definition
"""

processor = DocumentPreprocessor(markdown_text)
processor.display_summary()
