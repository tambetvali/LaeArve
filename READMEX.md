# Laegna Math Website: Project Scope.

The Laegna Math Website is an effort to:
- Create a consistent set of standards to teach new theories to an AI.
  - AI would learn the work based on old theories more easily.
  - It could be used to teach theories to an AI by fine-tuning; in case you need it, you rather have something rather new to your model.
- Work out:
  - Implementation plans for different purposes, where each component or implementation is rather a "might".

My use of programming languages:
- I want to use them as templates for language, for example this process:
  - Create a very strict standard of code lines for your intent.
    - For example create a basic class to implement such intents, for example to add studycards (.addCard(Q, A)).
    - Define a template for code: if code contains only these structures in this order, it's safe for your code.
    - You can define a parser for your subset, or use original language implementations.
    - For example, imperative language expresses algorithms, logical language expresses logic, symbol math language expresses mathematics.

## Programming languages

### Programming Languages Introduction

For each language here:
- It's very welcome if modules are developed to make them directly support Laegna numbers and if referenced, more elements of Laegna.
- Initially, we need to create these implementations or one of them:
  - 0l or other code based Laegna impl: 0 starts number, l is laegna type, for example 0lAAA would be AAA. This for languages, where hex is implemented this way - you should follow the rules of implementing hex as "h", and use rather the letter "l".
    - Supports complete Laegna implementation.
  - Decimal-based implementation, where U is added as generic letter, and rest of Laegna numbers are encoded to common decimal format: 1-4 for i-e, 5-8 for I-E, and if capitalization is not used 1-4 for I-E, 5-8 for À-Ó (from down-accented A to up-accented O, which gives half of both higher and lower octave, a freedom in number space).
    - Supports Higer Laegna Fantasy.
  - Decimal-based implementation is a bonus, where numbers are always added in order of size: for example, for À-I-E-Ó could be in order from 1 to 8, where U and V are at 0 and 9.
    - Supports Lower Laegna Fantasy, the first thing to implement perhaps if you are going to prepare implementation of Laegna Math Webpage of \<your name\>.

I use very basic standards, mainly:
- UTF8
- Markdown
- Programming Languages
- HTML, DHTML and Json

HTML in my terms: readable, open source HTML. Carefully simplistic use of dynamics.

DHTML: using Javascript, for example text box not visible in source.

### Programming Languages: Python

We use Python in several ways:
- As a programming language of our Systems.
- As a template language for our Scripts.

Scripts are code snippets, which:
- Follow a strict standard, such as only initializing a class and adding members.
- Non-programmers can learn these special cases of syntax, where semantic structure rather follows standard human understanding: for example "addFood(\<foodname\>)" would be understandable, as everybody plays some encoding or encrypting games.
- Rather complex programs are complex, than simple ones.

We use Python in such way:
- We build systems in it.

We use Python _Scripts_ (our website term) in such way:
- We define subsets of Python, which are qualified for the need; like we use Json for data (from Javascript), we could use Python for semantic meaning.

Still, we can use other formats such as CSV and convert something automatically to Python _Script_.

Each Template follows safety rules and thus there might be metatemplates, which also require some rather manual (where advanced AI would be kind of "manual" as well) verification of code.

### Programming Languages: Laegna

I am creating this about Laegna Family of Languages:
- Efficient coding and implementation strategies.
- Semantic analysis of possible structures and buildings.
- Example syntaxes joining several semantics together.

This is currenly rather an imaginary language, but we can utilize the minus-iterations (strating from I, the minus infinity) of ideas.

My key concern is to include the developments and possibilities of Laegna Language directly to programming language theory, and implement some close examples.

#### Generating code and execution output: the Q & A - for programs.

I believe that we can generate a lot when teaching AI.
- Generative materials lack originality and they repeat the same results. For this, we add a special hash tag to the generated materials: such as #automation, where the AI would learn this content, and how to relate it to it's parsing of the real content, which does not have such tag. _User_ is not an automation and does not have this tag.
- Some generative content can have systematic lack of style or mistakes. Given we have hashed it properly, the AI would learn it under this hash, and based on other examples, consider how this relates to the actual content.
  - Fixes could be given: for example, cards with systematic bias, and a number of human-made cards to fix a number of those biases under more proper tag.
