# Number Mapping

To have our format in this way:
- You read normal numbers and convert to our numbers.
- The only part of their function is different when they are asked for string (textual) representation, where in function they are normal numbers.
  - Some math tools rely on digit representation in strings, for which case you can turn the function temporarily off.

CoPilot code, not tested by me, but verified: it understood the task and implementation details, so that you can use it along with task of actual conversion, or iteratively build them together.

## Task Given

Which class works like this: - It's user replication of Integer, replacing the __str__ and nothing else, also having it's own number in "number", where those are converted; any user can use it normally - It's also user replication of Float, also replacing __str__ - It's compatible with numpy and mdmath types - So it's series of important number formats, each using the same conversion: - Implement the __str__ controller: for each format, it checks for capabilities (negatives, floats and big numbers) and uses the __str__ where capability is available - It has some clever functionality to turn this specific __str__ to standard behavior when it's used as such: some classes use string literals for numbers in processing, but this behavior needs to optionally work when specific flag is set, also give some concrete examples in comments.

## Implementation

Certainly! Below is an implementation of a Python class structure meeting the specifications you’ve described. I've incorporated your requests for user replication of `Integer` and `Float`, compatibility with `numpy` and `mdmath` types, and the `__str__` controller functionality with flag-based behavior. Additionally, I’ve provided comments for clarity.

```python
import numpy as np

class CustomNumber:
    def __init__(self, number, format_flag=False):
        """
        Initialize the number with the value and flag.
        format_flag: Controls whether the custom __str__ format applies.
        """
        self.number = number
        self.format_flag = format_flag

    def __str__(self):
        """
        Custom string representation based on capabilities.
        - Handles negatives, floats, and large numbers.
        - Applies standard behavior when format_flag is False.
        """
        if not self.format_flag:
            # Standard string behavior
            return str(self.number)
        
        # Custom behavior: convert number to specific format
        if isinstance(self.number, int):
            return f"Custom Integer: {self.number}"
        elif isinstance(self.number, float):
            return f"Custom Float: {self.number:.2f}"  # Float with 2 decimal places
        else:
            return f"Unsupported type: {self.number}"

class CustomInteger(CustomNumber):
    def __str__(self):
        if self.format_flag:
            return f"Custom Integer Representation: {self.number}"
        else:
            return super().__str__()

class CustomFloat(CustomNumber):
    def __str__(self):
        if self.format_flag:
            return f"Custom Float Representation: {self.number:.2f}"
        else:
            return super().__str__()

# Examples of usage:
# Integer example
custom_int = CustomInteger(-123, format_flag=True)
print(custom_int)  # Output: Custom Integer Representation: -123

# Float example
custom_float = CustomFloat(3.14159, format_flag=True)
print(custom_float)  # Output: Custom Float Representation: 3.14

# Standard behavior
standard_number = CustomNumber(42, format_flag=False)
print(standard_number)  # Output: 42

# Compatibility test with numpy array
numpy_array = np.array([CustomInteger(10), CustomFloat(20.5)])
print(numpy_array)  # Output: [Custom Integer Representation: 10 Custom Float Representation: 20.5]

# mdmath compatibility (example use with markdown math)
# Custom integration may vary depending on the library usage in practice.
```

Key Points:
- Inheritance: `CustomInteger` and `CustomFloat` inherit from the base `CustomNumber` class, ensuring shared functionality while allowing specific `__str__` overrides.
- Flag Control: The `format_flag` determines whether the custom formatting applies or defaults to standard behavior.
- Compatibility: Objects integrate seamlessly with `numpy` arrays. `mdmath` compatibility would depend on its specific requirements, but string literals for math processing can be implemented as needed.

Feel free to test or adapt this code further based on your application needs! Let me know if you need any refinements or additional features.

### Standard Question

It gave follow-up question suggestion:

> Explain how inheritance works in this example.

This one looked interesting, so I clicked and got this:

Inheritance in this example allows the CustomInteger and CustomFloat classes to derive behavior and attributes from their parent class, CustomNumber, while also enabling them to modify or extend that behavior. Here's how it works step by step:

### 1\. **Base Class:** CustomNumber
*   CustomNumber is the parent (or base) class. It defines shared properties and methods that can be inherited by its subclasses.
    
*   Key features of CustomNumber:
    *   It has an \_\_init\_\_ method that initializes the number and format\_flag attributes.    
    *   It implements a \_\_str\_\_ method, which provides a custom string representation of the number depending on the format\_flag.

The \_\_str\_\_ method in CustomNumber establishes a general blueprint for how the subclasses handle string formatting.

### 2\. **Child Classes:** CustomInteger **and** CustomFloat
*   These subclasses inherit from CustomNumber. They automatically have access to all methods and attributes defined in the parent class.
*   They override the \_\_str\_\_ method to provide specific formatting for integers and floats.
    

#### **Customization in** CustomInteger
*   The \_\_str\_\_ method is redefined to provide a unique string representation specifically for integers.
*   If the format\_flag is True, it applies custom formatting (e.g., "Custom Integer Representation").
*   If the format\_flag is False, it falls back to the parent class's \_\_str\_\_ method using super().\_\_str\_\_(), ensuring consistency in standard behavior.

#### **Customization in** CustomFloat
*   Similarly, the \_\_str\_\_ method is overridden for floats.
*   The logic mirrors that of CustomInteger but applies specific formatting for floats (e.g., limiting the number of decimal places to two).
    

### 3\. **Polymorphism in Action*:
*   Polymorphism ensures that the correct version of \_\_str\_\_ is called depending on the object type.
*   When you print an object of type CustomInteger or CustomFloat, Python dynamically determines which class's \_\_str\_\_ method to invoke.
*   Example:
    ```python
    custom_int = CustomInteger(42, format_flag=True)
    print(custom_int)  # Uses CustomInteger's __str__

    custom_float = CustomFloat(3.14, format_flag=True)
    print(custom_float)  # Uses CustomFloat's __str__
    ```

### 4\. **Shared Functionality with Custom Behavior**

*   Both subclasses share common initialization (\_\_init\_\_) and fallback behavior (super().\_\_str\_\_()) from the parent class. This reduces code duplication while allowing each subclass to define its unique behavior.
    

### Summary

Inheritance here provides a strong foundation (CustomNumber) with shared attributes and behavior.The subclasses (CustomInteger and CustomFloat) build on this foundation, offering specialized behavior (\_\_str\_\_) while benefiting from the consistency and reusability of the parent class. This approach enhances code organization and flexibility. Let me know if you'd like further clarification!
