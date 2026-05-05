## What Is Functional Programming?

A pure function is a function whose output value follows solely from its input values without any observable side effects. 

In functional programming, a program consists primarily of the evaluation of pure functions.

Computation proceeds by nested or composed function calls without changes to state or mutable data.

The functional paradigm is popular because it offers several advantages over other programming paradigms. Functional code is:
- High level: You describe the result you want rather than explicitly specifying the steps required to get there. Single statements tend to be concise but pack a lot of punch.
- Transparent: The behavior of a pure function can be described by its inputs and outputs, without intermediary values. This eliminates the possibility of side effects and facilitates debugging.
- Parallelizable: Routines that don’t cause side effects can more easily run in parallel with one another

## How Well Does Python Support Functional Programming?

To support functional programming, it’s beneficial if a function in a given programming language can do these two things:
1- Take another function as an argument
2- Return another function to its caller

In Python, functions are first-class citizens.

This means that functions have the same characteristics as values like strings and numbers.

Anything you would expect to be able to do with a string or number, you can also do with a function.

For example, you can assign a function to a variable. You can then use that variable the same way you would use the function itself:

```python
>>> def func():
...     print("I am function func()!")
...

>>> func()
I am function func()!

>>> another_name = func
>>> another_name()
I am function func()!
```
The assignment another_name = func on line 8 creates a new reference to func() named another_name. You can then call the function by either of the two names, func or another_name, as shown on lines 5 and 9.

You can display a function to the console with print(), include it as an element in a composite data object like a list, or even use it as a dictionary key:
```python
>>> def func():
...     print("I am function func()!")
...

>>> print("cat", func, 42)
cat <function func at 0x7f81b4d29bf8> 42

>>> objects = ["cat", func, 42]
>>> objects[1]
<function func at 0x7f81b4d29bf8>
>>> objects[1]()
I am function func()!

>>> d = {"cat": 1, func: 2, 42: 3}
>>> d[func]
2
```
In this example, func() appears in all the same contexts as the values "cat" and 42, and the interpreter handles it just fine.


For present purposes, what matters is that functions in Python satisfy the two criteria beneficial for functional programming listed above. You can pass a function to another function as an argument:
```python
>>> def inner():
...     print("I am function inner()!")
...

>>> def outer(function):
...     function()
...

>>> outer(inner)
I am function inner()!
```

Here’s what’s happening in the above example:
- The call on line 9 passes inner() as an argument to outer()
- Within outer(), Python binds inner() to the function parameter function.
- outer() can then call inner() directly with function.

This is known as function composition. 

Keep in mind that you’re passing the function object as an argument.

If you would call the function object using parentheses, then you wouldn’t pass the function object but instead its return value.

When you pass a function to another function, the passed-in function is sometimes referred to as a callback because a call back to the inner function can modify the outer function’s behavior.

A good example of this is the Python function sorted().

Ordinarily, if you pass a list of string values to sorted(), then it sorts them in lexical order:
```python
>>> animals = ["ferret", "vole", "dog", "gecko"]
>>> sorted(animals)
['dog', 'ferret', 'gecko', 'vole']
```

 However, sorted() takes an optional key argument that specifies a callback function that can serve as the sorting key.
  So, for example, you can sort by string length instead:

```python
>>> animals = ["ferret", "vole", "dog", "gecko"]
>>> sorted(animals, key=len)
['dog', 'vole', 'gecko', 'ferret']
```

sorted() can also take an optional argument that specifies sorting in reverse order. But you could manage the same thing by defining your own callback function that reverses the sense of len():
```python
>>> animals = ["ferret", "vole", "dog", "gecko"]
>>> sorted(animals, key=len, reverse=True)
['ferret', 'gecko', 'vole', 'dog']

>>> def reverse_len(s):
...     return -len(s)
...
>>> sorted(animals, key=reverse_len)
['ferret', 'gecko', 'vole', 'dog']
```


  
