"""

2. Using cls
Assignment:
Create a class Counter that keeps track of how many objects have been created.
 Use a class variable and a class method with cls to manage and display the count.
"""

class Counter:
      # class variable to track number of objects
    count = 0

    def __init__(self) -> None:
        # increament a count whenever an object create
        Counter.count += 1
    @classmethod
    def display_count(cls):
        print(f"The total count of created objects {cls.count}")


# Now created objects
obj1 = Counter()
obj2 = Counter()
obj1 = Counter()

# Access class method
Counter.display_count()