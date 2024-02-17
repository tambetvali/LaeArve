# Conversation about simplified Iteration 1 plan

## My set of a Goal

Okay I contemplated on why you don't want to generate code. I decided that my initial implementation was too complex and you cannot refactor that properly, so I moved it to folder "Old" - @Git Diff

@iter1_app.md - Application.

@iter1_cards.md - Cards

@iter1_luicanvas.md - canvas

@iter1_luichapters.md - chapters

@iter1_luipages.md - pages

@iter1_luiparams.md - params

You should also account for @Codebase.

Your task now:

- We are going to create an implementation plan.

- Analyze, until you find the basic ideas.

- It should be simpler now, if it's not, it's supposed to be so work on KISS where I failed.

- We are going to create an implementation plan for the UI, and rather don't care about the existing code as more than inspiration - we implemented it in short time and we can copy-paste what works, back to project.

From diff you see what changed, and what went simpler. Folder "Old" is the old version.

Create:

- Iteration plan for 1st iteration

- You generate code 3 or 4 times for this, and I check every time. Consider you are very expensive - on my computer like 1 hour waiting for answer, and still we have to finish in 4-5 hours because for monday, in 2-3 days, I want the initial version to be ready, generating some basic Laegna numbers with minimalistically functional interface for AI and preferrably human as well.

Now see also how to implement widgets, but given that I work on numbers - think deeply of UI, of cards, of Flask; also what happens with my number generator later - now it's bunch of classes, but mostly to define not yet to generate or work with numbers; try to imagine what it will be later, for example the number types Den, Ten, Tene, Tenet.

## AI implementation of the Goal
This, now, should be important not to forget, because with forgetting comes my inability to express, and AI's inability to understand it's own old code structures or decisions - rather, having something written down would make it clear and consistent.

### The AI answer

The task at hand is to create an implementation plan for a web application that generates mathematical training materials for an AI model, specifically for infinities. The existing code base consists of 5 files: iter1_app.md, iter1_cards.md, iter1_luicanvas.md, iter1_luichapters.md, and iter1_luipages.md. These files are part of a larger project that has already been implemented, but the user is looking to simplify and improve the codebase for better maintainability and scalability.

Based on the requirements and analysis, here's an implementation plan:

1. Refactor existing code: The first step would be to refactor the existing code to make it simpler and more maintainable. This involves analyzing the current structure of the application, identifying areas for improvement, and implementing changes accordingly.
2. Simplify user interface: The next step would be to simplify the user interface by removing unnecessary elements and features. This would help reduce complexity and improve usability.
3. Implement basic functionality: Once the user interface has been simplified, the next step would be to implement basic functionality such as generating mathematical training materials for an AI model. This would involve creating a new API endpoint that accepts input parameters and generates output based on those parameters.
4. Test and iterate: After implementing basic functionality, the next step would be to test the application thoroughly to ensure it's working correctly. If necessary, make changes and iterate until the desired outcome is achieved.
5. Improve performance: Once the basic functionality has been implemented, the next step would be to improve performance by optimizing the codebase and reducing unnecessary overhead. This could involve using caching, batch processing, or other performance-enhancing techniques.
6. Add new features: Finally, once the application is optimized for performance, the next step would be to add new features such as support for different mathematical concepts, improved user interface elements, and more.
Throughout this implementation plan, it's important to prioritize simplicity, maintainability, and scalability. By following these principles, the user can ensure that their application meets their needs and is easy to use and maintain over time.

## My clarification
Here I decided this is fine, but I need to reach some concrete code.

Well, this is consistent as a large plan. I give you an answer, point by point, and where we are with the progress.
* @iter1_app.md - Application init point, with the routes.
* @iter1_luipages.md - This is the highest level of the document tree, where different users could upload their work calling them different books, and where I consider separate major topics.
* @iter1_luicanvas.md - This renders the whole webpage, consisting of left and right menu, top bar and the canvas (again) at the center.
* @iter1_luichapters.md - On the internal canvas, there will be chapters in pages.
* @iter1_luiparams.md - Dynamic generation options, such as "generate 5000 numbers of 20 digits and their latin counterparts" would create a Card generator for an AI: Table contains 5000 rows, each row contains a number, each number is a link and each link has a number Card, which generates it's invariants such as slightly different wordings.
* @iter1_cards.md - The study cards, where an AI needs access to them all.
* You should also account for @Codebase, the other files in the system.

