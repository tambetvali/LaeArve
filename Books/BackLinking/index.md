# BackLinking

You can structure Markdown titles like this:

## Main title

#### It's personal subtitle (internal)

### The actual subtitle of it (external)

Folders are ordered, thus they behave the same way:
- Empty folders are not considered as parts of the tree
- Thus, upwards-linking can be formed.

For example, consider you want to add your own set of cards to current folder, not messing with next folder below; you assign _under_ your parent folder, but also _under_ it's child folder. This is a struct, which can be of nested use.

In HTML, to keep it nice, let's write /fold4/ to fold the folder 4 times inwards, because we can have keywords and several empty parts in url are not nice. So we got some reserved words or keywords, like programmers are used to say.

# Backlinking is mathematically complex piece, but it allows you to structure your documents, without necessarily breaking compliance with HTML or Markdown: while they don't understand your syntax, they won't complain. That's perfect for us as we are going to link into two directions: forward and backwards, to allow internal study cards for chapters for example, which do not span over rest of the content.

Backlinking is the easiest way to allow for multidimensional: expansive; trees in the file system and documentation. Initially we want to implement the whole piece in docs; later in the filesystem access - each folder can be marked as "backwards", and each connected list of "backwards" elements are reversed in index, in relation to their position: folder positions are referred in such way.
