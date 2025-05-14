
"""
13. Composition
Assignment:
Create a class Engine and a class Car. 
Use composition by passing an Engine object to the Car class during initialization. 
Access a method of the Engine class via the Car class.

"""
class Engine:
    def start(self) -> None:
        print("Engine started.")

class Car:
    def __init__(self, engine: Engine) -> None:
        self.engine = engine  # Composition

    def start_car(self) -> None:
        print("Starting car...")
        self.engine.start()  # Access Engine method via Car

# Example usage
engine = Engine()
car = Car(engine)
car.start_car()

