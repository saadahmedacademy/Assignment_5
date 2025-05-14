"""
 Using self
Assignment:
Create a class Student with attributes name and marks. 
Use the self keyword to initialize these values via a constructor.
 Add a method display() that prints student details.

"""
# Create the class
class Student:
    def __init__(self,name:str,marks:int):
        self.name = name
        self.marks = marks

    def display(self):
       print(f"{self.name} got {self.marks} ")

# Create the isinstance
student1 = Student("Hamza Ahmed" , 67)
student2 = Student("Saad Qureshi", 93)

# Call the class method to display the student info
student1.display()
student2.display()