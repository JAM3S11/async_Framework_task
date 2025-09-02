# async_Framework_task

## Overview

This repository contains a Python Object-Oriented Programming (OOP) assignment as part of the async Framework Task for the PLP program. The goal is to demonstrate a fundamental understanding of classes, attributes, and methods in Python by modeling a simple `Person` entity.

## Assignment Instructions

1. **Create a Python class named `Person`**  
   - The `Person` class should represent an individual with basic characteristics.

2. **Define the following attributes in the `Person` class:**  
   - `name`: A string representing the person's name.
   - `age`: An integer representing the person's age.
   - `gender`: A string representing the person's gender.

3. **Implement a method called `introduce`**  
   - The `introduce` method should print a message that introduces the person, including their name, age, and gender in a user-friendly format.

4. **Create an instance of the `Person` class**  
   - Instantiate the class with sample data.
   - Call the `introduce` method to display the information about the person.

5. **Repository Submission**  
   - Create a GitHub repository for your assignment.
   - Submit the repository link as part of your assignment submission.

## Example

Here is an example of how your code structure might look:

```python
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello! My name is {self.name}, I am {self.age} years old, and I identify as {self.gender}.")

# Creating an instance and displaying information
person1 = Person("Alice", 30, "Female")
person1.introduce()
```

## How to Use

1. Clone the repository:
    ```bash
    git clone https://github.com/JAM3S11/async_Framework_task.git
    ```
2. Open the Python file containing the `Person` class (e.g., `person.py`).
3. Run the file using Python:
    ```bash
    python person.py
    ```

## Purpose

This exercise is designed to reinforce your understanding of Python classes and object instantiation, encouraging clean, readable, and well-structured code. Feel free to extend the assignment by adding more attributes or methods to the `Person` class for additional practice.

---
**Author:** JAM3S11  
