
"""
5. Static Variables and Static Methods
Assignment:
Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.

"""

class MathUtils:

    @staticmethod
    def add(a, b):
        print(f"The sum of {a} and {b} is {a + b}")

# Access using the class
MathUtils.add(2,7)

# Access using the instance
obj :MathUtils = MathUtils()
obj.add(2,10)
