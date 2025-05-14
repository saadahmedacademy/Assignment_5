
"""
12. Static Methods
Assignment:
Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) 
that returns the Fahrenheit value.

"""

class Temperature_converter:
    # Static method
    # In statice method we don't use self or other keyword
    @staticmethod
    def celsius_to_fahrenheit(c:float) -> float:
        return (c * 9/5) * 32
    
# we don't need to create instance to access the static method of any class
celsius = input("Enter celsius to convert into fahrenheit : ")
fehrenheit = Temperature_converter.celsius_to_fahrenheit(float(celsius))
print(f"{celsius} celsius = {fehrenheit} fehrenheit")

    

        