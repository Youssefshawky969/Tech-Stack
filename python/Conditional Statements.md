In a Python program, the `if` statement is how you perform this sort of decision-making. 

It allows for conditional execution of a statement or group of statements based on the value of an expression.

## Introduction to the if Statement

We’ll start by looking at the most basic type of if statement. In its simplest form, it looks like this:

```python
if <expr>:
    <statement>
```

In the form shown above:

`<expr>` is an expression evaluated in a Boolean context.

`<statement>` is a valid Python statement, which must be indented.

If `<expr>` is true (evaluates to a value that is “truthy”), then `<statement>` is executed.

 If `<expr>` is false, then `<statement>` is skipped over and not executed.

 Note that the colon (`:`) following `<expr>` is required. Some programming languages require `<expr>` to be enclosed in parentheses, but Python does not.

 Here are several examples of this type of if statement:

```python
>>> x = 0
>>> y = 5

>>> if x < y:                            # Truthy
...     print('yes')
...
yes
>>> if y < x:                            # Falsy
...     print('yes')
...

>>> if x:                                # Falsy
...     print('yes')
...
>>> if y:                                # Truthy
...     print('yes')
...
yes

>>> if x or y:                           # Truthy
...     print('yes')
...
yes
>>> if x and y:                          # Falsy
...     print('yes')
...

>>> if 'aul' in 'grault':                # Truthy
...     print('yes')
...
yes
>>> if 'quux' in ['foo', 'bar', 'baz']:  # Falsy
...     print('yes')
...
```

### Grouping Statements: Indentation and Blocks

 let’s say you want to evaluate a condition and then do more than one thing if it is true:

 ```
If the weather is nice, then I will:

Mow the lawn
Weed the garden
Take the dog for a walk
(If the weather isn’t nice, then I won’t do any of these things.)
```
In all the examples shown above, each if `<expr>:` has been followed by only a single `<statement>`.

There needs to be some way to say “If <expr> is true, do all of the following things.”

The usual approach taken by most programming languages is to define a syntactic device that groups multiple statements into one compound statement or block.

 A block is regarded syntactically as a single entity. 

  When it is the target of an if statement, and `<expr>` is true, then all the statements in the block are executed. If `<expr>` is false, then none of them are.

 ```python
if <expr>:
    <statement>
    <statement>
    ...
    <statement>
<following_statement>
```

Here, all the statements at the matching indentation level (lines 2 to 5) are considered part of the same block.

 The entire block is executed if <expr> is true, or skipped over if <expr> is false.

  Either way, execution proceeds with <following_statement> (line 6) afterward.

  <img width="1161" height="567" alt="image" src="https://github.com/user-attachments/assets/4bb46e51-3d2d-456a-8179-8687af6312be" />

Notice that there is no token that denotes the end of the block. 

Rather, the end of the block is indicated by a line that is indented less than the lines of the block itself.

> [!NOTE]
>
> In the Python documentation, a group of statements defined by indentation is often referred to as a suite. This tutorial series uses the terms block and suite interchangeably

Consider this script file `foo.py`:

```python
if 'foo' in ['bar', 'baz', 'qux']:
    print('Expression was true')
    print('Executing statement in suite')
    print('...')
    print('Done.')
print('After conditional')
```

Running `foo.py` produces this output:

```bash
C:\> python foo.py
After conditional
```

The four `print()` statements on lines 2 to 5 are indented to the same level as one another.

They constitute the block that would be executed if the condition were true. But it is false, so all the statements in the block are skipped

After the end of the compound `if` statement has been reached (whether the statements in the block on lines 2 to 5 are executed or not), execution proceeds to the first statement having a lesser indentation level: the `print()` statement on line 6.

Blocks can be nested to arbitrary depth.

Each indent defines a new block, and each outdent ends the preceding block. 

The resulting structure is straightforward, consistent, and intuitive.

Here is a more complicated script file called `blocks.py`:

```python
# Does line execute?                        Yes    No
#                                           ---    --
if 'foo' in ['foo', 'bar', 'baz']:        #  x
    print('Outer condition is true')      #  x

    if 10 > 20:                           #  x
        print('Inner condition 1')        #        x

    print('Between inner conditions')     #  x

    if 10 < 20:                           #  x
        print('Inner condition 2')        #  x

    print('End of outer condition')       #  x
print('After outer condition')            #  x
```

The output generated when this script is run is shown below:

```bash
C:\> python blocks.py
Outer condition is true
Between inner conditions
Inner condition 2
End of outer condition
After outer condition
```

### The else and elif Clauses

Sometimes, you want to evaluate a condition and take one path if it is true but specify an alternative path if it is not. 

This is accomplished with an `else` clause:

```python
if <expr>:
    <statement(s)>
else:
    <statement(s)>
```

If `<expr>` is true, the first suite is executed, and the second is skipped.

If `<expr>` is false, the first suite is skipped and the second is executed.

Either way, execution then resumes after the second suite. Both suites are defined by indentation, as described above.

In this example, `x` is less than 50, so the first suite (lines 4 to 5) are executed, and the second suite (lines 7 to 8) are skipped:

```python
>>> x = 20

>>> if x < 50:
...     print('(first suite)')
...     print('x is small')
... else:
...     print('(second suite)')
...     print('x is large')
...
(first suite)
x is small
```

Here, on the other hand, `x` is greater than 50, so the first suite is passed over, and the second suite executed:

```python
>>> x = 120
>>>
>>> if x < 50:
...     print('(first suite)')
...     print('x is small')
... else:
...     print('(second suite)')
...     print('x is large')
...
(second suite)
x is large
```

There is also syntax for branching execution based on several alternatives.

For this, use one or more elif (short for else if) clauses.

Python evaluates each `<expr>` in turn and executes the suite corresponding to the first that is true.

If none of the expressions are true, and an `else` clause is specified, then its suite is executed:

```python
if <expr>:
    <statement(s)>
elif <expr>:
    <statement(s)>
elif <expr>:
    <statement(s)>
    ...
else:
    <statement(s)>
```
An arbitrary number of `elif` clauses can be specified.

The `else` clause is optional.

If it is present, there can be only one, and it must be specified last:

```python
>>> name = 'Joe'
>>> if name == 'Fred':
...     print('Hello Fred')
... elif name == 'Xander':
...     print('Hello Xander')
... elif name == 'Joe':
...     print('Hello Joe')
... elif name == 'Arnold':
...     print('Hello Arnold')
... else:
...     print("I don't know who you are!")
...
Hello Joe
```

At most, one of the code blocks specified will be executed.

If an `else` clause isn’t included, and all the conditions are false, then none of the blocks will be executed.

> [!NOTE]
>
> Using a lengthy `if`/`elif`/`else` series can be a little inelegant, especially when the actions are simple statements like `print()`.
> In many cases, there may be a more Pythonic way to accomplish the same thing.
>
> Here’s one possible alternative to the example above using the dict.get() method:
> ```
> >>> names = {
>  ...     'Fred': 'Hello Fred',
>  ...     'Xander': 'Hello Xander',
>  ...     'Joe': 'Hello Joe',
>  ...     'Arnold': 'Hello Arnold'
>  ... }
> >>> print(names.get('Joe', "I don't know who you are!"))
>  Hello Joe
> >>> print(names.get('Rick', "I don't know who you are!"))
> I don't know who you are!
> ```



