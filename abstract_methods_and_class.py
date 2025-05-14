
"""
9. Abstract Classes and Methods
Assignment:
Use the abc module to create an abstract class Shape with an abstract method area().
Inherit a class Rectangle that implements area().

"""

# import abc to create abstract class 
from abc import ABC , abstractmethod

# Abstract base class
class Shape(ABC):

 @abstractmethod
 def area(self):
        pass
 
#  subclass 
class Ractangle(Shape):
     def __init__(self, width:float , height:float):
         self.width = width
         self.height = height
 
    #  define the area method becase its abstract
     def area(self):
      return self.width * self.height
     
# Create the instance
shape : Ractangle = Ractangle(23.0,25.0)
print(f"The area of ractangel is {shape.area()}")
     
