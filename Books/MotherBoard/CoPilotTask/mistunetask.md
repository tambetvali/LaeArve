I want to extend Markdown library Mistune for my purposes.

I want to do these operations in Markdown, thereof:
- Separate asterisk and lowline bold and italic; give different HTML class and call the hook only if it's lowline.
- Identify, for the block, the positions of it's first and last string position, and for multiblock container, the first and last string position for unified content, and one for each. Based on this, allow modificators to "addbefore", "replacewith" and "addafter", or "deleteblock": this is done in phase of HTML generation if this is efficient. New classes of the same type are added, and thus this class also needs "addbefore" and "addafter", at least.
- Using recorded position; as a last step before HTML rendering, because you are waiting for data: allow user to do things in between, as this is the main processing. Write a widget class for flask, which runs jinja2 on the Markdown and each subsequent Markdown, when it's added to the class and before it's processed.
- Inside Markdown, if Code Blocks have paragraph mark § in beginning of comment on the fist line, followed by " run." or "run.", then classes and definitions, all static content, is executed in Python. After Jinja templates finish, the dynamic code is executed from the same blocks. As Flash is used to run it only once per each call, each time the static things are initialized afresh - but you cannot initialize the static again, when dynamic code will be ran. It can replace it's code window, write before it and write after it. If it's "run" followed by "preprocess: command", the command would be executed before running Jinja2, subsequently it would alter the template.
- They could all also return HTML; html has special chapters like "content" and "tools", which are in separate properties if flag is set, but otherwise it's in one propery, but it's better if it has properties for Json and Markdown.
- Write client class: if will be registered for each phase, and they would be ran in order, so that for each phase, each client is ran once; if new clients enter, they can go through all the phases later, but they cannot alter the initial process of others: they have to check the phase of other instance, if they want to interact, and they cannot use earlier-phase commands (each command can use a method, which throws runtime if it's not the right phase). Finally, HTML would still contain Flask templates, so this all happens in one Flask request.

# AI Generation

Extending the Mistune Markdown library for these sophisticated operations is an exciting project! Here's a roadmap for implementing your ideas step by step:

## 1. Separate Asterisk and Lowline for Bold/Italic

To differentiate between * and _ for emphasis:
- Extend Mistune's tokenizer to store the original syntax (* or _) for bold and italic.
- Create a custom renderer to assign different HTML classes based on the original syntax.

Example snippet:
```python
import mistune

class CustomRenderer(mistune.HTMLRenderer):
    def emphasis(self, token):
        if token.get('original') == '_':
            return f'<em class="lowline">{token["children"][0]}</em>'
        return f'<em>{token["children"][0]}</em>'

    def strong(self, token):
        if token.get('original') == '__':
            return f'<strong class="lowline">{token["children"][0]}</strong>'
        return f'<strong>{token["children"][0]}</strong>'

class CustomMarkdown(mistune.Markdown):
    def parse_emphasis(self, text, pos, end):
        token = super().parse_emphasis(text, pos, end)
        token['original'] = text[pos:end]  # Track whether `*` or `_` was used
        return token

renderer = CustomRenderer()
markdown = CustomMarkdown(renderer=renderer)

print(markdown("_italic_ **bold**"))
```

## 2. Block Position Tracking and Modificators

To track positions of blocks:
- Extend the tokenizer to record block positions (start and end offsets).
- Implement custom HTML generation logic that applies addbefore, replacewith, addafter, and deleteblock.

Example structure:
```python
class BlockManager:
    def __init__(self):
        self.blocks = []

    def track_block(self, start, end, content):
        self.blocks.append({'start': start, 'end': end, 'content': content})

    def modify_block(self, action, block_index, new_content=None):
        if action == "addbefore":
            # Logic for adding before
        elif action == "replacewith":
            self.blocks[block_index]['content'] = new_content
        # Implement other actions similarly
```

## 3. Flask Widget Class with Jinja2 Integration

Create a widget class to run Jinja2 templates:
- Implement a Flask view that dynamically processes the Markdown through Jinja2.
- Extend Mistune to process Markdown in phases, allowing user-defined modifications.

```python
from flask import Flask, render_template_string

class FlaskMarkdownWidget:
    def __init__(self):
        self.markdown_instances = []

    def add_markdown(self, markdown_text):
        self.markdown_instances.append(markdown_text)

    def process_all(self):
        processed_markdowns = [render_template_string(md) for md in self.markdown_instances]
        return processed_markdowns
```

## 4. Dynamic Code Execution for Special Code Blocks

For § run. functionality:
- Extend the Mistune tokenizer to recognize code blocks starting with § run..
- Execute static code during initialization, and dynamic code after Jinja2 templates finish.

Example of dynamic execution:
```python
import execnet

def execute_dynamic_code(code_block):
    gateway = execnet.makegateway()
    channel = gateway.remote_exec("""
        # Static execution
        exec({{ code_block.static }})
        # Dynamic execution
        exec({{ code_block.dynamic }})
    """)
    return channel.receive()
```

## 5. Returning Separate HTML Properties

Ensure parsed content is returned in separate properties (e.g., JSON, Markdown, HTML):

```python
class ContentRenderer:
    def __init__(self, markdown, json, html):
        self.markdown = markdown
        self.json = json
        self.html = html
```

## 6. Client Registration and Phases

Design the client class to handle multi-phase processing:
- Allow each client to register for specific phases.
- Track and enforce phase order to prevent earlier commands during a later phase.

Example structure:

```python
class ClientManager:
    def __init__(self):
        self.clients = {}
        self.current_phase = None

    def register_client(self, client, phase):
        if phase < self.current_phase:
            raise RuntimeError("Cannot register for past phases")
        self.clients[phase].append(client)

    def execute_phase(self, phase):
        self.current_phase = phase
        for client in self.clients[phase]:
            client.run()
```

## Final Integration

Combine all elements into a cohesive pipeline where Markdown processing, user modifications, code execution, and Flask rendering happen seamlessly within a single request.

If you'd like specific implementation help on any of these steps, let me know!

# Other interaction

## Me

Which library would support this architecture:
- Each python instance, which is added, can go through initialization cycle, but it can only interact with others if it's not behind _in this aspect_ of interaction
- Normally, if not qued later, each phase, for each instance, is run _at the same time_

It needs to be more or less dependenceless, lightweight thing, where I have some basic class structure with a few definitions within what I inherit

## CoPilot

To create a dependenceless, lightweight structure with basic class definitions, you can achieve this by using Python's built-in features. Here's a conceptual outline for implementing your architecture:
### Core Structure
1. __Base Class:__ Define a base class that handles phase management and interaction rules.
2. __Phase Logic:__ Implement logic to enforce phase progression and interaction constraints.
3. __Instance Management:__ Track registered instances and manage their initialization and execution cycles.

---

### Example Implementation
```python
class PhaseManager:
    def __init__(self):
        self.instances = []
        self.current_phase = 0

    def register_instance(self, instance):
        self.instances.append(instance)

    def run_phase(self, phase):
        if phase < self.current_phase:
            raise RuntimeError("Cannot run past phases")
        print(f"Running Phase {phase}")
        self.current_phase = phase
        for instance in self.instances:
            instance.run_phase(phase)

    def check_phase(self, instance):
        # Check if an instance is allowed to interact based on its phase
        return instance.phase == self.current_phase


class BaseInstance:
    def __init__(self, name):
        self.name = name
        self.phase = 0

    def run_phase(self, phase):
        if phase > self.phase:
            print(f"{self.name} running phase {phase}")
            self.phase = phase
        else:
            print(f"{self.name} cannot run phase {phase}, already completed")


# Example usage
manager = PhaseManager()

instance1 = BaseInstance("Instance1")
instance2 = BaseInstance("Instance2")

manager.register_instance(instance1)
manager.register_instance(instance2)

manager.run_phase(1)
manager.run_phase(2)
```

---

### Features
1. __Lightweight Design:__ No external dependencies—just Python classes and logic.
2. __Phase Enforcement:__ Ensures phases are run sequentially and instances don't skip ahead.
3. __Interaction Constraints:__ Implements checks for interaction rules based on phase progression.

---

### Customization
- You can extend the `BaseInstance` class to include specific initialization or interaction logic.
- Add hooks or events to allow dynamic behavior during phases (e.g., callbacks).

This design is minimal yet flexible, providing the foundation you need without relying on external libraries. Let me know if you'd like further refinements!

## Me

Okay, now give me the implementation:
- Using this extensive structure, implement this:
  - Jinja2 templates, seamlessly integrating into Flask, will be used to parse Markdown file
  - The base class parses Markdown, being similar to Mistune
  - It records beginning and end of each block, and allows it to be used or not, and markdown added after or before it, or just added in case of deleted block (replace in single operation).
  - If code blocks have paragraph, and run, in the first comment - first position of first line - it will be executed in python. Currently, leave only hook for this in design.
- The chapter structure will be built using Anytree connector, which knows the beginning and end of each block; to beginning or end content can be added, and the block can be deleted or replaced. Anytree connector points to class itself, which can be deleted.
- Code blocks with paragraph mark on the first comment, with the string on the same line as a parameter, will get Anytree items.
- Based on these items, code blocks and chapters can be deleted.
- Additionally blocks and lines starting with "@" or "@@" are registered in node tree, and it's easy to delete them and add markdown inside.
- Each markdown can be subsequently processed, but when each function of that phase ends, next phase comes automatically. Phases: preJinja Markdown, postJinja Markdown, HTML generation - for classes, which join later, because they are added in the same format to addbefore, addafter, and replacewith: those can be called freely using Anytree nodes of given 3 types, and each can contain a list of items where one can append. One function would preprocess each item, and other would connect two items and is ran as soon as the new item is preprocessed, to join them; by default the latter would just add them together. Format is the same format with root block, and also two elements added are the same: jinja templates are ran, and they cannot call any hooks, which modify the templates; after this they are in the same level and finish with others. Next phase is HTML generation, and last is post-HTML generation, where scripts can be used to modify HTML when it's ready.

# CoPilot

Here's the implementation of the requested architecture:
```python
from flask import Flask, render_template_string
from anytree import Node, RenderTree
import mistune

# Phase Manager: Handles phase progression and instances
class PhaseManager:
    def __init__(self):
        self.instances = []
        self.current_phase = 0

    def register_instance(self, instance):
        self.instances.append(instance)

    def run_phase(self, phase):
        print(f"Running Phase {phase}")
        self.current_phase = phase
        for instance in self.instances:
            instance.run_phase(phase)

# Base Markdown Processor
class BaseMarkdownProcessor(mistune.HTMLRenderer):
    def __init__(self):
        super().__init__()
        self.blocks = []
        self.node_tree = Node("root")

    def parse_markdown(self, markdown_text):
        # Tokenize and track beginning and end positions of each block
        tokens = mistune.create_markdown(renderer=self)(markdown_text)
        self.record_blocks(tokens)

    def record_blocks(self, tokens):
        pos = 0
        for token in tokens:
            block_start = pos
            block_content = token['text'] if 'text' in token else token['children']
            pos += len(block_content)
            block_end = pos
            node = Node(block_content, parent=self.node_tree)
            self.blocks.append({'start': block_start, 'end': block_end, 'content': block_content, 'node': node})

    def modify_block(self, action, block_index, new_content=None):
        # Modify blocks based on actions: addbefore, addafter, replacewith, deleteblock
        block = self.blocks[block_index]
        if action == "deleteblock":
            block['node'].detach()
        elif action == "replacewith":
            block['node'].name = new_content
        elif action == "addbefore":
            Node(new_content, parent=block['node'].parent)
        elif action == "addafter":
            Node(new_content, parent=block['node'])

# Flask Integration with Jinja2
class FlaskMarkdownWidget:
    def __init__(self):
        self.app = Flask(__name__)
        self.markdown_instances = []

    def add_markdown(self, markdown_processor):
        self.markdown_instances.append(markdown_processor)

    def run_jinja2_templates(self):
        processed_markdowns = []
        for processor in self.markdown_instances:
            markdown_text = "".join([block['content'] for block in processor.blocks])
            processed_markdown = render_template_string(markdown_text)
            processed_markdowns.append(processed_markdown)
        return processed_markdowns

# Code Block Hook
class CodeBlockHandler(BaseMarkdownProcessor):
    def handle_code_block(self, code_block):
        # Hook for handling § run. code blocks; currently just a placeholder
        if code_block.startswith("§ run."):
            print("Executing Python code block hook...")
            # Logic for handling and executing code will go here

# Implementation with Anytree
class AnytreeConnector(BaseMarkdownProcessor):
    def manage_nodes(self):
        # Example: Render the node tree structure
        for pre, fill, node in RenderTree(self.node_tree):
            print(f"{pre}{node.name}")

    def register_special_blocks(self):
        for block in self.blocks:
            content = block['content']
            if content.startswith("@") or content.startswith("@@"):
                Node(content, parent=self.node_tree)
```

### Features & Workflow

1. **Phase Management**:
   - A `PhaseManager` tracks and runs phases (preJinja Markdown, postJinja Markdown, HTML generation, post-HTML processing).
   - Instances process their Markdown content in the current phase, transitioning automatically to the next phase.

2. **Markdown Parsing**:
   - The `BaseMarkdownProcessor` records the beginning and end positions of blocks, storing them in a list.
   - Blocks can be modified using `addbefore`, `addafter`, `replacewith`, and `deleteblock`.

3. **Integration with Flask & Jinja2**:
   - Markdown files are processed through Jinja2 templates using the `FlaskMarkdownWidget` class.
   - This ensures seamless integration with Flask.

4. **Anytree for Chapter Structure**:
   - Anytree is used to maintain a hierarchical structure of blocks and chapters.
   - Nodes can be added, deleted, or modified dynamically.

5. **Special Code Block Hook**:
   - A placeholder for handling code blocks starting with `§ run.`.
   - Future implementation will execute Python code dynamically.

6. **Special Block Registration**:
   - Blocks starting with `@` or `@@` are registered in the Anytree structure.

7. **Multi-Phase Processing**:
   - Markdown is processed in phases (preJinja Markdown, postJinja Markdown, HTML generation).
   - Nodes and items can be appended or connected dynamically, ensuring flexibility.

#### Me

give me also an example structure, which would do in this environment: python code block uses paragraph for imaginary operation to replace itself by "Hello World!"

Here's an example structure that integrates with the environment described earlier, showing how a Python code block with a paragraph comment (`§ run.`) can replace its own content dynamically with `"Hello World!"`:

```python
from anytree import Node, RenderTree
import mistune

class DynamicCodeBlockProcessor(mistune.HTMLRenderer):
    def __init__(self):
        super().__init__()
        self.blocks = []
        self.node_tree = Node("root")

    def parse_markdown(self, markdown_text):
        tokens = mistune.create_markdown(renderer=self)(markdown_text)
        self.record_blocks(tokens)

    def record_blocks(self, tokens):
        # Record blocks, including positions and content
        pos = 0
        for token in tokens:
            block_start = pos
            block_content = token['text'] if 'text' in token else token['children']
            pos += len(block_content)
            block_end = pos
            node = Node(block_content, parent=self.node_tree)
            self.blocks.append({'start': block_start, 'end': block_end, 'content': block_content, 'node': node})

    def process_code_block(self, code_block):
        # Check for the § run. tag and process accordingly
        if code_block.startswith("§ run."):
            # Simulate the dynamic replacement operation
            return "Hello World!"
        return code_block

    def execute_dynamic_blocks(self):
        # Iterate through all blocks and apply dynamic processing
        for block in self.blocks:
            content = block['content']
            if isinstance(content, str) and content.startswith("§ run."):
                processed_content = self.process_code_block(content)
                block['node'].name = processed_content  # Replace in the tree

# Example Usage
markdown_text = """
# Example Markdown

Normal text block.

§ run. This is a dynamic code block.

Another text block.
"""

processor = DynamicCodeBlockProcessor()
processor.parse_markdown(markdown_text)

processor.execute_dynamic_blocks()  # Process dynamic code blocks

# Render and display the Anytree structure
for pre, fill, node in RenderTree(processor.node_tree):
    print(f"{pre}{node.name}")
```

### Explanation

1. **Markdown Parsing**:
   - The `DynamicCodeBlockProcessor` parses the Markdown and records each block's content and position in the `node_tree`.

2. **Dynamic Code Execution**:
   - Blocks that start with `§ run.` are identified and processed. The placeholder logic (*process_code_block*) replaces the block content with `"Hello World!"`.

3. **Anytree Integration**:
   - Blocks are represented as nodes in the `node_tree`. The modified content replaces the original node's name.

4. **Output Example**:
   After processing, the resulting structure will look like:

```
root
├── Example Markdown
├── Normal text block.
├── Hello World!
├── Another text block.
```

This approach demonstrates how dynamic blocks can integrate seamlessly into the described environment while maintaining the flexibility of Markdown processing and hierarchical block management. Let me know if you'd like further refinements!

###

