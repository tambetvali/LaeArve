# 🔳 Logex

Logex is a logical machine of my Laegna Logecs, the Logic System I am using herein - while I am trying to make it easy that you have Latin System implementations by my documents, where they might be easier to implement on current mainframes.

Let's assume a variable has time and space:
- Variable is `a`
- It's time or approximator is `~a`
- It's space `#a`

In system of time, the variable can be thought of moving further or backwards in time. When you go backwards in time, to recognize past values, it also creates a new axe: a new versioning, where in certain directions, you can fix the values of this past moment.

Space #a is simpler and here we can see the property:

Where variables are associated to Spaces, they won't have static logic values, but rather dynamic. With ",,", you can scroll time at the same time when you change the value: try Chuck as existing language for music, where you have to operate with time. If you would make chuck a logical machine, perhaps it would still have time.

In Prolog mapping, for example, every statement is conditioned into time:
- Condition that time is current is around every condition.
- To run multiple statements at the same time, time is ran multiple times.

This condition could be accessed by:

[cond]var

It's rather index outside than index inside, and it could contain settings, by which others would notice this variable. You can write "var.attribute" forwards, where var.[cond]attribute still says the attribute is in such space.

var[cond]

This is index inside.

You can have frequential conditionals:
F = [a, b, c, d, e, f].

This has 6 frequencies or conditions: each can map to one index in an array. When you use the array index, you directly use the condition: for example, if 3 is c in F, and F type is the index for variable A, then A[3] would mean the value of A given, that it's the value of A when F=3. F=3 in case c is True and all the other members are False: then, the frequencer has one precise value, which is in logical consistency with others. The frequential system means that if the frequential components do not build the same value, they won't fit; in this form, fit or non-fit is True or False at the position; in other implementations, the Position having same Value as it's Position makes it True, and all the other values make it False; we can use accented letters for each logical relation of ponegation, so that they would have absolute difference between 2 (2 has absolute values -2 and 2, why this means between -2 and 2, when those are written in order; rather we find a solution than a paradox, so we put them into order hearing this sentence with such solution into Position space).

When variables are added to space of something, which is being modified, their values would be mapped: for example if for [X]R, which is defined on range X and not variable X (by which it would simply point to such position in R, whether it exists or not, so that [x]R could be queried anyway and an AI could learn what to do in [x]R space, should you define a model there by adding a function scope). Having X, when you change X, value of R would change, and when you change it back, it would change back. It should be somehow dynamic: one could move an item from input to output and vice versa.

Time is attributed so:

This function's time condition could be accessed by this form:

(cond)var

It's rather the caller-way, and this syntax could be used:
- To reach back to where the function was called with such parameters, creating an additional body to this function in such case.
- To have this condition as an environment, where the function's values are changing otherwise.
- To call the function from other side of equality mark, being additional time-conditional of the execution, so that while the input goes here, the output will be in time-before, on I and E axe of the Ten, and in this regard the function has ran backwards; in vase of having (cond)()var it's in I position, where output is instead there and it's processed still in reverse.

Frequential form:
F = (a, b, c, d, e, f).

var(cond)

The function is called with input, and input is changing while the space is not:
- When you change spatial value, you think twice.
- When you change time value, it's rather not stored: the function might give you different output in next time.

Indeed, you could go just further in space and achieve the time effect, but for creating programs this makes sense:
- We differentiate () and [] space, because otherwise we lack semantic space for operations: for example, if matrix function is M(v), and this maps vector v, then how to access matrix space?

Then, let's also assume:
Properties you access in a way:
- __Variable.Property__: These are common-form properties or time properties.
- __Variable:Property__: These are spatial properties, such as actual projection matrix.
- __Variable·Property__: These are temporal properties, and they exist in sense of the current time moment.

() and [] cannot be separated in the hard space, but to keep it systematic, you need to use () for temporal values: which are not given, where the time is passing; and [] for spatial values, where some change in the system is needed to produce the change.

For frequency:

F = [a, b, c, d, e, f]

Connected with R as it's space, index:

[F]R, R[F]

Imagine a space of if blocks like this:

```
if F=0:
  R = 7
if F=1:
  R = 8
etc.
```

This means, R at position 0 is of that value, at position 1 at that value. If the logic is complete, values of R can be seen separately.

Let's imagine the "Ideal", parent of each entity or operation, is itself defined like this:

(t)Ideal.

t, in return, is a singleton value of time: for t, only a single time exists.

