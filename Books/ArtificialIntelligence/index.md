# ♗ Laegna A.I.

## Open Database

An A.I. must keep synchronized copies of it's history, where we utilize git:
- It creates a Git subbranch and commits in the database, where some models, being files under the same name, with some given hashtag of identity kept with them or restored, and each branch will get the docs up to date and have both it's input set (which can restore it's history) and possible cache of it's output, which would remain even if the sources are lost to the pages of history. Based on lost sources, it can also update to be regenerable.
- Updates to sources are added with dependency version updates: each source is a dependency, with either source or the permanent cache of it being available, with the source moment of time.
- We utilize Git, because training is expensive work and finally, we end up with our models being committed somewhere. Embeddings, their simplifications, AI generated lesson cards - everything is important. It's either the work of Spiders, which utilize user processor to do active work and commit to rather their personal Gits, or users, who run weeks of optimizations and commit to GitHub.

## Ponegative Containers

Ponegative container is able to track space and time through ponegative values: those are very extensible and scope can be raised.

### Space and Time

The Space is static, and it's contained in such structure:

Spatial Variables {
    Time: integer
    Id <minus> Time: unique integer
    TimeHash: integer
}

I use "<" and ">" for operators one for backwards and other for forewards effect of reasoning. Each operator made of letters and special symbols can be beautified like this, while for letter-made operators this is obligatory. Operators do not have any priorities each over another.

Function "minus"