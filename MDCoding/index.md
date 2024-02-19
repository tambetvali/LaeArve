# Coding

Code can be generated from documents and while the AI's I'm struggling with cannot finish the projects alone, rather the documentation contains the code and the code is to be changed by AI. For example, while we have some implementation now, it would be easy to implement it in C++ or any other language in the future, using mostly the AI.

## Coding Documentation

We do not depend on code, which is rather the free variable in hands of an AI, instead we put more important code into the documentation, such as:
- The essential working of the modules.
- The actual standards by which the mathematical functions and classes are generated.

We do not use math algorithms, but in each case, we use code - even for proofs. This is for programmers, not for mathematicians alone, and thus we utilize Python, being programmer-free in choice of language.

If the implementation is not depending on it, mathematical books and standards are welcome, especially as forks of the system, which would interlink and provide external documents.

### Algorithms

There can be algorithms described, referring to the documents, about how to generate the code step by step.

Current AI with very limited window size would be given the tasks, in order, to fulfill each step of the algorithm, possibly modifying some input or algorithm itself.

### Essentials

- Code is often written in minimalistic version into documents.
- - It contains only the bare-bones, but full functionality is accepted in sense: this is covered by the word "essential".
- - While implementations might differ, the practical or theoretical part, for example the exact mathematical algorithm to do a conversation, will be implemented in working Python.
- - The parts, which are rather needed to make the code and the system work, not to understand it, is described in the documents.

### Code

Code can be added to code tree, but it will be better reverse-engineered by others into a documentation, which can produce equivalent code and it's invariants.

Documentation can contain question-answer pairs, where the original code is produced by some question, and where this looks realistic; this production is as more advanced as more essential and elegant is the document.

## Implementation

Given that while there is good formalization, nowadays AI would not produce the efficient code alone, unless perhaps we find some large and smart model. In our case, we fake the case of the code being documented from documentation, but we leave it *technically possible*, where one can not tell this plainly by inspecting the documentation and the nature of an AI, but they must also know how powerful AIs are exactly available to us.

## Configuration

Configuration flags will be added to generate different versions of the code, for example for having C++ generation properly implemented, we would either include C++ example code, Q&A pairs and implementations in Documentation folders (C++ subfolders) or C++ branches (where Python documentation is an accessible subfolder, if it has any meaning in regards to creator of such library or fork, unless they do a different structure of Documentation or even a different idea, such as handwork / manual implementation for efficiency, studies or experience).