Okay now I answer you: okay the 5 files you mentioned, yes at this phase of refactoration we should start there - these are rather files I did show you, where filesystem has a bunch of .py files; we don't have much to do with them now as we want some basic user interface as well. Well yes I moved my old code to "old" - I thought it would inspire you, but you could not add the missing functions on the fly so it's too complicated to us. Basically today, I would like to implement rudimentary working system.

Btw: @iter1_aianalysis.md - this is our current conversation.

BTW. you was thinking about implementing our own AI. While I don't have plan for this, a testing set, which would perhaps learn quite fast even on my computer, would consist of something like this: 20 token input window, where each token would have something like 32 or 64 bits available, where one could have like 1 digit of bad precision more complex number, or perhaps 4 digits of good precision less complex number. Output would be something like 10 tokens of same type, where it could balance between input and output size. Additionally 2-3 tokens of context. It should learn to be a calculator of very small numbers, so it should be good in more or less strict combinatorics; it would be interesting what it could do - I don't know users, who would be very satisfied with this, but having a small proof-of-concept that it can download data would enable a tiny model solution to do something simple. Okay but this is not a priority now, perhaps just consider and comment about this in context - this would be our only single AI goal, because with bigger models we would run out of any kind of resources for other things, including the computer resources given that you also spend time thinking :)

With answers and questions given below in next paragraphs: Okay we have iteration 1 more or less described, but then we are now in iteration 0 instead. Even this is long, so let's have something like iteration 0.0, the first 4 hours of a very basic thing: our goal is me and you together work on documentation, and when we have enough of it, we generate some code. Your current input is very general, but I would go into details now.

Point by point, an answer to you:
# 1. Refactor existing code
I have these ideas:
* We should go deeper that "Number" is not a base widget, but I would benefit from having single widget for all pages. It has separated templates for layout table (bar, panels, content), menu and properties, top bar and content. Inside content, we start creating blocks: initially, titles, links and paragraphs as 3 types of blocks. Class to add them to page - I don't want any customized functions, but I can basically do if I can generate text.

# 2. Simplify user interface
I have these ideas:
* In properties, let's implement only the dropdown selection. For every property, just a list of possible options where we select one; instead of numbers for precision, for example, we allow user to choose between 3 selections.
* Could we, without internet for libraries, be able to replace the complexity of the content pane by turning Markdown into HTML? Or implement this: we need titles, paragraphs, lists, bold and italic and links in separate paragraphs. Perhaps the menu would be the same, but with properties pane it could be harder.
* We need text, lists of numbers with their decimal and Laegna values, and Q&A cards.
* For simplicity, perhaps initially we only have Q&A, not other types of cards - many AI systems demand that.

# 3. Implement basic functionality
Basically we need the operational flow here:
* We need the information to reach a simple class, where input is number type, it's precision, and what operations to train. Output is Q&A plan for simplicity of having only one.
* We have simpler numbers - I removed all complex properties, but what is left is still interesting. We do only 4 basic math ops, * / + -, but with interesting number type, which simplifies the numbers and operations itself so that good AI would already notice many symmetries.

# 4. Test and iterate
We have two choices:
* Creating a Spyder, which would, once executed download new cards until Ctrl+C is pressed, and simply demonstrate that it got the cards and was able to feed them to given function, mocker "fit".

