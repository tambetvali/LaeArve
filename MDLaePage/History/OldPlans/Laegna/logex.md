# Laegna

I have my own mathematics and logic, which I call Laegna Logex for machines or Laegna Logecs as a logical system. It has four Truth values.

I describe the Laegna Assembler here, which I want to implement before creating the Laegna Programming Language. It will contain interesting things to try out.

I leave this document partial - in regards to full descriptions of each object, even if not an exact fit, is a demonstration of the base logic followed here.

## Logical or empirical

Laegna Logex is not defined to be logical, but it's defined to be empirical.

For a machine, the difference is that it can take this as an empirical mistake, if one gets a variable complexity, which is so hard to resolve that it does not exist.

Complexities can be:
* Unmanaged theorem trees growing indefinitely
* Unmanaged loops, which do not have the right entry and leave conditions.

## The Assembler

### Assembler is made of what represents Laegna binary unit - a Ten.

Ten is a dimension-exponentially growing object, which is still absolutely good in reading itself up and down, this in several rounds. For this, it has an upper and lower boundary, which will grow linearly over it's dimension.

For Ten is the natural complexity number, the natural numbers of decimals will start from 1, and without extension, a smaller decimal number cannot be written.

Equivalently, along with decimal digits, Laegna digits can be used. They are O, U and A, or I, O, U, A, E, V - either 3 or 6 in count, but U is one-dimensional, thin line, zero dimensions vertically. 

Let's have three decimal digits for these natural numbers - with non-digit being a thin line in the middle, but a sign showing that the number is going diagonally up and down.

The middle position is actual number, True or False, in case boolean is contained within. Then, A and E are frequencies, consisting of two digits, but having only values inside it's if condition. If condition states that inside, some other value holds and outside, it does not hold. Let's say that for  dimension -k, it's the opposite, and for +k, it's so big that values of k would form an opposite. Still, k has values, which hold in upwards dimension.

Normally, for flat Den, values of A and E need to be closed, so much that the logic expects them to be so. If, inside one branch of the if, a value is compared True, it's automatically false in this case for other branch. Thus, for trivial Tens, two branches would go in conflict, if the values do not match. This, because we want to keep the logic combinations low.

Default Den is Den of Boolean, which is the smallest unit on Truth Value Table.

1 Den[k] = {
    A:U:E
}

Den forms in two dimensions, and becomes a symbolic representation of infinity:

k has now two dimensions, so it can be true and false in two combinations. Vector of other variables might now exist. Let's assume it's an assembler, so we won't add many possibilities - only the trivial ones. V is thought to be either outside at all, or inside exactly between I and E, within certain frequency. Minus this frequency, it would bring the infinity infinitely close, so that it becomes a normal zero - infinity, then, is twisted to be one. Two, then, as a normal number in conditions of infinite curve, in relation to one, becomes an infinity outside the infinity, and the relation between Zero to One, inclusive, and One to Two, inclusive, are the breaking points between minus and plus infinity, .

1 Ten[k] = {
    I:O:U:A:E:V
}

This brings Den into two dimensions:

2 Dens[k] = {
    A:U:E
    A:U:E - middle line is the initial combination
    A:U:E
}

Dimension of 2 Dens, with dimension k, is made of two values either True or False - but when one finds such two values in a row, coupled in pairs, they form a Laegna number, and if there is one True or False in the middle, which is a condition impossible for several combinations of types, it will be a sign of a direction, forming an U dimension in relation to other numbers.

2 Dens define the relations Up, Down, Left and Right. The directions are True for Up and Right, and False for Top and Left. This is called dimension zero - division into Two. Creating a True and False value out of the variables will make them somewhat neutral.

2 Tens, then, consists of 6 lines, where the initial condition is at U and the final condition is at V.

For 2 Dens, diagonal line from down to up should contain two combinations of k in relation to other variables. Those variables must close a circle that they form two condition sets, which yield the same frequency pairs. Then, it will be counted.

3 Dens[k] has 3-bit k value, which can represent 3 if clauses or 3 dimensions of k. It has a surrounding box similar to 2 Dens, but for each element of 2 Dens. So, this decimal number of type representation has an exponential growth factor. It grows in every dimension, but it has first combinations still at the center. Now it has 2 dimensions of Up, Down, Left, Right. They have two local diagonals in fractal pattern and two global diagonals, and diagonals represent A, E on upper and I, O at lower dimension. When they are upwards position, they form Position to their Ten representation - Ten means the middle letter, which is surrounded by combinators -; when they are downwards, but happy Position, it's a Negation. When it's in upwards position, but not happy - could not combine the solution with their precessors -, it is Posetive. When it's in downwards position and not happy, it is a Negotive. The bit represents only True and False value, and it's set either to True or False. Still, it can also mean those four values, which can be used. When it tries all the combinators and fails, it becomes a bad value; when it will remain in one position, it becomes a good value; when it's good in several settings, it can become temporary posetive, which wants to give away some of it's decision power - a controller would appear to set it's value by other means. If it's not set, it will finally have a random value, which can be overriden by having a Frequency over selections.

1 Digit[n] {
    I = False, False
    O = False, True
    A = True, False
    E = True, True
}

n is a dimension of the digit, which is a natural number dimension and can be written starting from 1. The whole combination can be None, in which case unknowns are considered, or it can be All, in which case, it's strictly bigger than infinite number of nines. The index numbers, in Laegna, are decimals, and an index is used here to count the digits. For division and subtraction of numbers inside, we must consider None - but, in addition to not having a value, it does not have any size, and thus it's not our idea to evenly distribute it inside the numeric system. Such numbers exist as thin lines between the values, but when we are interested in whole values, having infinitely thin numbers is not particularly interesting. The combinations of one A and one O, in infinity, continue to remain the smallest number, and thus it will converge to zero - then, despite them being ones, we can use them in place of zeroes in case we talk about infinite relations of our numbers. 

It could be Ten digit, or Den digit, by default a Den digit, and it will become a shapeshifter - with many possibilities of different logical tables. But their binary codes do not change - initially, I considered other codes, where I = False, False, O = False, True, A = True, False and E = True, True. But as it's a machine code, it should represent itself only in one way. Where possible, this behaviour is expected.

2 Digits would form one digit out of two-dimensional Dens, which is 