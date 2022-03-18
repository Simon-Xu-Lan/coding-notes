# Library vs. Framework

| Librara                                                                                                    | Framework                                                                                                            |
| ---------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| Library is a set of resuable functions used by computer programs.                                          | Framework is a piece of code that dictates the architecture of your project and aids in programs                     |
| You are in full control when you call a method from a library and the control is then returned             | The code never calls into a framework, instead teh framework calls you                                               |
| It's incorporated seamlessly into existing projects to add functionality that you can access using an API. | It cannot be seamlessly incorporated into an existing project. Instead it can be used when a new project is started. |
| They are important in program linking and binding process.                                                 | They provide a standard way to build and deploy applications                                                         |
| Example: jQuery is a JavaScript library that simplifies COM manipulation.                                  | Example: AngularJS is a JavaScript-based framework for dynamic web applications.                                     |

# Flask

https://py.plainenglish.io/how-to-build-a-web-api-fa0f3bd73a71

```py
from flask import Flask

app=Flask(__name__)
@app.route('/')
def index():
    return 'Welcome'
if __name__ == '__main__':
    app.run()
```

## app=Flask(**name**)

- create an instance of the Flask class and pass the name of the application (variable **name**) as the argument to the constructor.

## Flask object

- Flask object is a WSGI (Web Server Gateway Interface) application
  - which means that the web server passes all the requests it receives to this instance for further processing.

## @app.route('/')

- Flask maps HTTP requests to Python functions.
- This is achieved through the .route() decorator in the code.
- A Route binds a URL to a function, which can be programmed to respond to a request.

## The designated URL, ‘/’, or technically when no additional path is provided

- is mapped to our simple user-defined function, index().

## if **name** == '**main**':

- The condition **name**==’**main**’ ensures that the .run() method starts the server when the script is executed as the main program.

## Sample Data

```py
@app.route('/sample/')
def sample():
    return jsonify([{'state': 'CA', 'city': 'Napa', 'name': 'Sample'}])
```

- We designate the route ‘/sample/’ to call the user-defined sample() function,
- which returns the sample data in the form of a list of a Python dictionary with key-value pairs.
- jaonidy
  - The query results have to be serialized through the jsonify() method and turned into a response object.
- Route
  - Flask will redirect the request without the trailing slash to the URL with the trailing slash.
  - This means a request to /breweries will be redirected to /breweries/

# Connecting the Web Application to the Database

```sql
from flask import jsonify
from flask_cors import CORS
from sqlalchemy import create_engine

CORS(app)
engine=create_engine('sqlite:///assets/data/breweries.sqlite')

@app.route('/breweries/')
def fetch():
    results=engine.execute('select state, city, name from breweries')
    return jsonify([{'state': result[0], 'city': result[1], 'name': result[2]} for result in results])

```

## flask-CORS

- flask-CORS extension to make cross-origin resource sharing possible, since we are hosting the database and API in a separate domain.
- CORS enables controlled access to resources located outside of a given domain.

## create_engine()

- The create_engine() function produces an Engine object based on the database URL,
- usually the starting point for any SQLAlchemy application.
- The database URL usually includes username, password, hostname, database name as well as optional keyword arguments for additional configuration.
- The typical form of a database URL is:

```py
dialect+driver://username:password@host:port/database
```

# Resources

- Flask Quikc Start Documentation
  - Flask Quick Start Documentation

# Routing route

- https://flask.palletsprojects.com/en/1.1.x/quickstart/#routing

# Working Flask URL Paths and the Flask Debugger

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
