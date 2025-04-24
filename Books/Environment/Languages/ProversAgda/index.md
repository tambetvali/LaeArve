# Agda Prover

From Agda Manual:

> Agda is a dependently typed programming language. It is an extension of Martin-Löf’s type theory and is the latest in the tradition of languages developed in the programming logic group at Chalmers. Other languages in this tradition are Alf, Alfa, Agda 1, Cayenne. Some other loosely related languages are Coq, Epigram, and Idris.

> Because of strong typing and dependent types, Agda can be used as a proof assistant, allowing to prove mathematical theorems (in a constructive setting) and to run such proofs as algorithms.

This means: while we could try proofs with Isabelle and Coq, which are powerful general purpose provers, I set Agda as a standard for what we are going to do here:
- Programmer friendly: this is a programming language and prover in one package, which means the language resembles a programming language.
- Proofs can be used as algorithms, which means we can create some mathematical types or implementations alongside with their proofs.
