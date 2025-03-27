# Lagatal: Laegna Digital System

Don't mind if the name does not sound especially cool - it's not going to be (at least before the salary day, when you forget about it anyway and say "lagatal" :D).

__Dens__: Boolean False is `O`, Boolean True is `A`.

__Tens__: use the simplest floating point with 1 bit for whole number value, 1 bit for exponent value. Mapping the floating point standard, you should get -Inf, -0, +0 and +Inf, which is a _Laegna Digit Ten_.

_-Inf, -0, +0, +Inf_, __Laegna Number Discrete Mapping__: Somehow, this suggests math behind discrete mapping of infinity to numeric scale and then removing one exponential level to get digit and it's relation to it's infinite repetition (of it's properties).

_-Inf, -0, +0, +Inf_, __Laegna Number Discrete Mapping__: You see that infinity relations are instantly broken if your number system relies on classical 0; this is why we do some magic with 0 before using our system. You can imagine a precisionless numeric mapping, which maps 4 limit values directly to 0 based on their properties; and where their properties are lost in case of any other number

_Unsigned Binary Laegna Number_, __Unsigned Binden__: _Compressed Laegna Number_ maps to binary using 2 bits to represent one Ten, with no loss of information.

_Signed Binary Laegna Number_, __Signed Binden__: The way binary digits are represented, in signed numbers some Laegna numbers map precisely all the necessary operations, especially with uncompressed numbers (but not only, if you are advanced, calculating the exact angle of compression and it's digit-wise properties of representation with deep math); using two bits for Ten might require you to do minimal, fast and optimized conversion from Ten to 2 binary digits.

_Floating Point Binary Laegna Number_, __Floatden__: use exponential part as Octave, mapping `IE` to 2 bits; and whole number part as the number. Consider: we map infinity based on symmetries, and with these symmetries the properties of calculations remain intact.

_Representing Laegna angles with Ticks_, __Laegna 2-bit Ticks__: ensure coordinate mapping, which maps points into their 2-bit representations, where only 4 angles are possible. Where 1 tick is the precise angle, +0 and -0 are normal angles, -1 and 1, where +Inf and -Inf come back from infinity and form 2 and -2 in opposite direction. (_precisely_)

_Representing Laegna angles with Ticks_, __Laegna 1-bit Ticks__: ensure coordinate mapping, which maps points into their 1-bit representations, where only 2 angles are possible. Where 1 tick is the precise angle, +0 and -0 are normal angles, -1 and 1, where +Inf and -Inf come back from infinity and form 1 and -1 in opposite direction. (_close to_)

_Representing Laegna angles with Gradians_, _Angle of +Laegna `A`_, __Unsigned Laegna `A` Angle__: convert Laegna angle to gradians, multiplying it's value with 100. This is also _an angle of this number_.

_Representing Laegna angles with Radians_, _Angle of +Laegna `A`_, __Signed Laegna `A` Angle__: convert Laegna angle to radians, multiplying it's value with 100. This is also _an angle of this number_. Notice that for unsigned number, 2 is rather half infinities: infinity of unsigned number is 2 times bigger.

_Laegna Harmonic Circle_, __Harmonic Circle__: take numbers [`À`, `Ò`, `I`, `O`, `A`, `E`, `Ó`, `É`] - values of accented digits modify _previous digit_ of the number, being frequential. Assigning values -4 to 4, you get two full circles; if two degrees are at the same angle, they are called _harmonic_.
- For example, have musical octave sqrt(i, 12): i / 12 is the octave of harmonic system.

_Sin and Cos of Laegna_, _Sincos_: have sinus and cosinus. Numeric value of one is the input angle (-2 to 2) divided by two, so it oscillates between -1 and 1. You cannot do all the calculations without complex numbers, as it's only the AE frequency of it, the real part, with the imaginary part missing.

_Frequential Complex Number_, __Laegna 2-frequency complex__: very often, Laegna numbers involve 2 frequencies. Written by two digits R and T or complex number: the number integrates negative and positive frequency at IO and AE axes, which is why complex numbers create dimensions and do not map to numbers X or R, but to R² (Laegna R or R² if C is Space).

_Mapping inertial system with complex numbers_: why the Laegna Projections and number system symmetries seem initially complex, because you need a complex number to map a point. Real or imaginary part of complex number map square, while both together map circle; square does not have direction, but it's a mental illusion, which appears as you cannot have the line, which forms a circle, straight (you need an imagination-ball, sphere like an Earth and horizontals/parallels of it's standard projection united with Laegna's projective system of triangles and squares).

_Laegna Unit Ball_: Laegna unit ball is a Sphere, where `r`=1, `d`=2, `pi*r`=1 or 4 or 100 if pi is 400. From center to outside center of infinity is 4 units, also to travel around the center in "the Middle Way" or "the Longest Way" of 2 components. In Flat Space, the ground of such Earth represents Laegna number system, where we sum only local (flat) angles to get T and hyperspherical angles to get R.

_Laegna Unit Circle_: Laegna unit circle is the unit ball with `r` and `d` range doubled, where in the initially 2 times smaller flat space of the resulting flat system is projected so that it fills the whole area, and coordinates are used accordingly. Use complex numbers or combine them to `18` (dec) if you don't want to see the exterior line as a point; in system of A, E, Í, Ó [+`14`].

_Laegna Angle in Julia Programming Language:
```julia
laeangle = 1 # angle "A"
radians = laeangle / 4 # 0.25

```

_Representing Laegna Number Frequences in Binary System_, __Frequential Binden__: you need more than one digit for a digit, or more than one number for a number, to have frequential representation of a Laegna Number (optimized).

## Ticks

@__Tick__:

The unit "tick" is a measure of angular displacement in the context of computer science, particularly in the field of robotics and automation. It's used to represent small changes or differences between two points on an object. In this sense, it's similar to radians (radians per second) but with a smaller resolution.

In programming languages like Julia, R, Python, and even AI fields such as machine learning, "ticks" are often represented using the tick keyword in functions that deal with angles or rotations. For example, if you have an angle of 10 ticks, it means there's been a change of 1/10th of a full rotation.
In relation to other units like radians and degrees, "ticks" can be used as a way to represent angular displacement in more precise settings where the resolution is important. However, for general use or when dealing with angles that are not too small (less than one tick), it's often better to stick with standard unit conversions.

In summary:
* Ticks are a measure of angular displacement. 
* They're used in computer science and robotics as an alternative to radians and degrees. 
* In programming languages, they can be represented using the tick keyword or similar syntax.