"""

10. Instance Methods
Assignment:
Create a class Dog with instance variables name and breed.
Add an instance method bark() that prints a message including the dog's name.
"""

# Create dog class
class Dog:
    def __init__(self ,name:str, breed:str) -> None:
        self.name = name      # instance variable
        self.breed = breed

     # instance method
    def bark(self):
        print(f"{self.name} says woof woof! and it's breed {self.breed}  ")
        

# Create the instance of the dog class
dog : Dog = Dog("Buddy","Golden Retriever")

# "Call the bark method"
dog.bark()