Now, while logic can be barely added, it cannot be changed unless t is added 1. Each contained variable will be respective to t; if you call it with criteria (t = 2)R, (t < 4)R, (3)R if t is in it's ordered parameter list; in each case, you get a value of R _if another condition is met_.

To achieve lists:
- The other condition is compatible with each logical state.
- You cannot use values, against which there are conditions: for example, stating "if R < 3", which means values from 3 are False, or "if not R >= 3", which states vaguely in first place that values _above_ 3 are rather True, with the same logic. We can add frequencers for such effects.

## Time-backwards conditioning

In various ways, you can send signals back in time in Logex conditioning.

Consider you define a class:

```python
class Apple(Fruit):
  def __init__(self):
    self.a = 7
    Fruit.stage2() # on both sides of Apple and Banana, Fruit goes to stage 2 of
                   # initialization. We don't cover the semantics.
    if self.is_yellow:
      type(self) = Banana
    self.b = 7
```

Notice that A condition self.a = 7 must exist in Banana at the entry point; self.b = 7 is not an applied condition and might not exist. Advanced compiler would figure out non-effective variables and variables, which allow for update; classes themselves could keep a log of initialization variables and guarantee that those are up-to-date so that applying other class could redevelop this.

Rather than making advanced features illegal:
- Optimizer could optimize out these functions to enable some people to understand, if compiled at user-optimization or implementation-optimization flags, an AI could figure out, how to do the same operation in other language; advanced compiler could have a preprocessor, which is able to simplify the code to equivalent structures and statements in less advanced logical spaces, where the user's languages might be implemented. Agile Open Source always starts small: we need to create very simple standards and code, which would implement them; the standards, however, would contain rules for much more complex cases and be extensible; where user with less features should be able to use subset of features or autogenerated dialect or version.
- We need "genuine freedom", where intelligent people can develop their solutions: we would have advanced mathematical solutions. People, companies and parties interested in not using this code, but they could utilize less advanced code, buying from same or other developers - rather, we don't want to miss the features altogether. Where one man at my childhood said: "for compilers, it's too complicated to work backwards in time".

To work backwards in time, the logex machine (calling this the "space dimension", where your past karma is resolved, vs. "time dimension" where you grow into the future and resolve conditions in different way: you align for your future karma, which might be dharma instead [as a Buddhist, you could use "good and bad karma", or simplify to "dharma and karma", where good karma could be lack of bad karma, but dharma is the existence of good: then, they are values like OA and AA, where in OA the unit is where the good is reached by lack of bad, which means it might be actually more effort where AA is the same amount, where it's reached by existence of good: Laegna digit has the same spatial content for each, so the digit O in it's position Ó would resolve just so much in it's dimension that the result is equal to calculating position A, but it happens by resolving the O]).

It can work backwards the following ways:
- Functions allow for change and improvement, where they move further in their local time, where the global time is rather not unaffected by this, or is affected by collections of such changes. When values are changed after their initial appearance, this could be of low-precision values optimization.
- The past is affected if you resolve it's outcome: for example, you did buy a stock yesterday and you want to know it's actual worth at buying moment, but you have to reconsider your current situations and the value of your stocks and that single stock and it's risks (whether it's _all_ you have or a _part_, for example) yield in the future; you calculate back for these effects and at the same time, you update spatial variables, which reflect that change.
  - To commit the change, you must have, at the last level, global time progress in case you changed the variables, in some dialects.
  - Despite it might be a logical language, you have the imperative commands, which do _change_ the value: it works, because it subsequently changes the _value space_, where the logic must belong to value space, which makes progress at the same time (",," operator).
- The past is kept without change, and it _only adds_ variables; it can be even intelligent in growing together with future.
- The change is consistent with acceleration ratios of the variables, which would change their values.

To condition backwards in time:

Let's imagine the constructor or equivalent semantics (template in ideal world) exists:

```python
t = s

if (s)typ == "Apple":
  a = Apple(i),, s += 1
if (s)typ == "Banana":
  a = Banana(i),, s += 1
```

A is here conditioned by value, which exists in value space s. When a is changing it's type, at the same time conditional time is passing in s, and the logical value is dependent on the value of s: optimizer would rather collect values, which are invariant to this conversion, where they keep together a constant space.

If type has been changed, last t, which is the previous value of s, could be checked - I cannot ensure every language allows to write it in this way, but lets assume t is watched for each change and relevant functions do all their work; for example, they finish by creating a line in the log file or other side-effect: this side-effect would be fed back, and the consistency would break if the parts are not executed in order.
