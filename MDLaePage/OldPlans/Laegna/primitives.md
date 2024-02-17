# Laegna Primitives

Laegna Assembler is the name for my assembler, which I plan to create, and Laegna is the name for my own mathematical and logical work.

## Code orders

Code is written in sentences, and the sentences have punctuation.

Sentance! - this, with exclamation mark, will send the information backwards in time.
Sentence? - this, with question mark, will run an assert (or create a code block for "if" statement).
Sentence. - this, with a dot, runs a logical value.

Also:
Variable = Variable. - this is with dot.
Variable := Variable. - this is with dot, but ":" before "=" turns it into exclamation.
Variable ?= Variable. - "?" before dot is another way to express question.

This also simplifies having no punctuation in some version of the language, which supports code lines without punctuation, but we won't need this in Assembler, which is not very AI.

## Functions and classes

Code block forms a class:

{
    Code inside.
}.

It has punctuation mark at the end, as it's also a class.

Class will be put into indefinite loop, but unless it's declared as a loop, the program will try to reach an ending condition. Once the output value is not altered, it will finish.

{
    Return.
}.

{
    Return x, y, z.
}.

Return will stop the function part of the class, which is initially run, and start with the class.

Input for the function, or constructor for the class, is asked in the following way:
test = (a, b, c) {

}.

For a subclass or subfunction, it's written as tree element:

a.test = (a, b, c) {

}.

This will set something referenced as "a" to have function or class property with inputs a, b, c, so that one could do:
a.test(1, 2, 3).

# Simplifications and logic

"&" declares symbols, which synchronizes given elements for every connection they are used in. For function input it's better to use symbols.
&a, b.

a + b = 4 {
    # Inside, a multitude of connections can be declared:

    iseven(a + b): =True.
}

"=True" would set the current code block named value into "True".

iseven(a + b): - sentences, which end with colons, will define code blocks; .