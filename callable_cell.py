
"""
19. callable() and __call__()
Assignment:
Create a class Multiplier with an __init__() to set a factor. 
Define a __call__() method that multiplies an input by the factor. 
Test it with callable() and by calling the object like a function.

"""

# Create a class
from typing import Any


class Multiplier:
    def __init__(self, factor) -> None:
        self.factor = factor

    def __call__(self, value):
        return self.factor * value

# Create an instance 
m = Multiplier(5)

# Check this 
callable(m)

# Use the object like a function
print(m(10))