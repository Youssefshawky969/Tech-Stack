## How to Write Beautiful Python Code With PEP 8

PEP 8, sometimes spelled PEP8 or PEP-8, is the official style guide for Python code.

PEP 8 gives guidelines on naming conventions, code layout, and other best practices. 

PEP stands for Python Enhancement Proposal, and there are many PEPs. 

 These documents primarily describe new features proposed for the Python language, but some PEPs also focus on design and style and aim to serve as a resource for the community.

 PEP 8 is one of these style-focused PEPs.

 If you follow PEP 8, you can be sure that you’ve named your variables well. 
 
 You’ll know that you’ve added enough whitespace so it’s easier to follow logical steps in your code. 
 
 You’ll also have commented your code well. All of this will mean your code is more readable and easier to come back to.

 ### Naming Conventions

 When you write Python code, you have to name a lot of things: variables, functions, classes, packages, and so on.

 Choosing sensible names will save you time and energy later.

 You’ll be able to figure out, from the name, what a certain variable, function, or class represents.

 You’ll also avoid using potentially confusing names that might result in errors that are difficult to debug.

 One suggestion is to never use l, O, or I single letter names as these can be mistaken for 1 and 0, depending on what typeface a programmer uses.

 ```python
O = 2  # ❌ Not recommended
```

Doing this may look like you’re trying to reassign 2 to zero. 

While making such a reassignment isn’t possible in Python and will cause a syntax error.

using an ambigious variable name such as O can make your code more confusing and harder to read and reason about.

### Naming Styles

|Type|Naming Convention|Examples|
|----|-----------------|--------|
|Function|Use a lowercase word or words. Separate words by underscores to improve readability. This style is called snake case.	| function, python_function|
|Variable|Use a lowercase single letter, word, or words. Separate words with underscores to improve readability.| x, var, python_variable|
|Class|Start each word with a capital letter. Don’t separate words with underscores. This style is called camel case or Pascal case.| Model, PythonClass|
|Method|Use a lowercase word or words. Separate words with underscores to improve readability (snake case).| class_method, method|
|Constant|Use an uppercase single letter, word, or words. Separate words with underscores to improve readability.|CONSTANT, PYTHON_CONSTANT, PYTHON_LONG_CONSTANT|
|Module|Use a short, lowercase word or words. Separate words with underscores to improve readability.| module.py, python_module.py|
|Package|Use a short, lowercase word or words. Don’t separate words with underscores.| package, pythonpackage|

These are some of the common naming conventions and examples of how to use them.

But in order to write readable code, you still have to be careful with your choice of letters and words.

In addition to choosing the correct naming styles in your code, you also have to choose the names carefully.

### How to Choose Names

When naming variables, you may be tempted to choose simple, single-letter lowercase names, like `x`

But unless you’re using x as the argument of a mathematical function, it’s not clear what `x` represents. 

Imagine you’re storing a person’s name as a string, and you want to use string slicing to format their name differently.

You could end up with something like this:(❌ Not recommended)

```python
>>> x = "John Smith"
>>> y, z = x.split()
>>> print(f"{z}, {y}")
'Smith, John'
```

This will work, but you’ll have to keep track of what x, y, and z represent.

It may also be confusing for collaborators. 

A much clearer choice of names would be something like this: (✅ Recommended)

```python
>>> name = "John Smith"
>>> first_name, last_name = name.split()
>>> print(f"{last_name}, {first_name}")
'Smith, John'
```

Similarly, to reduce the amount of typing you do, it can be tempting to use abbreviations when choosing names. 

In the example below, you defined a db() function that takes a single argument, x, and doubles it: ❌ Not recommended

```python
def db(x):
    return x * 2
```

At first glance, this could seem like a sensible choice.

 The name db() could be an abbreviation for double.

 But imagine coming back to this code in a few days. You may have forgotten what you were trying to achieve with this function, and that would make guessing how you abbreviated it difficult.

 The following example is much clearer. If you come back to this code a couple of days after writing it, you’ll still be able to read and understand the purpose of this function: ✅ Recommended

 ```python
def multiply_by_two(x):
    return x * 2
```

The same philosophy applies to all other data types and objects in Python. Always try to use the most concise but descriptive names possible.

### Code Layout

How you lay out your code has a huge role in how readable it is.

you’ll learn how to add vertical whitespace to improve the readability of your code. You’ll also learn how to handle the 79-character line limit recommended in PEP 8.

#### Blank Lines

Vertical whitespace, or blank lines, can greatly improve the readability of your code. Code that’s bunched up together can be overwhelming and hard to read.

