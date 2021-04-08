## unlike regular functions, arrow functions do not have their own this.

## Arrow functions don’t redefine the value of this within their function body. This makes it a lot easier to predict their behavior when passed as callbacks,

## Inside a function, the value of this depends on how the function is called.

## regular funciton

- this is the who call the function

## arrow function

- this is the who define the function
  - Arrow functions don't have their own this or arguments binding.
  - Instead, those identifiers are resolved in the lexical scope like any other variable.
  - That means that inside an arrow function, this and arguments refer to the values of this and arguments in the environment the arrow function is defined in (i.e. "outside" the arrow function):
