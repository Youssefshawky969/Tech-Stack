## What is Python Syntax?

Syntax in programming refers to the rules that define how code must be written so that the computer can understand it.

Just like grammar rules exist in natural languages, programming languages also have syntax rules.

Some important characteristics of Python syntax include:
- Python uses indentation instead of braces to define code blocks.
- Python statements are usually written one per line
- Python code is designed to be easy to read and maintain

### Python Statements

A Python statement is a line of code that performs a specific action.

Python programs are made up of multiple statements that are executed by the Python interpreter.

Example 1: Simple Python Statement

```python
print("Hello Python")
```

- print() is a built-in Python function
- The function displays text inside the parentheses
- When this statement runs, it prints the message on the screen

Example 2: Multiple Python Statements

```python
name = "Alice"
age = 25

print(name)
print(age)
```

- The first two lines assign values to variables
- The print statements display those values
- Each line is a separate Python statement

### Python Indentation

One of the most important rules of Python syntax is indentation.

Unlike many other programming languages that use braces to define blocks of code, Python uses indentation.

**Indentation means adding spaces at the beginning of a line to indicate that it belongs to a specific block of code**

Example 1: If Statement with Indentation

```python
age = 20

if age > 18:
    print("You are an adult")
```

- The if statement checks a condition
- The indented line belongs to the if block
- Python requires proper indentation for this structure

Example 2: Incorrect Indentation

```python
age = 20

if age > 18:
print("You are an adult")
```
This code will produce an IndentationError because the print statement is not indented correctly.

### Python Code Structure

Python programs are usually structured using statements, functions and modules.

Even small Python programs follow a logical structure to make them easier to read and maintain.

Example 1: Simple Python Program

```python
name = "Alice"

print("Hello", name)
```

- The program starts by defining a variable
- The print function then displays the value
- This is a simple two-statement Python program

Example 2: Python Program with Logic

```python
number = 10

if number > 5:
    print("Number is greater than 5")
```

- The variable number stores a value
- The if statement checks a condition
- If the condition is true, the message is printed

### Case Sensitivity in Python

Python is a case-sensitive programming language.

This means that uppercase and lowercase letters are treated as different.

Example 1:

```python
name = "Alice"
Name = "Bob"

print(name)
print(Name)
```

These variables are considered different because their names use different letter cases.

Example 2:

```python
age = 20
Age = 30
```
Python treats age and Age as two separate variables.


## What is a Python Variable?

A variable is a name that refers to a value stored in memory.

When a value is assigned to a variable, Python stores that value and allows the program to access it later using the variable name.

Think of variables like labeled boxes. The label is the variable name and the box contains the stored value.

### Creating Variables in Python

Python makes creating variables very simple. 

Unlike some other programming languages, you do not need to declare the type of the variable before assigning a value.

A variable is created automatically when a value is assigned to it.

Example: Creating Variables

```python
name = "Alice"
age = 25

print(name)
print(age)
```
- The variable `name` stores the text "Alice".
- The variable `age` stores the number 25.
- The `print()` function displays the values.

### Variables Can Store Different Types of Data

Python variables can store many different types of data including text, numbers and Boolean values.

Python automatically determines the data type based on the value.

Example: Different Data Types

```python
name = "Alice"
age = 25
height = 5.6
is_student = True

print(name)
print(age)
print(height)
print(is_student)
```
- `name` stores a string value.
- `age` stores an integer.
- `height` stores a decimal number.
- `is_student` stores a Boolean value.

### Changing the Value of a Variable

The value stored in a variable can be changed during program execution.

This is why they are called variables — their values can vary.

Example: Updating Variables

```python
age = 25

print(age)

age = 30

print(age)
```
The value of the variable `age` changes from 25 to 30.

### Rules for Naming Python Variables

When creating variables in Python, certain naming rules must be followed.

- Variable names must start with a letter or underscore.
- Variable names cannot start with a number.
- Variable names can contain letters, numbers and underscores.
- Python variable names are case sensitive.

#### Valid Variable Names

```python
name = "Alice"
_age = 20
student1 = "John"
```
#### Invalid Variable Names

```python
1name = "Alice"
student-name = "John"
```
These examples will produce errors because the names violate Python's naming rules.

