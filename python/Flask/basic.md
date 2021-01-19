## Library vs. Framework

| Librara                                                                                                    | Framework                                                                                                            |
| ---------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| Library is a set of resuable functions used by computer programs.                                          | Framework is a piece of code that dictates the architecture of your project and aids in programs                     |
| You are in full control when you call a method from a library and the control is then returned             | The code never calls into a framework, instead teh framework calls you                                               |
| It's incorporated seamlessly into existing projects to add functionality that you can access using an API. | It cannot be seamlessly incorporated into an existing project. Instead it can be used when a new project is started. |
| They are important in program linking and binding process.                                                 | They provide a standard way to build and deploy applications                                                         |
| Example: jQuery is a JavaScript library that simplifies COM manipulation.                                  | Example: AngularJS is a JavaScript-based framework for dynamic web applications.                                     |

## Resources

- Flask Quikc Start Documentation
  - Flask Quick Start Documentation

## Routing route

- https://flask.palletsprojects.com/en/1.1.x/quickstart/#routing

## Working Flask URL Paths and the Flask Debugger

- 452 Working Flask URL Paths and the Flask Debugger
- Enable debug

## Variable Rules

- add variable sections to a URL by marking sections with <variable_name>
- without slash

```py
  app.route("/<name>)
  def greet(name)::
    return f"Hello there {name}"
```

- include slash:

```py
  app.route("/<path:name>)
  def greet(name)::
    return f"Hello there {name}"
  # output:
  # if URL: 127.0.0.1:5000/Simon/1
  # output is: Hello there Simon/1
```

- Multiple variables

```py
  app.route("/username/<name>/<int:number>)
  def greet(name)::
    return f"Hello there {name}, you are {number} years old!"
  # output:
  # if URL: 127.0.0.1:5000/username/Simon/48
  # output is: Hello there Simon, you are 48 years old!
```

- use a converter to specify the type of the argument like <converter:variable_name>.
  - By default, it convert the value to a string
  - Converter types:
    | | |
    | --- | --- |
    | string | default, accepts any text without a slash |
    | int | accepts positive integers |
    | float | accepts positive floating pointing values |
    | path | like string but also accepts slashes |
    | uuid | accepts UUID strings |

```py

```

## giphy

- https://giphy.com/

## Chrome cashe the webpage static file for one day.

using hard refresh to update the static file.
hold shift to refresh
