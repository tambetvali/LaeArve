# Markdown preformatting

Initial markdowns act a little bit like templates or widgets.

## Code preexecution

__Preprocessor directives__: Code, which starts with paragraph mark
in comment, such as "#§ ..." is meant to be executed by given rules
in the preprocessor, where it can hide it's own block and replace
it with a generator, or where inline code can replace themselves
with result of a function call.

__Code block preprocessor directives__: Code blocks with #§ at the
first line, such as "#§ Generator" would use specific method and
run the file, with input such as: "#§ Generator: template=math".

__Inline preprocessor directives__: Inline code with § at the
beginning would execute the given function and expect string as
a resuls. The string would replace the code part, so that if you
write `§L("A")`, the function "L" from it's own import would be
executed, and for example it could properly format and print the
Laegna Number "A".

## Document nesting and referencing

__Document Nesting__: Another document can be nested, like with
"include" or "import" in programming languages. It's then either a
chapter, part of the document; a subdocument, which opens from the
reference link, or a nested document, which would be added to the
end with content index added to the point, where it was nested.

__Referencing__: Another document in another book can be referenced,
in which case it's special.

## Theorems, callouts, important blocks

Blocks with "> " format, quotes, can be added an icon lamp from utf-8,
turning it into a very special theorem. The special theorem can appear
multiple times, and while slightly different names can be added, we
will work on the intelligence to see them as same theorem (without
making it strict).

## Dictionary items and reference targets

Blocks with underscore italic, but not asterisk italic, _mention_ the
thing in _italic_, thus where the mentioned thing is a context, they
are candidates to be listed.

Blocks with undercore bold, but not asterisk bold, _define_ that term or
_define_, how we are going to use it; they can also _introcuce_ it,
stating it's a special term in this context - in such case, it would
also be included to definitions list, because it defines a specific
use or introduces to specific group.

_Blocks with underscore bold and colon after it_ turn the following
block into dictionary item (usually one paragraph) or if followed by
paragraph break, into an encyclopedia definition. We do not deny
long dictionary items, because given target can specifically only
use the short ones. Encyclopedia pages take the whole page: the item
continues, until the given chapter is over, and subchapters are added
as a book or reference list (giving the card to an AI, it can follow
the references or they would be taught separately, possibly under
the same session).

_Inline dictionary items_ are using the sentence after colon as it's
definition, where the bold before the colon is a term. If used inline,
certain exceptions might be made: if the parent paragraphs can be
semantically proper, when some part of the sentence such as comment
in braces before is used, that part is not part of the definition.

_Repetition of dictionary items and reference targets_: if the same
item is repeated, an AI would gain, because it would be able to figure
out different wordings for the same sentence, and generate new
dictionary items for the term and for special cases.

_The @ symbol_: when in the beginning of dictionary item is another
item with @ symbol, it will be used instead; if the local item contains
also some information about specific use of the term, one would try
to connect them. When feeding to an AI, the term could be uncompressed
and directly included.

_Underscore bold with colon after it, used inline_ creates a dictionary
item, using only this sentence. The paragraph, where it is, would be
used as a context and there it presumably, obviously holds as it was
defined, in an example.

_Blocks with underscore and ">" after it_ are used 