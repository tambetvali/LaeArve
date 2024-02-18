# Philosophy of Code

## Multiple Classes in the Same File

Put multiple classes into the same file to keep code tree short - instead of searching inside the file, you would need to search in the file tree.

I would keep this project rather flat and small - indeed, whoever wants can refactor it to be more structured and accross multiple folders; in fact you could refactor it in any way.

## It's not going to be overoptimized

In regards to current iteration, next iterations, iterations in the future:
- There is a goal, that whoever would implement this in C++, Go, even Prolog or languages of different features of speed, symbolic math, proving etc., should be able to extract the necessary bits here very well. We are not going to make clever construcs, such as what I do in multiple classes could be possibly done with a few bytes somewhere; or where I have multiple flags one could just cancel another. The logic behind needs to be visible:
- - There are types of people, who would like to reverse-engineer and follow the logic into it's depth. The code here is supposed to be open source and thus not compiled, either manually or automatically. Python, on it's own, supports rather this paradigm and talking about such optimizations - programmers of C++, C are just eager for this and somebody possibly writes a cryptic one-liner, which would do something like parsing the whole Laegna number binary system into decimals in one go; however, there are only a couple of people, who know what these one-liners actually do.
- - There are also types of people, who like such reverse-engineering documents and who perhaps know even fancier languages than C++ in this sense, for example Assembler - with Assembler, specific to some very powerful processor type, they would make use of specific processor, specific environment like amount of memory, and they would be able to write a driver for specific use case, such as cleverly load-balancing between processor and video card of given types. Finally it's burnt into iron so that those devices load this in a moment from ultrafast memory - from this point on, you have specifically nothing to do with this.

# We are looking for balance and mathematical coherence

The number of combinations the elegant Laegna Math would do with large numbers and scopes is impressive, and where decimal system would do it infinitely long, sometimes in Laegna it's trivial - there are operations in Laegna math, which simply take no operation at all, for example Fourier transform is straightforward, trivial, and could result the same number you gave as input, as it's ouput, where finally you don't have any operations but only the paradigm.

Compare to Python: in certain cases, your code is so simple that it simply does nothing.