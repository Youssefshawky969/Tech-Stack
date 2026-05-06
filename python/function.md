# Defining Functions in Python

The general syntax for defining a function is shown below:
```python
def function_name([parameters]):
    <block>
```

- **def**: The keyword that begins the function definition
- **function_name**:	A valid Python identifier that names the function
- **[parameters]**:	An optional, comma-separated list of formal parameters for the function
- **:** The punctuation that denotes the end of the function header
- **<block>**:	The function’s code block

The final item `<block>` is usually called the function’s body. The body is a series of statements that will run when you call the function. The body is defined by indentation.

Here’s your first Python function:
```python
>>> def greet(name):
...     print(f"Hello, {name}!")
...

>>> greet("Pythonista")
Hello, Pythonista!
```

You start the function’s definition with the `def` keyword.

Then, you have the function name, greet, followed by a pair of parentheses enclosing an argument called name.

To close the function header, you use a colon (:).

Next, you have an indented code block consisting of a call to the built-in print() function. This call will display a greeting message on your screen

Finally, you call the function using "Pythonista" as an argument. As a result, you get `Hello, Pythonista!` printed on the screen.

# Calling Functions in Python

You’ve already called a few functions so far. The syntax consists of writing the function’s name followed by a pair of parentheses, which encloses an optional series of arguments:
```python
function_name([arguments])
```
Here, <arguments> represent the concrete values that you pass into the function. They correspond to the <parameters> in the Python function definition.

>[!NOTE]
>
>There’s a subtle distinction between the terms parameter and argument.
>
> Parameters are those names used in the function definition,
>
> while arguments are the concrete values that you supply for each parameter in the function call. In Python, the term argument is often used informally to refer to both.

The arguments are optional, meaning that you can have functions without arguments.

However, the parentheses are required when you intend to call the function, even if the function takes no arguments.

Both function definitions and calls must always include parentheses, even when they’re empty.

You’ll get a syntax error if you forget the parentheses in a function definition.

If you forget the parentheses in a function call, then you’ll get a function object instead of the expected result that the function should produce.

# Calling function

two main ways to call Python functions

## Positional Arguments

The quickest way to call a function with arguments is to rely on the specific position of each argument. In this case, you’ll be using what’s known as positional arguments.

In the function definition, you specify a series of comma-separated parameters inside the parentheses.

 For example, consider the following function that computes the cost of a product and displays a message to the screen:
 ```python
>>> def calculate_cost(item, quantity, price):
...     print(f"{quantity} {item} cost ${quantity * price:.2f}")
```
To call this function, you must specify a corresponding list of arguments in the correct order:
```python
>>> calculate_cost("bananas", 6, 0.74)
6 bananas cost $4.44
```
The parameters item, quantity, and price are like variables defined locally in the function.

When you call the function, the values "bananas", 6, and 0.74 are bound to the parameters in order, as though by variable assignment:

Although positional arguments are a common way to pass data to a function, they could cause some issues. 

The order of the arguments in the call must match the order of parameters in the definition. If you change the order, then you may get unexpected behavior or an error:

```python
>>> calculate_cost("bananas", 0.74, 6)
0.74 bananas cost $4.44

>>> calculate_cost(6, "bananas", 0.74)
Traceback (most recent call last):
    ...
TypeError: can't multiply sequence by non-int of type 'float'
```

As in the first call above, the function may still run, but it’s unlikely to produce the correct results. The programmer who defines the function must document the arguments appropriately, and the user must be aware of that information and stick to it.

In summary, the arguments in the call and the parameters in the definition of a function must agree in order and number. In a sense, positional arguments are required because if they don’t have a default argument value, then you can’t leave them out when calling the function:

```python
>>> # Too few arguments
>>> calculate_cost("bananas", 6)
Traceback (most recent call last):
    ...
TypeError: calculate_cost() missing 1 required positional argument: 'price'

>>> # Too many arguments
>>> calculate_cost("bananas", 6, 0.74, "mango")
Traceback (most recent call last):
    ...
TypeError: calculate_cost() takes 3 positional arguments but 4 were given
```


