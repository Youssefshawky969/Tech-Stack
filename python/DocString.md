## How to Write Docstrings in Python

Writing clear, consistent docstrings in Python helps others understand your code’s purpose, parameters, and outputs.

Python docstrings are string literals that show information regarding Python functions, classes, methods, and modules, allowing them to be properly documented.

They are placed immediately after the definition line in triple double quotes (`"""`).

Their use and convention are described in PEP 257, which is a Python Enhancement Proposal (PEP) that outlines conventions for writing docstrings. Docstrings don’t follow a strict formal style. Here’s an example:

```python
def determine_magic_level(magic_number):
    """
    Multiply a wizard's favorite number by 3 to reveal their magic level.
    """
    return magic_number * 3
```

Docstrings are a built-in means of documentation.

While this may remind you of comments in Python, docstrings serve a distinct purpose.

see a quick breakdown of the differences:

|  Comments  |  Docstrings |
|------------|-------------|
| Begin with `#` | Are enclosed in triple quotes (`"""`)  |
| Consist of notes and reminders written by developers for other developers | Provide documentation for users and tools |
| Are ignored by the Python interpreter | Are stored in `.__doc__` and accessible at runtime |
| Can be placed anywhere in code | Are placed at the start of modules, classes, and functions |

So, while comments and docstrings may look similar at first glance, their purpose and behavior in Python are different.

## One-Line vs Multiline Docstrings

Docstrings are generally classified as either one-line or multiline. 

As the names suggest, one-line docstrings take up only a single line, while multiline docstrings span more than one line.

An important formatting rule from PEP 257 is that one-line docstrings should be concise.

while multiline docstrings should have their closing quotes on a new line.

You may resort to a one-line docstring for relatively straightforward programs like the one below:

```python
import random

def picking_hat():
    """Return a random house name."""
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    return random.choice(houses)
```

In this example, you see a program that returns a random house as depicted in the classic Harry Potter stories. This is a good example for the use of one-line docstrings.

You use multiline docstrings when you have to provide a more thorough explanation of your code, which is helpful for other developers.

Generally, a docstring should contain parameters, return value details, and a summary of the code.

You’re free to format docstrings as you like. 

That being said, you’ll learn later that there are common docstring formats that you may follow. Here’s an example of a multiline docstring:

```python
def get_harry_potter_book(publication_year, title):
    """
    Retrieve a Harry Potter book by its publication year and name.

    Parameters:
    publication_year (int): The year the book was published.
    title (str): The title of the book.

    Returns:
    str: A sentence describing the book and its publication year.
    """
    return f"The book {title!r} was published in the year {publication_year}."
```

## Ways to Access Docstrings in Python

docstrings aren’t ignored by the interpreter.

They become a part of the program and serve as associated documentation for anyone who wants to understand your program and what it does.

Python provides two built-in ways to access docstrings: the `.__doc__` attribute and the `help()` function.

### The `.__doc__` Attribute

Say you wanted to access the documentation for the math module.

 You could do so in the following way:

 ```python
>>> import math
>>> print(math.__doc__)
This module provides access to the mathematical functions
defined by the C standard.
```

To illustrate further, you could try accessing the `.__doc__` attribute for the `get_harry_potter_book()` function from the previous example, which would generate this:

```python
>>> from multiline_docstring import get_harry_potter_book
>>> print(get_harry_potter_book.__doc__)

Retrieve a Harry Potter book by its publication year and name.

Parameters:
publication_year (int): The year the book was published.
title (str): The title of the book.

Returns:
str: A sentence describing the book and its publication year
```

As you can see, using `.__doc__` gives you information about an object at a glance. However, if you’re looking to obtain more robust documentation, then you can use the `help()` function.

### The help() Function

The built-in `help()` function in Python provides interactive access to an object’s documentation, including more detailed metadata than what’s available through the `.__doc__` attribute alone.

For example, you can retrieve more thorough documentation of the `math` module by running the following code:

```python
>>> import math
>>> help(math)
Help on built-in module math:

NAME
    math

DESCRIPTION
    This module provides access to the mathematical functions
    defined by the C standard.

FUNCTIONS
    acos(x, /)
        Return the arc cosine (measured in radians) of x.

        The result is between 0 and pi.

    acosh(x, /)
        Return the inverse hyperbolic cosine of x.
-- More --
```

You can also use help() with your own functions that include either one-line or multiline docstrings.

This is a great way to see how your documentation reads from the perspective of someone using your code for the first time.

### The pydoc Tool

Python includes a powerful built-in documentation tool called `pydoc` that can display and generate documentation from your docstrings.

To illustrate, imagine you have a file named `magical_characters.py` that contains the following docstring:

```python
"""A module for adding and listing magical characters."""

def add_characters(magical_being):
    """Add a new magical character."""
    return f"You've added {magical_being} to the magical beings record"

if __name__ == "__main__":
    print(add_characters("Gandalf"))
```

You can use `pydoc` to view the documentation for the `magical_characters` module directly in your terminal.

Make sure you’re in the same directory as `magical_characters.py` and run the following command to display the formatted documentation:

```bash
$ python -m pydoc magical_characters

Help on module magical_characters:

NAME
    magical_characters - A module for adding and listing magical characters.

FUNCTIONS
    add_characters(magical_being)
        Add a new magical character.

FILE
    /Users/rp/projects/python-docstrings/magical_characters.py
```

You can even create HTML documentation that can be viewed in a browser by adding a `-w` flag, which is short for “write”.

The HTML file will inherit its name from the `magical_characters` module name that you pass in:

```bash
$ python -m pydoc -w magical_characters
wrote magical_characters.html
```

## Writing Effective Docstrings

A good analogy for an effective docstring is a well-drawn road map that tells you where to go while on vacation in a foreign country.

### Docstrings for Modules

When you write docstrings for modules, the goal is to provide a high-level summary of what the program does.

This appears at the top of your Python file and serves as an overview of its contents.

Here, you’ll add a brief description of the module’s purpose and a list of its components. 

You could also add references to related modules or examples of usage. Check out the example below:

```python
"""
This module provides tools for creating and managing magical maps.

Example:
    from navigation import build_map
    build_map(["mandrake", "phoenix feather", "tree bark"], heat_level=3)
"""
```

It’s especially helpful if you use clear, concise descriptions and relevant examples to make it easier for readers to understand and use your module.

### Docstrings for Functions

Functions are common in most codebases, so writing clear and informative docstrings for them is essential. 

A good function docstring should provide a summary of what the function does, along with details about its parameters, return values, and exceptions, if any

 Here’s an example:

 ```python
def enchant_wand(wand_type, level=1):
    """
    Enhance a wand with magical properties.

    Args:
        wand_type (str): The type of wand to enchant.
        level (int, optional): The enchantment level. Defaults to 1.

    Returns:
        str: A message confirming the enchantment.

    Raises:
        ValueError: If the enchantment level is invalid.
    """
    if level < 1:
        raise ValueError("Enchantment level must be at least 1.")
    return f"{wand_type.title()} enchanted to level {level}!"
```

When you write multiline docstrings, you should always follow a one-line summary—in the imperative verb form—with a blank line. 

Also, don’t shy away from examples and clearly describe any exceptions and arguments, as shown above.

