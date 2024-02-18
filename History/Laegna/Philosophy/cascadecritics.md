# Critics to Cascade

I am using Cascade, which is combination of Continue, the AI framework, with CodeLlama-7b and CodeLlama-13b, which are the neural networks of an AI. I am not very sure, which part of the process each plays.

I have this critics:
- VSCode does not properly allow me to disable some files from Cascade, missing a command given by Cascade; which is the problem of either one or another.
- It does not refresh it's index when I add and remove files; possibly it's too hard to rebuild the internal state.
- It does not understand, when it does not have access to files. It has learnt, how to cope with limited information (Game Theory, despite not using this), and thus it gives some statistical average of information - being aware of only certain files (Attention, where my computer thereby the model cannot have much attention); in this case it generates probable answer, given this information.
- When working with large code bases, it gets very theoretical.

Given this - as we technologically are unable to overcome all this, rather going slowly towards target, I am building a philosophy about how to make use of an AI, given different limitations.