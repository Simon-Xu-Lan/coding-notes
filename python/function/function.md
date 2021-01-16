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
