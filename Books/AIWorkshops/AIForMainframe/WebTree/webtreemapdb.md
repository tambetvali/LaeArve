# CoPilot Task

Notice it did not work on first try: it had to fix the package address. Indeed, if you get errors, give them back to your AI.

## Task

(given after webtreemap's task)

tvali@PC366:~/LaeArve$ sudo systemctl start mongod
[sudo] password for tvali: 
Failed to start mongod.service: Unit mongod.service not found.
tvali@PC366:~/LaeArve$ 

Can you write bash file, which asks to install or get status of mongodb and properly connects it to project file, webtreemap.py in the current folder; it has Markdown in comments: surrounded by markdown code, which explains it's content and is written to bash full-line comments and blocks.

## Attach

Well include "how to run" as first part of it; also the markdown is not in code block inside: whole this type of comments is markdown, and the python code instead would appear as code block, automatically in parser.