## Keyword Arguments

When calling a function, you can specify arguments in the form argument=value. This way of passing arguments to a Python function is known as using keyword arguments.

 For example, you can call the calculate_cost() function as shown below:
 ```python
>>> calculate_cost(item="bananas", quantity=6, price=0.74)
6 bananas cost $4.44
```

Using keyword arguments lifts the restriction on argument order because each keyword argument explicitly designates a specific parameter by name, so you can specify them in any order, and Python will know which argument goes with which parameter:

```python
>>> calculate_cost(price=0.74, quantity=6, item="bananas")
6 bananas cost $4.44
```

If you use keyword arguments in a function call, Python has an unambiguous way to determine which argument goes to which parameter. So, you don’t have the restriction of providing the arguments in a strict order.

Like with positional arguments, though, the number of arguments and parameters must still match:

```python
>>> calculate_cost(item="bananas", quantity=6)
Traceback (most recent call last):
    ...
TypeError: calculate_cost() missing 1 required positional argument: 'price'
```

So, keyword arguments allow flexibility in the order that function arguments are specified, but the number of arguments is still rigid.

The second advantage of keyword arguments is readability. Do you remember the update_product() function from the previous section? Check out at how it’d look using keyword arguments in the call:

```python
# Using positional arguments
update_product(1234, 15, 2.55, "12-31-2025")

# Using keyword arguments
update_product(
    product_id=1234,
    quantity=15,
    price=2.55,
    expiration_date="12-31-2025"
)
````


Isn’t the call with keyword arguments way more readable than the call with positionals?
 
When you call functions in your code, if there’s a risk of ambiguity, try to use keyword arguments if possible. This tiny detail will improve your code’s readability.

You can also call a function using both positional and keyword arguments:
```python
>>> calculate_cost("bananas", quantity=6, price=0.74)
6 bananas cost $4.44
```

In this example, you’ve provided item as a positional argument. In contrast, quantity and price are keyword arguments.

>[!NOTE]
>When you use positional and keyword arguments in a function call, all the positional arguments must come first. Otherwise, you’ll get a syntax error

```python
>>> calculate_cost(item="bananas", quantity=6, 0.74)
  File "<input>", line 1
    calculate_cost(item="bananas", quantity=6, 0.74)
                                                   ^
SyntaxError: positional argument follows keyword argument
```

Once you’ve specified a keyword argument, you can’t place any positional arguments after it. In this example, you use keyword arguments for item and quantity, but positional arguments for price. This raises a SyntaxError exception because Python’s grammar prohibits positional arguments following keyword arguments to avoid ambiguity.

# Returning From Functions

Python functions can return concrete values, as you briefly saw at the end of the previous section. To do this, you can use the return statement, which serves two purposes:

1- Passing data back to the caller
2- Terminating the function and passing execution control back to the caller

If you place a `return` statement followed by an expression inside a Python function, then the calling environment will get the value of that expression back:
```python
>>> def identity(x):
...    return x
...

>>> x = identity(42)
>>> x
42
```
This function mimics an identity function in math. It maps every input value to itself. 

In this example, you use `return x` to return a concrete value from your function. The general syntax for a return statement is shown below:

```python
def function_name():
    return [expression_0[, expression_1, ..., expression_n]]
```

First, you need to know that you can’t use the return statement outside of a function.

If you do so, then you’ll get a SyntaxError exception.

Second, the expression or expressions that follow the return keyword are optional.

That’s what the square brackets mean in this syntax.

In summary, you can have a return statement with zero, one, or more expressions. If you have multiple expressions, then you must separate them with commas.

In this case, the caller will receive a tuple of values:

```python
>>> def create_point(x, y):
...     return x, y
...

