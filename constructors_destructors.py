
"""
6. Constructors and Destructors
Assignment:
Create a class Logger that prints a message
 when an object is created (constructor) and another message when it is destroyed (destructor).
"""

# Create class
class Logger:
    def __init__(self) -> None:
        print("Logger object created")

    def __del__(self) ->None:
        print("Logger object has destroyed")

# Create an object
logger : Logger = Logger()
logger

# Manually delete the object
del logger