# 5. Improve performance
But we have to avoid overkills:
* Simpler cache to remember small numbers would do, but
* Basically I think it would generate like 10 000 examples of numbers and operations in reasonable time, and rather I would not optimize. Rather we target to implement the functionality: remember the w3c browser, which simply lags at every step, but is the model standard of HTML specification; as a model standard of my math: when someone trains big math, they have resources to implement efficiencies, so our more valuable thing is full functionality; let it generate a week instead of a day - 10 000 numbers is already something, and user would not meet this performance having trained AI; I think AI itself would have harder time with performance than we with basic math ops, even with more advanced number type.
* If we could comparatively show where are the classic math solutions in this new solution, maybe an AI would recognize them and do a leap of utilizing known theorems and what it has studied from classic math. Python, for example is slow but efficient, and thus the code is quite functional and efficient. Iron Python is faster, but not Guido van Rossom (or how the name was). Computer is hardly ever so slow that it could not generate numbers - once somebody spends a week for few hundred thousand numbers with inefficient code, they could send it to us or others (who train AI's, preferrably), the rest of the process has almost zero dependency on the speed of our code. Rather, let's try to get substantial things, like generating given number of cards ..well it's kind of cache, but if we just save each card, we can reuse them without even thinking of inefficiency.
* Rather, my current code targets readability and simplicity: it's not a real-time thing after all, user could have their server or cloud generating for some time, and then use the cards. They are files, basically, Json files and the Spyder can just save them without caching - almost never want we the specific file.
* Indeed, _at some point_ we work with efficiency and optimizations.

# 6. Add new features
This is better, but also:
* They are not so much "features", than substantiality: in a sense features, but we need to get into efficient basic math, then a little up, and to reach rather _reliability_ and _consistency_ - features sound like adding something, like a swimming pool to a city, but what we have is rather like resolving the bottlenecks where many users would run into inconsistency; well for example it's kind of features to implement things like vector multiplication, tensors and matrices - then, with some form of differentiation and integration, users could program their own math.
* Notice this thing: classical math is better than ours with *combinations with small numbers*, but as we approach infinity - actually even just large numbers -, while their complexity starts approaching infinite complexity and number of combinations grows exponentially, in our case the combinator is more and more efficient as the numbers grow and we have more combinations, and it reaches certain levels of precision; here, what matters is rather coherence: it's not a big problem if we lack some fancy math solution in our framework, but it's a big problem if, for example, in certain relations we cannot achieve something simple in given condition, for example being unable to multiply or sum two numbers in a given space without paradoxes and odd behaviours.
* To state in other words: where classic math will grow into several self-referential exponential complexities, and self-referential means it combines existing exponential inefficiency with another divider, which turns even this slow result into exponential inefficiency in terms of itself; consider that it's hard to reach into infinity with combinations - rather, with combinations of two numbers with few thousand digits there will be precision problems, and non-balanced combinatoric space as while the real numbers indeed grow into infinity, the combinatoric system *must not grow into infinity*, nobody is going to reach infinitely many combinations, even quantum supercomputers with superpositions do this, they have some rules of not being able to just *perfectly* solve it in reality. With decimal system growing towards infinity, it *simply does not approach any closer*, except a few numbers - even those rather irrationals, internally as complex. In our case, we actually reach something like limits, because we are growing only to certain, finite number of digits, in a very balanced way so that we are not trying some marginal combinations in heavy large brute force somewhere in rather random edge of infinity, but we are running in balanced way in combinatoric space, which is *close to infinity by it's properties*, and we don't care that there are more and more infinities - we hit the right points in combinatoric space and we can do things like Newtonian method, trying the middle of infinity and zero, and then the resulting center and infinity - this one we do for real. This efficiency is rather mathematical property than anything computational, and those are hard to call "features" as this is the mathematical synchronicity, fit of our theory with reality, rather than efficient use of computational power, so I rather would follow this other principle, also well-known with good example being Python itself we are writing - notice that it's actually, computationally, very inefficient, but the code is elegant and *inherently efficient*, where in terms of computational power or even math itself it's hard to say what is the "feature" or "optimization", rather it's the holistic whole that you don't get annoyed from entering extreme code and managing large code base for even simpler problems:
* * The first rule: don't optimize. The second rule: if you really have to, just do it later. I think in our mathematically elegant case we can earn back by optimizing towards simplicity, and gaining elegance.

This given: while the resulting system might be slow, world contains hackers who like to optimize system, like Iron Python, and even stronger argument is that if someone needs this computational elegance, we rather enable them to work with mathematical theory; with memory compression and cloud-based cache we don't even surprise Google, but even more there is the mathematical genius somewhere out there for this task - for example, to use my well-structured code and find it very simple to translate it into C++.

Please: now contemplate - this is what you are doing with your time, it's hard to use any other word for 1 hour of thinking - on actually implementing something. Go deep into the meanings and purposes, and find out the actual thing, which would enable us to progress - with minimal, yet scalable steps to reach the point where number cards reach the AI, and perhaps it's able to validate the results in the later versions; my iter1 is now future, and we need to scale in approximately that feature set later as well, but currently it's now iter0 and we are not any more interested in every function, which should optimize our time.