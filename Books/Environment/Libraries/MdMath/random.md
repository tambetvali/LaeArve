### Differences Between mdmath and mpmath

1. **Core Focus**:
   - **mpmath**: This library is mature, widely used, and specifically optimized for arbitrary precision arithmetic, including floating-point operations. It provides extensive functionality for numerical analysis, special functions, and matrix calculations.
   - **mdmath**: While similar to mpmath, mdmath might focus more on specialized use cases, like formatting precision-heavy numbers or scientific computations. Its features may include handling big numbers in unique formats, tailored for specific domain requirements.

2. **Functionality**:
   - In **mpmath**, random number generation is supported via `mpmath.rand()`. You can generate and manipulate numbers with specified precision easily, like in the example provided earlier.
   - In **mdmath**, it depends on the specific implementation and whether it provides built-in random number generation. If mdmath does not include random functions, integrating Python's `random` module could be one workaround.

---

### Example in mdmath Format

If you need a 100-digit random number compatible with mdmath:
1. Ensure mdmath precision is set to 100 decimal places.
2. Use a custom function that combines `random` and mdmath-like formatting.

For instance:

```python
from random import uniform

# Generate random float as a string with 100 digits
random_float_mdmath_format = f"{uniform(0, 1e100):.100f}"  
print(random_float_mdmath_format)
```

Here, the output is formatted to have precisely 100 digits, simulating mdmath requirements.
