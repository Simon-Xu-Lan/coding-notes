## Parameter vs argument

- parameter: is the name of the data being passed to function
- argument: is the actual value of the data

![parameter] vs argument](images/parameter and argument.png)

## Positional arguments

- argumet is determined by position

## Keyword arguments

- argument is determined by keyword, position doesn't matter

## Advance Arguments

### default value 246

```py
  # Set default value when declare the function
  def my_function(a=1, b=2, c=3):
    # Do something with a, b. c
```

### Unlimited Positional Arguments

- \*args
- Lecture: args Many Positional argument 247 / 100 days of code

```py
# Can accept any number of arguments
def add(*args):
  for n in args:    # args is a tuple.
    print(n)
```

### Many Keyworded Arguments

- \*\*kwargs
- Lecture 248 100 days of code

```py
# Example 1
def caculate(**kwargs):
  print(kwargs)   # kwargs is a dictionary

calculate(add=3, multiply=5)
# Output: {'add': 3, 'multiply': 5}

# Example 2
def calculate(n, **kwargs):
  n += kwargs["add"]
  n += kwargs["multiply"]
  print(n)

calculate(2, add=3, multiply=5)
# Output: 25

# Example 3
def calculate(n, **kwargs):
  add = kwargs.get("add")
  multiply = kwargs.get("multiply")
  print((n + add) * multiply)
```

## args Many Positional argument 247

## kwargs 248 249

# Advanced concept

- 447, **name** and **main**: Special attribtes built into python
- 448, Python Functions as first class objects: passing and nesting function
- 449, Python decorator functions and @ syntactic suger

# Python Decorators

## Functions can have inputs/functionality/output

```py
  def add(n1, n2):
      return n1 + n2

  def subtract(n1, n2):
      return n1 - n2

  def multiply(n1, n2):
      return n1 * n2

  def divide(n1, n2):
      return n1 / n2
```

## Functions are first-class objects, can be passed around as arguments e.g. int/string/float etc.

````py
  def calculate(calc_function, n1, n2):
      return calc_function(n1, n2)

  result = calculate(add, 2, 3)
print(result)
# Output: 5
``
## Functions can be nested in other functions
```py
  def outer_function():
      print("I'm outer")

      def nested_function():
          print("I'm inner")

      nested_function()

  outer_function()
  # Output:
  # I'm outer
  # I'm inner
````

## Functions can be returned from other functions

```py
  def outer_function():
      print("I'm outer")

      def nested_function():
          print("I'm inner")

      return nested_function

  inner_function = outer_function()
  inner_function()
  # Output:
  # I'm outer
  # I'm inner
```

# Python decorator function

## Python decorator function is a function which wrap another function and give it additional functionality or modify the functionality

## Simple Python Decorator Functions

```py
  import time

  def delay_decorator(function):
    def wrapper_function():
      time.sleep(2)
      #Do something before
      function()
      function()
      #Do something after
    return wrapper_function

  # With @ syntactic suger
  @delay_decorator
  def say_hello():
  print("Hello")

  #With the @ syntactic sugar
  @delay_decorator
  def say_bye():
  print("Bye")

  #Without the @ syntactic sugar
  def say_greeting():
  print("How are you?")
  decorated_function = delay_decorator(say_greeting)
  decorated_function()
```

# Visualize Coding Running

- http://pythontutor.com/visualize.html#mode=display
