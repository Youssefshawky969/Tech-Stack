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

## What is Data Types?

In Python programming, a data type defines the kind of value stored in a variable.

When a variable is created, Python automatically determines the type of data stored inside it.

Data types are important because they determine how values are stored, processed and used inside a Python program

For example, numbers can be used for mathematical calculations, text can be used for messages or user input, and boolean values can represent logical conditions.

Python provides several built-in data types. In this beginner lesson we will focus on the most important atomic data types:

- Integer (int)
- Float (float)
- String (str)
- Boolean (bool)

### Checking the Data Type of a Variable

Python provides a built-in function called type() that allows you to check the data type of a variable.

```python
x = 10

print(type(x))
```
This shows that the variable `x` contains an integer value.

### Integer Data Type (int)

The integer data type represents whole numbers. Integers can be positive numbers, negative numbers, or zero.

Example: Integer Values

```python
age = 25
year = 2024
temperature = -5

print(age)
print(year)
print(temperature)
```

Example: Integer Calculations

```python
a = 10
b = 5

sum = a + b

print(sum)
```

### Float Data Type (float)

A float represents numbers that contain a decimal point. 

These numbers are used when more precise values are required.

```python
price = 19.99
height = 5.8
temperature = -2.5

print(price)
print(height)
print(temperature)
```

Example: Float Calculation

```python
a = 5.5
b = 2.5

result = a + b

print(result)
```

### String Data Type (str)

A string represents text in Python. Strings are written inside quotation marks.

Strings can use either single quotes or double quotes.

Example: String Values

```python
name = "Alice"
course = "Python Programming"
city = "London"

print(name)
print(course)
print(city)
```

Example: Combining Strings

```python
first_name = "Alice"
last_name = "Smith"

full_name = first_name + " " + last_name

print(full_name)
```

```python
first_name = "Alice"
last_name = "Smith"

print (f"{first_name} {last_name}")
```

This process is called string concatenation.

### Boolean Data Type (bool)

The boolean data type represents logical values. A boolean value can only be either **True** or **False**.

Boolean values are commonly used in conditions, decision making and program control structures such as `if` statements.

Example: Boolean Values

```python
is_student = True
is_logged_in = False

print(is_student)
print(is_logged_in)
```

Example: Boolean from Comparison

```python
x = 10
y = 5

print(x > y)
```


## How to Input and Output in python?

In programming, input and output allow a program to communicate with users. 

Input allows the user to provide data to the program, while output allows the program to display results.

Python provides simple built-in functions for performing input and output operations. The two most important functions are:

- print() – used to display output
- input() – used to receive input from the user

### Python Output Using the print() Function

The `print()` function is used to display information on the screen. It is one of the most commonly used functions in Python.

Example: Printing Text

```python
print("Hello Python")
```

In this example, the program prints the message `Hello Python` on the screen.

Example: Printing Multiple Values

```python
name = "Alice"
age = 25

print(name)
print(age)
```

Example: Printing Multiple Items in One Statement

```python
name = "Alice"
age = 25

print("Name:", name)
print("Age:", age)
```

### Python Input Using the input() Function

The `input()` function allows a program to receive data from the user. When Python executes this function, the program pauses and waits for the user to type something.

The value entered by the user is stored as a string.

Example: Basic User Input

```python
name = input("Enter your name: ")

print("Hello", name)
```

In this example:
- The program asks the user to enter their name.
- The value entered by the user is stored in the variable name.
- The program then prints a greeting message.

#### Receiving Numeric Input

The `input()` function always returns text. 

If a program needs numbers, the input must be converted using functions such as `int()` or `float()`.

Example: Converting Input to Integer

```python
age = int(input("Enter your age: "))

print("Your age is", age)
```

