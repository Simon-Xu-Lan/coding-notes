- What is Node.js

  - Node.js is an open source server environment
  - A common task for a web server can be to open a file on the server and return the content to the client.
  - Here is how Node.js handles a file request:
    - Sends the task to the computer's file system.
    - Ready to handle the next request.
    - When the file system has opened and read the file, the server returns the content to the client.
  - Node.js eliminates the waiting, and simply continues with the next request.
  - Node.js runs single-threaded, non-blocking, asynchronously programming, which is very memory efficient.

- What Can Node.js Do?

  - Node.js can generate dynamic page content
  - Node.js can create, open, read, write, delete, and close files on the server
  - Node.js can collect form data
  - Node.js can add, delete, modify data in your database

- What is a Node.js File?

  - Node.js files contain tasks that will be executed on certain events
  - A typical event is someone trying to access a port on the server
  - Node.js files must be initiated on the server before having any effect
  - Node.js files have extension ".js"

- What is a Module in Node.js?

  - Consider modules to be the same as JavaScript libraries.
  - Built-in Modules
    - Node.js has a set of built-in modules which you can use without any further installation.
  - Include Modules
    - To include a module, use the require() function with the name of the module
    - example:
      - Create a module that returns the current date and time:
      ```javascript
      exports.myDateTime = function () {
        return Date();
      };
      ```
      - Use the exports keyword to make properties and methods available outside the module file.
      ```javascript
      var dt = require('./myfirstmodule');
      // can use list this
      dt.myDateTime();
      ```
  - ./
    - use ./ to locate the module
    - the module is located in the same folder
  - ../
    - the module is located in the upper level folder

- \_\_filename

  - This is a variable that contains the absolute path of the current module.
  - Given two modules: a and b, where b is a dependency of a and there is a directory structure of:
    - /User/home/node_blog/a.js
    - /User/home/node_blog/node_modules/b/b.js
    - So, if we do console.log(\_\_filename)within b.js,
      - we will get /User/home/node_blog/node_modules/b/b.js.
    - If we do console.log(\_\_filename) within a.js,
      - we will get /User/home/node_blog/a.js.

- \_\_dirname

  - The directory name of the current module.
  - This is the same as the path.dirname() of the \_\_filename
  - f we do console.log(\_\_dirname) within b.js,
    - we will get /User/home/node_blog/node_modules/b/
    - and in a.js, we will get /User/home/node_blog/.

- Difference Between module.exports and exports, and return function

  - We use both module.exports and exports to export our functionalities out of our module.
  - The exports object is just shorthand for module.exports.
  - module.exports object is returned by the require function when we require in a module.

- main in package.json

  - package.json must be located in root directory
  - If Node does not find any package.json in the root directory of the module,
    - or in package.json if the main entry is missing or cannot be resolved.
    - Then, Node.js will try to load index.js or index.node from that directory.
      - If these attempts fail, then Node.js will report the entire module as missing with the default error:
        - rror: Cannot find module "..."

- require()
  - When we require a module it is not necessary to give the file extension.
    - For example, if there is a some-file.js file that we want to require and it is on the same level, we can require it as:
      - const someFile = require(‘./some-file’);
  - While resolving the path of this file, Node follows a procedure.
    - It first looks for some-file.js
    - if some-file.js is not present, it will look for some-file.json
    - if that is also not present, it will look for some-file.node
      Use the exports keyword to make properties and methods available outside the module file.
