# Python OOP Assignments

This repository contains solutions to Python Object-Oriented Programming (OOP) assignments from basic concepts to advanced features including decorators, inheritance, and custom exceptions.

---

## Table of Contents

1. [Using `self`](#1-using-self)
2. [Using `cls`](#2-using-cls)
3. [Public Variables and Methods](#3-public-variables-and-methods)
4. [Class Variables and Class Methods](#4-class-variables-and-class-methods)
5. [Static Variables and Static Methods](#5-static-variables-and-static-methods)
6. [Constructors and Destructors](#6-constructors-and-destructors)
7. [Access Modifiers](#7-access-modifiers-public-private-and-protected)
8. [The `super()` Function](#8-the-super-function)
9. [Abstract Classes and Methods](#9-abstract-classes-and-methods)
10. [Instance Methods](#10-instance-methods)
11. [Class Methods](#11-class-methods)
12. [Static Methods](#12-static-methods)
13. [Composition](#13-composition)
14. [Aggregation](#14-aggregation)
15. [Method Resolution Order (MRO)](#15-method-resolution-order-mro-and-diamond-inheritance)
16. [Function Decorators](#16-function-decorators)
17. [Class Decorators](#17-class-decorators)
18. [Property Decorators](#18-property-decorators-property-setter-and-deleter)
19. [`callable()` and `__call__()`](#19-callable-and-__call__)
20. [Creating a Custom Exception](#20-creating-a-custom-exception)
21. [Make a Custom Class Iterable](#21-make-a-custom-class-iterable)

---

### 1. **Using `self`**

Create a class `Student` with attributes `name` and `marks`. Use the `self` keyword to initialize these values via a constructor. Add a method `display()` to print the student details.

---

### 2. **Using `cls`**

Create a class `Counter` that keeps track of how many objects have been created. Use a class variable and a class method with `cls` to manage and display the count.

---

### 3. **Public Variables and Methods**

Create a class `Car` with a public variable `brand` and a public method `start()`. Instantiate the class and access both from outside the class.

---

### 4. **Class Variables and Class Methods**

Create a class `Bank` with a class variable `bank_name`. Add a class method `change_bank_name(cls, name)` that allows changing the bank name. Show that it affects all instances.

---

### 5. **Static Variables and Static Methods**

Create a class `MathUtils` with a static method `add(a, b)` that returns the sum. No class or instance variables should be used.

---

### 6. **Constructors and Destructors**

Create a class `Logger` that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).

---

### 7. **Access Modifiers: Public, Private, and Protected**

Create a class `Employee` with a public variable `name`, a protected variable `_salary`, and a private variable `__ssn`. Try accessing all three variables from an object of the class and document the behavior.

---

### 8. **The `super()` Function**

Create a class `Person` with a constructor that sets the name. Inherit a class `Teacher` from it, add a subject field, and use `super()` to call the base class constructor.

---

### 9. **Abstract Classes and Methods**

Use the `abc` module to create an abstract class `Shape` with an abstract method `area()`. Inherit a class `Rectangle` that implements `area()`.

---

### 10. **Instance Methods**

Create a class `Dog` with instance variables `name` and `breed`. Add an instance method `bark()` that prints a message including the dog's name.

---

### 11. **Class Methods**

Create a class `Book` with a class variable `total_books`. Add a class method `increment_book_count()` to increase the count when a new book is added.

---

### 12. **Static Methods**

Create a class `TemperatureConverter` with a static method `celsius_to_fahrenheit(c)` that returns the Fahrenheit value.

---

### 13. **Composition**

Create a class `Engine` and a class `Car`. Use composition by passing an `Engine` object to the `Car` class during initialization. Access a method of the `Engine` class via the `Car` class.

---

### 14. **Aggregation**

Create a class `Department` and a class `Employee`. Use aggregation by having a `Department` object store a reference to an `Employee` object that exists independently of it.

---

### 15. **Method Resolution Order (MRO) and Diamond Inheritance**

Create four classes: `A` with a method `show()`, `B` and `C` that inherit from `A` and override `show()`, and `D` that inherits from both `B` and `C`. Create an object of `D` and call `show()` to observe MRO.

---

### 16. **Function Decorators**

Write a decorator function `log_function_call` that prints "Function is being called" before a function executes. Apply it to a function `say_hello()`.

---

### 17. **Class Decorators**

Create a class decorator `add_greeting` that modifies a class to add a `greet()` method returning "Hello from Decorator!". Apply it to a class `Person`.

---

### 18. **Property Decorators: `@property`, `@setter`, and `@deleter`**

Create a class `Product` with a private attribute `_price`. Use `@property` to get the price, `@price.setter` to update it, and `@price.deleter` to delete it.

---

### 19. **`callable()` and `__call__()`**

Create a class `Multiplier` with an `__init__()` to set a factor. Define a `__call__()` method that multiplies an input by the factor. Test it with `callable()` and by calling the object like a function.

---

### 20. **Creating a Custom Exception**

Create a custom exception `InvalidAgeError`. Write a function `check_age(age)` that raises this exception if `age < 18`. Handle it with `try...except`.

---

### 21. **Make a Custom Class Iterable**

Create a class `Countdown` that takes a start number. Implement `__iter__()` and `__next__()` to make the object iterable in a for-loop, counting down to 0.

---
## Good luck! 🚀