>>> create_point(2, 4)
(2, 4)
```
If you specify multiple comma-separated expressions in a return statement, then they’re packed and returned as a tuple object, as shown in the example above.

Python functions can return any object.
That means anything whatsoever, even other functions.

In the calling environment, you can use a function’s return value in any way that’s appropriate for its type.

For example, in this code, `as_dict()` returns a dictionary. In the calling environment, the call to this function returns a dictionary, and something like `as_dict()["key"]` is an entirely valid syntax:

```python
>>> def as_dict():
...     return dict(one=1, two=2, three=3)
...

>>> as_dict()
{'one': 1, 'two': 2, 'three': 3}

>>> as_dict()["two"]
2
```

When you call a function that returns a concrete value, you can use that value in any expression or further computation.
 So, you’ll often find and use function calls in expressions.


You can also have a bare return with no expression at the end. In this case, the function will return None:
```python
>>> def function():
...     return
...

>>> print(function())
None
```

Here, the return value is None by default. Note that Python REPL sessions don’t show None when you call a function that returns this object. That’s why you need to use print() in this example.

You can alternatively return None explicitly when this value has a specific semantic meaning in your code.

 In this case, doing something like return None will explicitly express your code’s intent. For example, the function below takes a username and checks whether that name is in the current user list:

 ```python
>>> def find_user(username, user_list):
...     for user in user_list:
...         if user["username"] == username:
...             return user
...     return None
...

>>> users = [
...     {"username": "alice", "email": "alice@example.com"},
...     {"username": "bob", "email": "bob@example.com"},
... ]

>>> find_user("alice", users)
{'username': 'alice', 'email': 'alice@example.com'}
>>> print(find_user("linda", users))
None
```

Although not mandatory, returning None explicitly is an appropriate and readable solution in this example. If you get None, it’s because the user wasn’t found.


Python returns None automatically from a function that doesn’t include explicit return statements:
```python
>>> def function():
...     pass
...

>>> print(function())
None
```
This function doesn’t have an explicit return statement. However, it returns None as in the previous example. This is the default behavior for all Python functions where you don’t have an explicit return statement, or where a specific execution doesn’t hit any of the existing ones.


You can use functions that return None explicitly in a Boolean context. In this case, the Pythonic way to check the return value would be as shown below:
```python
>>> if find_user("linda", users) is None:
...     print("Linda isn't a registered user")
...
Linda isn't a registered user
```
You compare the function’s return value against None using the `is` operator. You can also use the `is not` operator for appropriate situations.

```python
>>> if find_user("alice", users) is not None:
...     print("Do something with Alice's data...")
...
Do something with Alice's data...
```
## Exiting Functions Early

The return statement causes Python to exit from a function immediately and transfer the execution’s control back to the caller. This behavior allows you to use a bare return when you need to terminate a function’s execution early.

Consider the following toy example that processes a file:
```python
from pathlib import Path

def read_file_contents(file_path):
    path = Path(file_path)

    if not path.exists():
        print(f"Error: The file '{file_path}' does not exist.")
        return

    if not path.is_file():
        print(f"Error: '{file_path}' is not a file.")
        return

    return path.read_text(encoding="utf-8")
```
In this function, you have two conditionals. The first one checks if the file exists. If it doesn’t, an error message is printed and the function exits. Next, the second one checks if the provided path points to a file. If not, another error message is printed and the function returns.

 In the final line of this function, you have another return statement that returns the file’s content, which is the function’s primary goal.



## Returning Boolean Values

Another common use case of the return statement is when you need a function to return True or False depending on some concrete condition of your code. These types of functions are known as Boolean-valued functions or predicates.

For example, here’s a function that checks whether a number is even:
```python
>>> def is_even(number):
...     return number % 2 == 0
...

>>> is_even(2)
True
>>> is_even(3)
False
```
In this example, the return value comes from a condition that evaluates to either True or False, depending on the input number.

Predicate functions are common and useful in programming. For example, Python’s built-in functions all(), any(), hasattr(), isinstance(), and issubclass() are all predicate functions.




