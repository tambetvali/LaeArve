# Some class and function ideas:

Note: probably I will write more clear content about those topics some day.

A class should be a template, but also for a given instance: it should be it's whole range.

Then, to be sure in this, we can also call them templates and not classes: we can create a template for a given instance class.

Template A:
  Number n
  Den X
  Ten Y
  Local:
    id id: autoincrement int

Where these classes have their templates in uppercase starting names.
I don't follow Python convention here, where Classes as metaentities are with
capital, while def and trm are small-case.

Class a:
  den x
  ten y

Template behaves like:
- A normal SQL table, where one should be able to do SQL queries.
- When it's metastate is changed from "memory" to "disk", and filename is given in the same operation where there was memory space (some index).
- Template would be generated from class if it just needs all variables, types and names in capital.

Parent classes could be free: to id it, parent class autoincrement int could be added, for this template to parse that class. This way, id could be any type.

Function of a template is to have a common structure for the data: for example, if template A uses id to give it's members as a list, local data could be added to have an id field. Id numbers would be mixed to get the template id, which could contain first bit of each in order, second bit in order and so on.

I need it for this:
- each a contains single components of the data structure.
- with same case non-sensitive name, for instance, the classes and variables can be easily connected, where they could be given numbers or other variables [0], [1], as in Den[0] connected to den[0].
  - The list content should be reflected, and each id field reflects it's member: if it's deleted from table, it actually exists until the last id is deleted, where the status is also visible for a class, which still holds an instance, and which could do it's work without noticing, like an update of news text moment after delete, or it could just return with job-done value and stop it's expensive calculation by this.
  - The list could contain hard reference or soft reference, where any of the classes would need to hold the key to access the element, and when there are no keys: the element is deleted. For example if parent is deleted, the operations-going-on, which were started with this key, are still working, but as they can verify: as soon as they finish, the element is probably deleted; they have actual chance to restore it, so the boolean as well should carry the identity of it's value and not finish the job before it's done in regards to last value. Keys are thread-safe and we can choose other track, in case of failure, unless we already commited some output after the breaking point, which would differ in any way from the "proven" output of the other track; where if it's an estimation, it's nature is to improve: but it's still the same variable unless the container is like this as well; or it's the value of new history, which confirms that it really could override the old and move it to drop-down history of parent chapter, which I mark as before-titles in Markdown being more indented, than where the list actually starts, which is the least indented subsequent chapter name. So we can use third-level chapters to leave room for added content to be first subchapter, and end of itself being probably garbage collected.


Why I need this:
- Each component, which is bitwise visible in digits, are same way visible in sentences; there needs to be possibility of parallel tracks to follow and this is the easy implementation. Numbers themselves could be generalized to higher-level components in order: same template or class from a pair would be used for selections, where some instances might have parents of subsets of classes with more Templates.

Classes and templates could be instantiated into local variables before use:
- If global variables are used, class and templates would be global tables with each instance.
- If class a is given a local variable la, it would also generate the same kind of members, but could be applied local changes.
- If it's initialized, new child class is also associated with a variable, and in each time when this value is assigned to other variables, child classes are applied, but they are empty and very simple structures, even lazy to appear dynamically. New methods and variables could be added to child or template.
- Template could be initialized for class for subranges of the variables, and the same template used for other class using the same template, but now contains the next level, but still the same dimensions.
  - Dimensions could have also some precision or raster, where each group of several digits is used for operations.
  - Templates should allow for use of trees and other structures: perhaps it could be sometimes assigned bitwise basis, which means for each Ten digit separately with template index. Other times, for whole Class structure: if b = a, class for a is copied into b and B would appear as template, if some AI or logic would use capital names automatically. Bit properties could be changed by class, it could also be denoted by "#" is capitals are used for other purposes: but class would attach on first level, family, then subspecies, then class, but finally a group of values together. "#a" could be used for template of a, but "~a" for class of a.

Ways to implement:

Let's use "Data" for "object", because in AI we use "Datasets".

Data a {
    a, b: integer
}

Apply a list of 50 members to a, creating a subclass #[a]a, where "#" means class and the inside "a" is remembered as original name of the axe. pointer(#[a = 20]a) would turn a into pointer of that index. Multidimensional structures could leave dynamic sets of variables, and could be read sequentially: dimension names or chapters coming in between; generally let's make everything also markdown-encoded in this sense, where data is created in code block or outside Markdown comment.

Here we assign superposition, i.e. being indexed from outside container to a (notice second "." has whitespace after it, so it ends the sentence and does not create a branch or node of object tree).

[list[50] a]a.c.

Instead of templates, [Any i]a.c would map to any element with index i, and thus the range. (i)a.c would map to certain element, where [] would also give a structure of something, where () gives the something itself. [Any i < 7 ** Any i > 5] would give an array of element at position 6 or an empty array, if there is nothing.

Class can be defined in such way:

Define term C

trm C(a, i):
  [Any i]a.c

As i, a and c are known, term maps to their instances, and reflects the mapping to inherited dictionaries, where a as a whole is assigned to something, where class tree is inherited: #a is class of a, which can be changed dynamically and switched when used on "self" in function calls. "#", then, allows to use something as a class: when Matrix or Vector is value of the class, the object itself would have a function call of multiplication of matrix or vector. It could be code object or data object or AI method, or a combination.

C has a parameter i, which is mapped to the index i, and parameter a, which is the object. Class objects will be in tuple before the name of something, and terms would semantically unite them into objects with given input. It can be called once with constructor, it's function - functions, also, are defined that way and give output of subclass type of themselves, later allowing controller calls.

(C).fun1(a, b, c):
  pass

Would now define function on C: same way, variables, classes, terms and definitions (functions) can be given, or other classes inside. Everything is a variable and to given class, variables could be defined instantly.

Also in private spaces, more terms could be defined, and some APIs made public.

# Class Keys

Keys:

Class names can be forwarded as keys, where instances can be created.

All kinds of restrictions can be applied to keys.

Virtual environments: when executed in condition, which does not have keys to the system, for example client-side code could be executed.
