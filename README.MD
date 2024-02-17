# Laegna Math Studies - what is this about?
Form of this text: talking in present form, I speak about future. This is the recommendation that we don't change time forms in each document after each iteration, rather we won't even find them properly.

This is *to teach an AI some math*, where this document describes this and similar sentence, not related to having my own AI but teaching an AI of another, unknown person or at least in different project.

For next confusion, which appeared: Laegna Math System *itself* is not available and it's not a documentation of it, but we are *developing* it. We are developing a generator of math puzzles, and a Spider to fetch the data - the Spider provides Q&A as Python class, object, or for example tuple, and this is where our mission ends - Laegna system itself is what we *do* develop, and it's based on mathematics invented by me (the author of this document, Tambet Väli) and hopefully in future, also by others who like my ideas and theorems and develop consistent math, or simplify, extend, import and more deeply understand the classical math; including the ones who solve open problems of Laegna (for example, where I sometimes see theoretical solutions or rather partial theoretical solutions: the problem remains open, what is the proper numerical technique giving actual numbers for numbers, to do addition and multiplication *at the same time*, where I cannot imagine the whole solution at the same time, or the whole solution, but on the other hand it would resolve several things I am inventing; I think I have intuitively seen the answer a few times - but those, who implement different solutions with practical number solutions, especially in concrete form; they might be based on different approaches, where even the U approach of proving some solutions to be outside of the problem scope, such as where 2+2 and 2*2 map to certain solution, it can be easily deduced that 1+3 and 1\*3 are not equal solutions).

The trained AI is absolutely necessary, but my scope is: many people are able to train AI's, and they would even conclude to architectures, which could best fit Laegna, or they would include Laegna Knowledge Base - but there are not many people who would be able to do my math, given that the problems were not solved in the history.

## What is this system?
My Code Assistant (an AI indeed, not a person) was not able to understand precisely, what I want to achieve - I have quite a small model of CodeLlama, running on my average computer, and it's far from GPT-3 in this sense. I write this extremely short and clear for my AI to understand with classical math examples.

I have my own math to teach, and it will be open and public system, which I improve over time. This document makes examples based on classical math. I am *not* creating an AI itself, which would learn math, nor anything generative in AI terms - all I do is simple lists and iterators, some of them static and some of them dynamic.

## My client system - this is not mine, but the user of my website can create this in CoLab or Hugging Face or wherever they want.

Imagine an AI, which is learning math:
- It will need math cards with tasks such as 1+2=3, maybe false posetives such as 1+2=4 to get negative feedback.
- It will benefit from automatic system, which generates:
-- Q&A: For example Json file, where Q equals 1+2 and A equals 3
-- Q&A&D: For example Json file, where Q equals Pi and A equals 3.14 and D (Doc) equals "2 digits"; it will reason that it needs 2 digits after comma to make sense of the cryptic D, which will improve it's heuristics.
-- D: Only a document: D equals "Pi=3.14 with 2 digit preciseness". Negative example can include unethical sentence or notice that certain math formula just looks like something perverse, (UU) could resemble certain part of body of woman for example and while we need it, perhaps not in the banner of politician.

## My own system - this is what we are going to make, and this will help the client AI to learn, despite it's not our own; perhaps we only include one simple example AI at some point of time.

I agree that the following is possible:
- My system might include some AI code, but this is not related to it's main functionality.
- My questions regarding to building AI systems are not about this system.
- My code tree might, in future, contain simple AI such as one which would learn to be a basic calculator, able to understand "1+2" and answer "3". This is for testing and fun, not essential part of it in sense of being ambitious to build a best AI inside this project.
- My documentation might, in future, include how to set up an AI.
- It will include documents and example code for doing so:
-- Documents would be rather for others, and they are not documentation of this project.
-- The example code reads my web page, and generates question answer pairs, documents, or question answer pairs related to context in a document. This is a *driver* or *client* of this project, and another person, inside another project, would benefit from this. They will understand, how my Json is structured and for them, this is the most trivial part of their task, it's only related to reading my code tree.

## Driver module

My website has a structured documentation, and it will be:
- Static documents, such as dictionary items. For example, a document could statically contain information that 1+2=3 on a single line. This is directly fed to the user.
- Dynamic lists, but static in content. For example, it might generate a, b and c, each iterate over 1 to 10; it would contain table items with columns a, b and c; and additional column stating whether a+b=c is correct or incorrect in context of this row; for example that 4+2=3 is incorrect, thus a=4, b=2 and c=3 in grouped into question gives answer=False.
- Dynamic pages or "cards", such as big number + big number = their sum, a big number. This is because I cannot iterate over big numbers. My system does not learn those numbers, but it's work is as trivial as addition, in a sense - in this sense that it's generated, using static algorithms and not learnt by an AI from bunch of examples. It does not learn from bunch of examples, but it *is* a bunch of examples.

Given this:
- It accepts requests, which ask for a card of knowledge.
- It generates the card in it's own standard format.

Now, it *does* contain the code to make such requests itself, but it *does not* depend on them in any way. Rather, the user is supposed to take this code, as it is, copy into CoLab, where they have their AI model, and possibly combine with other sources of information. From this *driver* or *user* code, the Spyder, my user and not myself (at least directly, while I might benefit from user base or being famous, or I might train a bot myself, but then I am my user and not developer of this system, and this is a different context than the one used to generate any code here - I write most of the math code, but AI Assistant would work mostly with Flask, the website, and finding me documentations and imports) will benefit. Definitely I use it to: fetch my content with Spyder - well it's name is similar to existing one, but it's also not my trademark but a fancy word a little ironic in this context -, generate the Q&A pairs for an AI: but this is where it stops; I am happy with this - the user will take my Json output, with Q&A, and feed it to *their own* AI, thus an AI is not the development task of this project, but rather a bigger framework where it belongs to.

## Concrete example

Our user: opens CoLab account, downloads an AI model, and copy-pastes code to train this AI.
Our user: they write this code: [for a in infinity: ai.fit(training_data_item)], where infinity might be following: [def infinity():\lf while True:\lf  yield get_random_item_from_database()].
Our user: they create a function: get_random_item_from_database() with description: from database of columns ("Q": string, "A": string) fetch random item and return it as it is.
Our system: has a web page, which is able to return something in form of ("Q": string, "A": string) indefinitely. Let's say the page http://laegna.math/?Q=1&A=1&D=0 would return Json in form of containing 10 objects, where there is an object called "Question" and an object called "Answer".
Our system: while it's based on mathematics, for example generating things in form a+b=c such as 1+2=3 is trivial and does not take an AI, to generalize and study this, and to creatively use that fact, takes an AI. Thus, in the "Spyder", we need this class: fetch the Q&A from our system, and let them to create their object in form ("Q": string, "A": string).
Our task: while our user might be really competent in their equivalent of ("Q": string, "A": string), and how to feed it to their AI, and they might have an AI readily made, they are not so competent in how our Json is structured and where to find them on our website. For this, we also create a very simple script which, while it could have access to our codebase and we easily use this, to import some files, but not the whole system, the user would rather be happy if they have some standard prefix code such as "Laegna.init()" and then they have the function with a return value: ("Question": string, "Answer": string); here, they would be programmers and for them, it's now trivial to replace "Question" with "Q" and "Answer" with "A" - now they have unlimited number of our cards, and they can use them as easily as the files in their hard drive or web-based drive.
The user: is now happily using Laegna math to understand my webpage, where while sometimes I write something either poetic or cryptic, using my own number system: but now they can ask their AI, finally, how much is something like "1+2" _in my math_, and this is step closer to doing innovations based on it.