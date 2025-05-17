
"""
20. Creating a Custom Exception
Assignment:
Create a custom exception InvalidAgeError. 
Write a function check_age(age)
 that raises this exception if age < 18. Handle it with try...except .

"""

# step 1 : Create a custome exception
class InvalidAgeException(Exception):
    """Custome exception for invalid age"""
    pass

# step 2 : Define a function to check the age
def check_age(age):
    if age < 18 :
        raise InvalidAgeException("Age must be at least 18 to proceed")
    else:
        print("Access granted")

# step 3 : To handle the exception
try:
    age_input = int(input("Enter your age : "))
    check_age(age_input)
except InvalidAgeException as e:
    print(f'InvalidAgeError : \n {e}')
except ValueError:
    print("Please enter a valid number")