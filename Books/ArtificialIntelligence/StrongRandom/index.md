# Strong Random Basis of an AI

There exists a random number generator:
- It renders each dynamic feed into a static presentation of the random number.
- It gives random feed to an AI, with specific mapping of random factor to specified outcome; for example the machine has 10 000 random states, but they can be identified by random number after the generation.
- The fit algorithm, in it's "corrects" and "wrongs", trains the AI with the random answers statically mapped; it can give question and aswer pairs with synchronized randomization.

AI would subsequently develop a sense about creating answers with given random probability, for example:
- Roll a Dice

Implement like this:
Metacontainer: contain random function, which calculates the dice value 1-6.
AI can access this number when generating answer.
The right answer has always correct number.

When AI does not have this random feedback any more, it's randomization is in closed box: it gives this distribution of answers.

It also needs to learn that it does not measure questions on the same basis.

## Questions and answers

To measure questions and answers on the same basis with simples method:
- Create statistical correlation table for random results
- Add statistical distribution or average divided by number of samples, of the fit modifications and perhaps create a learning model.

For example:
You have 10 000 samples where you know the random distribution.

You consider a little bit in your weighting, if it slowly learns the basis over time, for example random function by observation - altough if it optimizes for maximum score, it could be measured precisely in each step to utilize it's common sense.

You can train with 10 000 samples and do the fit with the complete result.

You measure random factors in answers: for example, the average score of dice. You apply your fix on the whole space at once. You are expected to have enough connections between the units, where you might want to utilize Laegna numbers to get them in less combinations.
