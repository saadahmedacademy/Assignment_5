
"""
7. Access Modifiers: Public, Private, and Protected
Assignment:
Create a class Employee with:

a public variable name,

a protected variable _salary, and

a private variable __ssn.

Try accessing all three variables from an object of the class and document what happens.

"""

# Create a class Emplyee
class Employee:
    def __init__(self,name:str , salary:int, ssn:str) -> None:
        self.name = name          # Public
        self._salary = salary     # Protected
        self.__ssn = ssn          # Private

# Create an object
emp : Employee = Employee("Muhammad Saad Ahmed", 200000, "123-34995-212")

# Access public variable
print(f"Public Variable : {emp.name}") # works

# Access protected variable 
print(f"Protected variable : {emp._salary}")  # ⚠️ Works, but not recommended (by convention)


# Access private variable
try:
    print("SSN:", emp.__ssn)  # ❌ Will raise AttributeError
except AttributeError:
    print("Cannot access private variable __ssn directly!")

# Accessing private variable using name mangling
print("SSN (using name mangling):", emp._Employee__ssn)  # ✅ Works, but discouraged