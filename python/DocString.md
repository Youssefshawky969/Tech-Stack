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

## Exploring Docstring Formats in Python

While the structure of your docstrings may depend on your preference, certain conventions have emerged that standardize the way they’re written.

These docstring formats help with staying consistent and allow automated tools like Sphinx and pydoc to parse docstrings and generate navigable documentation websites.

Following a structured format could turn your plain text comments into full-featured developer documentation.

Some of the most widely used of these formats are the following:

- reStructuredText docstrings
- Google-style docstrings
- NumPy-style docstrings
- Doctest-style docstrings

It’s important to learn the nuances of each of these formats so you can make the right choice for your Python projects.

### reStructuredText Docstrings

reStructuredText—often abbreviated as reST—is a lightweight markup language used for writing plain text.

It’s the default formatting style for inline documentation in Python, as outlined in PEP 287, and is used with tools like Sphinx to generate documentation.

When you write docstrings in reST, you need to include specific elements such as **parameter names**, **type names**, **return value descriptions**, and **return types**.

You can also add **headers**, **lists**, and **links** to improve the structure.

While reST is slightly more technical than other formats, it offers precision and can render documentation into beautiful HTML or PDFs.

Here’s a magic-infused reST docstring example for a function:

```python
def cast_spell(wand, incantation, target=None):
    """
    Cast a magical spell using a wand and incantation.
    This function simulates casting a spell. With no
    target specified, it is cast into the void.

    :param wand: The wand used to do the spell-casting deed.
    :type wand: str
    :param incantation: The words said to activate the magic.
    :type incantation: str
    :param target: The object or person the spell is directed at (optional).
    :return: A string describing the result of the spell.
    :rtype: str

    :raises ValueError: If the incantation is unknown or the wand fails to work.
    """
    valid_incantations = ["Lumos", "Alohomora", "Expelliarmus"]
    if not wand:
        raise ValueError("You can't cast spells without a wand!")
    if incantation not in valid_incantations:
        raise ValueError("Incantation not recognized.")
    if target:
        return f"{incantation} hits {target} with magic speed!"
    return f"{incantation} is cast into the void...sparkles shimmer faintly"
```

### Google-Style Docstrings

Google-style docstrings provide a clean, structured way to document your code, especially when it’s concerned with multiple parameters or returns complex values.

They became popular through Google’s Python projects and other large codebases.

To illustrate, imagine casting a spell that allows users to retrieve magical items with ease.

For such a program, a Google-style docstring might look like this:

```python
def get_magic_items(user_id, include_potions=False):
    """
    Retrieve a list of magical items for a specific user.

    Args:
        user_id (int): The ID of the user whose items should be retrieved.
        include_potions (bool, optional): Whether to include potions.

    Returns:
        list[str]: A list of item names associated with the user.
    """
    items = ["wand", "cloak", "crystal ball"]
    if include_potions:
        items.extend(["healing potion", "invisibility potion"])
    return items
```

In this format, `Args` lists parameters and their descriptions, `Returns` describes the return value and its type, and Raises (when included) shows exceptions that might be raised by the function.

Google-style docstrings shine when you need a detailed, consistent structure—especially if you’re collaborating on large projects or using documentation generators like Sphinx.

### NumPy-Style Docstrings

The NumPy style of docstrings is favored in scientific and data-oriented Python projects.

It uses sections with headers underlined by dashes to clearly distinguish different parts of the docstring.

Here’s a NumPy-style docstring in action:

```python
def brew_potion(ingredients, heat_level):
    """
    Brew a potion using selected ingredients and heat.

    Parameters
    ----------
    ingredients : list of str
        A list of magical ingredients.
    heat_level : int
        The intensity of the heat used for brewing.

    Returns
    -------
    str
        A description of the brewed potion.
    """
    return f"A sparkling blue elixir of friendship heated at {heat_level}."
```

This style places emphasis on headers such as parameters, examples, and returns.

It’s mostly used in academic and scientific circles with libraries like NumPy, pandas, and SciPy.

You may find NumPy-style docstrings to be an attractive choice when writing programs for data analysis, scientific computing, or any project that requires detailed, well-formatted documentation.

### Doctest-Style Docstrings

The doctest-style docstring stands out among the common formats because it accomplishes two things at the same time:
- it documents your code and acts as a lightweight automated test suite.
-  When you include example code in the docstring, the `doctest` module verifies the examples you’ve written as part of your tests.

The built-in `doctest` module ensures that the function behaves as expected.

You essentially write examples in the same way they would be typed in the Python shell, and `doctest` confirms if the output matches.

In the example below, a spell to undo other spells is documented so you can see the doctest format in action:

```python
def undo_spell(spell):
    """
    Reverses characters in a spell incantation, thereby undoing a spell.

    Example:
    >>> undo_spell("Expelliarmus")
    'sumraillepxE'

    >>> undo_spell("Lumos")
    'somuL'
    """
    return spell[::-1]
```

After typing out the docstring as shown above, you could run it as a test by entering it in your terminal like this:

```bash
$ python -m doctest magic_spells.py
```
This assumes that your file is named `magic_spells.py`.

If your function returns something that isn’t expected based on your docstring, then `doctest` would raise an error.



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

### Docstrings for Classes

Class-level docstrings describe the overall purpose of a class, its attributes, and public methods.

With class-level docstrings, you generally include a summary of the class’s purpose at the top of the class definition, as in the example below:

```python
class Potion:
    """
    Represents a magical potion composed of various ingredients.

    Attributes
    ----------
    name : str
        The name of the potion.
    ingredients : list of str
        A list of ingredients used in the potion.
    potency : int
        The strength level of the potion.

    Methods
    -------
    brew():
        Completes the potion and sets its potency.
    describe():
        Returns a human-readable summary of the potion.
    """

    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients
        self.potency = 0

    def brew(self):
        """Simulate brewing the potion by calculating potency."""
        self.potency = len(self.ingredients) * 10

    def describe(self):
        """Return a string describing the potion and its strength."""
        return f"{self.name} (Potency: {self.potency})"
```