Similarly, too many blank lines in your code makes it look very sparse, and the reader might need to scroll more than necessary.

Below are three key guidelines on how to use vertical whitespace.

**Surround top-level functions and classes with two blank lines** Top-level functions and classes should be fairly self-contained and handle separate functionality.

It makes sense to put extra vertical space around them, so that it’s clear they are separate:

```python
class FirstClass:
    pass


class SecondClass:
    pass


def top_level_function():
    return None
```

Therefore, PEP 8 suggests surrounding top-level functions and class definitions with two blank lines.

**Surround method definitions inside classes with a single blank line**

Methods inside a class are all related to one another. It’s good practice to leave only a single line between them:

```python
class ClassWithMethods:
    def first_method(self):
        return None

    def second_method(self):
        return None
```

In the code example, you can see a class definition with two instance methods that are separated from one another with a single blank line.


**Use blank lines sparingly inside functions to show clear steps** 

Sometimes, a complicated function has to complete several steps before the `return` statement. 

To help the reader understand the logic inside the function, you can leave a blank line between each logical step.

In the example below, there’s a function to calculate the variance of a list. This is two-step problem, so you can indicate the two separate steps by leaving a blank line between them:

```python
def calculate_variance(numbers):
    sum_numbers = 0
    for number in numbers:
        sum_numbers = sum_numbers + number
    mean = sum_numbers / len(numbers)

    sum_squares = 0
    for number in numbers:
        sum_squares = sum_squares + number**2
    mean_squares = sum_squares / len(numbers)

    return mean_squares - mean**2
```

In this code example, you separated the logical steps with a blank line in between them to improve readability.

There is also a blank line before the `return` statement.

This helps the reader clearly see what the function returns.

#### Maximum Line Length and Line Breaking

PEP 8 suggests lines should be limited to 79 characters.

This allows you to have multiple files open next to one another, while also avoiding line wrapping.

Of course, keeping statements to 79 characters or fewer isn’t always possible. Therefore, PEP 8 also outlines ways to allow statements to run over several lines.

Python will assume line continuation if code is contained within parentheses, brackets, or braces:

```pytohn
def function(arg_one, arg_two,
             arg_three, arg_four):
    return arg_one
```

In this example, you moved arg_three and arg_four onto a new line, indented at the same level as the first argument. 

You can split your code like that because of Python’s implicit line joining inside of parentheses.


If it’s impossible to use implied continuation, then you can use backslashes (\) to break lines instead:

```python
from package import example1, \
    example2, example3
```

However, any time that you can use implied continuation, then you should prefer that over using a backslash.

If you need to break a line around binary operators, like `+` and `*`, then you should do so before the operator.

This rule stems from mathematics. Mathematicians agree that breaking before binary operators improves readability.

Below is an example of breaking before a binary operator: ✅ Recommended

```python
total = (first_variable
         + second_variable
         - third_variable)
```


You can immediately see which variable Python will add or subtract, as the operator is right next to the variable it operates on.

Now, here’s an example of breaking after a binary operator: (❌ Not recommended)

```python
total = (first_variable +
         second_variable -
         third_variable)
```
Here, it’s harder to see which variable Python is adding and which one it’s subtracting.


### Indentation

Indentation, or leading whitespace, is extremely important in Python. 

The indentation level of lines of code in Python determines how Python groups statements together.

Consider the following example:

```python
x = 3
if x > 5:
    print("x is larger than 5")
```

The indented call to `print()` lets Python know that it should only execute this line if the `if` statement returns `True`.

The same indentation applies to tell Python what code to execute when you’re calling a function or what code belongs to a given class.

The key indentation rules laid out by PEP 8 are the following:
- Use four consecutive spaces to indicate indentation.
- Prefer spaces over tabs.

While Python code will work with any amount of consistent indentation, four spaces is a widespread convention in the Python community, and you should stick to it as well.

#### Tabs vs Spaces

As mentioned above, you should use spaces instead of tabs when indenting your code.

You can adjust the settings in your text editor to output four spaces instead of a tab character when you press the `Tab` key.

Python 3 doesn’t allow mixing of tabs and spaces. Write the following code and make sure to use spaces where indicated with a dot (·) and a tab character where you can see the (⇥) symbol:

```python
def mixed_indentation(greet=True):
····if greet:
········print("Hello")
⇥   print("World")  # Indented with a tab.

mixed_indentation()
```

The difference is invisible when you’re just looking at the code, but make sure to use a tab character for indentation in line 4, while using four space characters for the other indentations.

