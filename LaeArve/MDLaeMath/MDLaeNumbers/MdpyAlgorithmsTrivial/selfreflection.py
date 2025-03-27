
sr_markdown = None
sr_verbose = False
sr_content = []

def init(Markdown):
        global sr_markdown
        markdown = None

def verb(verbose = False):
        global sr_verbose
        sr_verbose = verbose

with open('output.md', 'w') as f:
        # Write the first subchapter and all examples in it
        f.write("### First Chapter\n\n".join(["Example {index}".format(index=1) for index in range(3)]))
        f.write("\n\n## Subpage 1 Example\n")
