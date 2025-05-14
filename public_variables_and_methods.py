"""
3. Public Variables and Methods
Assignment:
Create a class Car with a public variable brand and a public method start().
 Instantiate the class and access both from outside the class.

"""

class Car:
    def __init__(self, brand):
        self.brand = brand  # public variable

    def start(self):  # public method
        print(f"{self.brand} is starting...")

# Instantiate the class
my_car = Car("Toyota")

# Access the public variable
print("Car brand:", my_car.brand)

# Access the public method
my_car.start()
