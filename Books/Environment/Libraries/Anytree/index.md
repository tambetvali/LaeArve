# Anytree

We are going to build treelike structures around Markdown preprocessor document, which has a raw structure into it's blocks.

To make it more versatile: we use Anytree to create chapter structures and other important structures, where it's going to like to elements in the original structure and we can create backlinks to store our constructs - but it's outside providing you a tree on it's own, for example the actual structure of titles.

- We do not touch the Markdown's blocks for preprocessing, as it depends on it in how to produce the output: and it's aligned with subdocuments and nested documents, creating a heavy scope.
  - Here, we use Anytree: we build tree of, for example, the logical chapter structure, and each node in the structure will also know it's object in Markdown preprocessor.

- [Any Python Tree Data](https://anytree.readthedocs.io/en/latest/): Simple, lightweight and extensible [Tree](https://en.wikipedia.org/wiki/Tree_(abstract_data_type)) data structure.
