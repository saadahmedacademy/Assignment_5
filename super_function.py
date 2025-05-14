"""
8. The super() Function
Assignment:
Create a class Person with a constructor that sets the name. 
Inherit a class Teacher from it, add a subject field,
and use super() to call the base class constructor

"""

# Create a parent class
class Person:
    def __init__(self,name:str) -> None:
        self.name = name

# Create a subclass 
class Teacher(Person):
    def __init__(self, name:str,subject:str) -> None:
        super().__init__(name)
        self.subject = subject

# Create the isinstance of the class 
teacher : Teacher = Teacher("Muhammad Saad Ahmed","Methamatic")
print(f"{teacher.name} teachs {teacher.subject}")

