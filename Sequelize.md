**Instructions:**

- Spend the next few ~15 minutes with your partner answering the following questions. You should be using the Sequelize Documentation (and whatever other references you find online).

  - Question: What is Sequelize?

    - ORM.
    - Object-Relational Mapper
    - it plots an object syntax into database schemas.
    - Object in Js - Relational table in databse - Mapping

  - Question: What advantages does it offer?

    - Easy to test.
    - Gives you support for syncing databases.
    - Validation, restricts to specific form of data.
    - Complex SQL queries in simple syntax,

  - Question: How do I install it? How do I incorporate it into my app?

    - `npm install sequelize`

  - Question: What the heck is a Sequelize model? What role will it play?

    - A representation of table data for Sequeliz
      -REST
    - Representational State Transfer
    - determines how the API appears
      -CRUD
    - Create, Read, Update, and Delete

  - Express

    - a web application framework for Node.js
    - free, open-source, fast, and minimalist

  - Sequelize can query all complicated join functions. The user only needs to learn how ‘Objects’ connect with one another.

- Let's say I have the below table in MySQL.

  | Country     | PhoneCode | Capital   | IndependenceYear |
  | ----------- | --------- | --------- | ---------------- |
  | Afghanistan | 93        | Kabul     | 1919             |
  | Belarus     | 375       | Misk      | 1991             |
  | Netherlands | 31        | Amsterdam | 1648             |
  | Oman        | 968       | Muscat    | 1970             |
  | Zambia      | 260       | Lusaka    | 1964             |

  - Question: How would I model it in Sequelize?

    ```javascript
    // the method define() creates model in sequelize that represend a table in database
    var tableName = sequelize.define(
      'tableName',
      {
        Country: {
          type: Sequelize.STRING,
        },
        PhoneCode: {
          type: Sequelize.INTEGER,
        },
        Capital: {
          type: Sequelize.STRING,
        },
        IndependenceYear: {
          type: Sequelize.INTEGER,
        },
      },
      {
        freezeTableName: true,
        // With freezTableName, the table name will be the same as the model name that sequelize defines, otherwise, the tabel name in DB would be pluralized
        // { define: { freezeTableName: true } }); This way, all tables will use the same name as the model name.
      }
    );

    // force: true will drop the table if it already exists
    tableName.sync({ force: true }).then(function () {
      // Table created in Database with method .create()
      return tableName.create({
        Country: 'Afghanistan',
        PhoneCode: 93,
        Capital: 'Kabul',
        IndependenceYear: 1919,
      });
    });
    ```

  - Example -- Chirpy -- /14-Full-Stack/01-Activities/03-/Chirot-Sequelize

        - /config/connection.js  => the file initialize the connection to mySql

        ```javascript
        // Dependencies
        var Sequelize = require('sequelize');

        // Creates mySQL connection using Sequelize, the empty string in the third argument spot is our password.
        // 'sequelize_chirpy': schema name in mySQL
        // user: root
        // password for the user: password
        var sequelize = new Sequelize('sequelize_chirpy', 'root', 'password', {
          host: 'localhost',
          port: 3306,
          dialect: 'mysql',
          pool: {
            max: 5,
            min: 0,
            idle: 10000,
          },
        });

        // Exports the connection for other files to use
        module.exports = sequelize;
        ```

        - /models/definemodel.js  => defines/creates model
        ```javascript
          // Dependencies

          // This may be confusing but here Sequelize (capital) references the standard library
          var Sequelize = require("sequelize");
          // sequelize (lowercase) references our connection to the DB.
          var sequelize = require("../config/connection.js");

          // Creates a "Chirp" model that matches up with DB
          var Chirp = sequelize.define("chirp", {
            author: Sequelize.STRING,
            body: Sequelize.STRING,
            created_at: Sequelize.DATE
          });

          // Syncs with DB
          Chirp.sync();

          // Makes the Chirp Model available for other files (will also create a table)
          module.exports = Chirp;
        ```

        - /routes/api-routes.js  => using sequelize to get data from database and write data to database
        ```javascript
          // Dependencies
          var Chirp = require("../models/chirp.js");

          // Routes
          // =============================================================
          module.exports = function(app) {

          // Get all chirps
          app.get("/api/all", function(req, res) {

              // Finding all Chirps, and then returning them to the user as JSON.
              // Sequelize queries are asynchronous, which helps with perceived speed.
              // If we want something to be guaranteed to happen after the query, we'll use
              // the .then function
              Chirp.findAll({}).then(function(results) {
                // results are available to us inside the .then
                res.json(results);
              });

          });

          // Add a chirp
          app.post("/api/new", function(req, res) {

              console.log("Chirp Data:");
              console.log(req.body);

              Chirp.create({
                author: req.body.author,
                body: req.body.body,
                created_at: req.body.created_at
              }).then(function(results) {
                // `results` here would be the newly created chirp
                res.end();
              });

          });

          };
          // =================================================================

          ```

- Example -- StarWars -- /14-Full-Stack/01-Activities/04-StarWars

  - define a model with sequelize type

    ```javascript
    // Dependencies
    // Sequelize (capital) references the standard library
    var Sequelize = require('sequelize');
    // sequelize (lowercase) references our connection to the DB.
    var sequelize = require('../config/connection.js');

    // Creates a "Character" model that matches up with DB
    var Character = sequelize.define(
      'character',
      {
        // the routeName gets saved as a string
        routeName: Sequelize.STRING,
        // the name of the character (a string)
        name: Sequelize.STRING,
        // the character's role (a string)
        role: Sequelize.STRING,
        // the character's age (a string)
        age: Sequelize.INTEGER,

        // and the character's force points (an int)
        forcePoints: Sequelize.INTEGER,
      },
      {
        // disable the modification of tablenames; By default, sequelize will automatically
        // transform all passed model names (first parameter of define) into plural.
        // if you don't want that, set the following
        freezeTableName: true,
      }
    );

    // Syncs with DB
    Character.sync();

    // Makes the Character Model available for other files (will also create a table)
    module.exports = Character;
    ```

  - sequelize method -- findOne() -- findAll()

  ```javascript
  // Dependencies
  var Character = require('../models/character.js');

  // Routes
  // =============================================================
  module.exports = function (app) {
    // Search for Specific Character (or all characters) then provides JSON
    app.get('/api/:characters?', function (req, res) {
      if (req.params.characters) {
        // Display the JSON for ONLY that character.
        // (Note how we're using the ORM here to run our searches)
        Character.findOne({
          where: {
            routeName: req.params.characters,
          },
        }).then(function (result) {
          return res.json(result);
        });
      } else {
        Character.findAll().then(function (result) {
          return res.json(result);
        });
      }
    });

    // If a user sends data to add a new character...
    app.post('/api/new', function (req, res) {
      // Take the request...
      var character = req.body;

      // Create a routeName

      // Using a RegEx Pattern to remove spaces from character.name
      // You can read more about RegEx Patterns later https://www.regexbuddy.com/regex.html
      var routeName = character.name.replace(/\s+/g, '').toLowerCase();

      // Then add the character to the database using sequelize
      Character.create({
        routeName: routeName,
        name: character.name,
        role: character.role,
        age: character.age,
        forcePoints: character.forcePoints,
      });

      res.status(204).end();
    });
  };
  // =============================================================
  ```

- Example -- StarWars -- /14-Full-Stack/01-Activities/05-SequelizeLibrary

  - sequelize method -- findOne() -- findAll() -- create() -- destroy

  ```javascript
  // *********************************************************************************
  // api-routes.js - this file offers a set of routes for displaying and saving data to the db
  // *********************************************************************************

  // Dependencies
  // =============================================================
  var Book = require('../models/book.js');

  // Routes
  // =============================================================
  module.exports = function (app) {
    // Get all books
    app.get('/api/all', function (req, res) {
      Book.findAll({}).then(function (results) {
        res.json(results);
      });
    });

    // Get a specific book
    app.get('/api/:book', function (req, res) {
      Book.findAll({
        where: {
          title: req.params.book,
        },
      }).then(function (results) {
        res.json(results);
      });
    });

    // Get all books of a specific genre
    app.get('/api/genre/:genre', function (req, res) {
      Book.findAll({
        where: {
          genre: req.params.genre,
        },
      }).then(function (results) {
        res.json(results);
      });
    });

    // Get all books from a specific author
    app.get('/api/author/:author', function (req, res) {
      Book.findAll({
        where: {
          author: req.params.author,
        },
      }).then(function (results) {
        res.json(results);
      });
    });

    // Get all "long" books (books 150 pages or more)
    app.get('/api/books/long', function (req, res) {
      Book.findAll({
        where: {
          pages: {
            $gte: 150,
          },
        },
        order: [['pages', 'DESC']],
      }).then(function (results) {
        res.json(results);
      });
    });

    // Get all "short" books (books 150 pages or less)
    app.get('/api/books/short', function (req, res) {
      Book.findAll({
        where: {
          pages: {
            $lte: 150,
          },
        },
        order: [['pages', 'ASC']],
      }).then(function (results) {
        res.json(results);
      });
    });

    // Add a book
    app.post('/api/new', function (req, res) {
      console.log('Book Data:');
      console.log(req.body);
      Book.create({
        title: req.body.title,
        author: req.body.author,
        genre: req.body.genre,
        pages: req.body.pages,
      }).then(function (results) {
        res.json(results);
      });
    });

    // Delete a book
    app.delete('/api/book/:id', function (req, res) {
      console.log('Book ID:');
      console.log(req.params.id);
      Book.destroy({
        where: {
          id: req.params.id,
        },
      }).then(function () {
        res.end();
      });
    });
  };
  ```

- Example -- SequelizeCLI -- /14-Full-Stack/01-Activities/05-SequelizeCLI

  ```javascript
  module.exports = function (sequelize, DataTypes) {
    var User = sequelize.define('User', {
      email: DataTypes.STRING,
      password: DataTypes.STRING,
    });
    return User;
  };
  ```

- Example -- /14-Full-Stack/09-Sequelize-Update-Delete
  - sequelize update()
  ```javascript
  // PUT route for updating todos. We can get the updated todo data from req.body
  app.put('/api/todos', function (req, res) {
    // Update takes in an object describing the properties we want to update, and
    // we use where to describe which objects we want to update
    db.Todo.update(
      {
        text: req.body.text,
        complete: req.body.complete,
      },
      {
        where: {
          id: req.body.id,
        },
      }
    ).then(function (dbTodo) {
      res.json(dbTodo);
    });
  });
  ```
- Sequelize validation

  - example

  ```javascript
  module.exports = function (sequelize, DataTypes) {
    var Todo = sequelize.define('Todo', {
      text: {
        type: DataTypes.STRING,
        // AllowNull is a flag that restricts a todo from being entered if it doesn't
        // have a text value
        allowNull: false,
        // len is a validation that checks that our todo is between 1 and 140 characters
        validate: {
          len: [1, 140],
        },
      },
      complete: {
        type: DataTypes.BOOLEAN,
        // defaultValue is a flag that defaults a new todos complete value to false if
        // it isn't supplied one
        defaultValue: false,
      },
    });
    return Todo;
  };
  ```

  - example => handle error

  ```javascript
  // =============================================================

  // Requiring our models
  var db = require('../models');

  // Routes
  // =============================================================
  module.exports = function (app) {
    // GET route for getting all of the todos
    app.get('/api/todos', function (req, res) {
      // findAll returns all entries for a table when used with no options
      db.Todo.findAll({}).then(function (dbTodo) {
        // We have access to the todos as an argument inside of the callback function
        res.json(dbTodo);
      });
    });

    // POST route for saving a new todo
    app.post('/api/todos', function (req, res) {
      // create takes an argument of an object describing the item we want to
      // insert into our table. In this case we just we pass in an object with a text
      // and complete property (req.body)
      db.Todo.create({
        text: req.body.text,
        complete: req.body.complete,
      })
        .then(function (dbTodo) {
          // We have access to the new todo as an argument inside of the callback function
          res.json(dbTodo);
        })
        .catch(function (err) {
          // Whenever a validation or flag fails, an error is thrown
          // We can "catch" the error to prevent it from being "thrown", which could crash our node app
          res.json(err);
        });
    });

    // DELETE route for deleting todos. We can get the id of the todo to be deleted from
    // req.params.id
    app.delete('/api/todos/:id', function (req, res) {
      // We just have to specify which todo we want to destroy with "where"
      db.Todo.destroy({
        where: {
          id: req.params.id,
        },
      }).then(function (dbTodo) {
        res.json(dbTodo);
      });
    });

    // PUT route for updating todos. We can get the updated todo data from req.body
    app.put('/api/todos', function (req, res) {
      // Update takes in an object describing the properties we want to update, and
      // we use where to describe which objects we want to update
      db.Todo.update(
        {
          text: req.body.text,
          complete: req.body.complete,
        },
        {
          where: {
            id: req.body.id,
          },
        }
      )
        .then(function (dbTodo) {
          res.json(dbTodo);
        })
        .catch(function (err) {
          // Whenever a validation or flag fails, an error is thrown
          // We can "catch" the error to prevent it from being "thrown", which could crash our node app
          res.json(err);
        });
    });
  };
  ```

- Sequelize association

  - The following three methods will cause Sequelize to automatically add foreign keys to the appropriate models (unless they are already present).

  - hasMany()

    - The A.hasMany(B) association means that a One-To-Many relationship exists between A and B
    - with the foreign key being defined in the target model ( B ).

  - belongsTo()

    - The A. belongsTo(B) association means that a One-To-One relationship exists between A and B
    - with the foreign key being defined in the source model ( A ).

  - hasOne()

    - The A.hasOne(B) association means that a One-To-One relationship exists between A and B, with the foreign key being defined in the target model (B).

  - belongsToMany()

    - The A.belongsToMany(B, { through: 'C' }) association means that a Many-To-Many relationship exists between A and B
    - using table C as junction table, which will have the foreign keys (aId and bId, for example).
    - Sequelize will automatically create this model C (unless it already exists) and define the appropriate foreign keys on it.
      - In the examples above for belongsToMany, a string ('C') was passed to the through option. In this case, Sequelize automatically generates a model with this name. However, you can also pass a model directly, if you have already defined it.

  - Creating the standard relationships

    - One-To-One relationship
      - To create a One-To-One relationship, the hasOne and belongsTo associations are used together;
    - One-To-One relationship
      - To create a One-To-Many relationship, the hasMany and belongsTo associations are used together;
    - To create a Many-To-Many relationship, two belongsToMany calls are used together.

  - example -- /14-Full-Stack/13-Post-Author-Association

    ```javascript
    var Author = sequelize.define('Author', {
      // Giving the Author model a name of type STRING
      name: DataTypes.STRING,
    });

    Author.associate = function (models) {
      // Associating Author with Posts
      // When an Author is deleted, also delete any associated Posts
      Author.hasMany(models.Post, {
        onDelete: 'cascade',
      });
    };

    var Post = sequelize.define('Post', {
      title: {
        type: DataTypes.STRING,
        allowNull: false,
        validate: {
          len: [1],
        },
      },
      body: {
        type: DataTypes.TEXT,
        allowNull: false,
        len: [1],
      },
    });

    Author.associate = function (models) {
      // Associating Author with Posts
      // When an Author is deleted, also delete any associated Posts
      Author.hasMany(models.Post, {
        onDelete: 'cascade',
      });
    };

    Post.associate = function (models) {
      // We're saying that a Post should belong to an Author
      // A Post can't be created without an Author due to the foreign key constraint
      Post.belongsTo(models.Author, {
        foreignKey: {
          allowNull: false,
        },
      });
    };
    ```

- Question: How would I query for all the records where the Independence Year was less than 50 years ago?

  ```javascript
  tableName.findAll({
    where: {
      IndependenceYear: { $gt: new Date().getFullYear() - 50 },
    },
  });
  ```

- How would I query the table, order it by descending Independence Years, and limit the results to just show 2 of the records. Skipping the first two? (i.e. Results: Zambia, Afghanistan)

  ```javascript
  tableName.findAll({
    offset: 2,
    limit: 2,
    order: [[sequelize.col('IndependenceYear'), 'DESC']],
  });
  ```

- Bonus: How do I use sequelize to make changes to an existing table with data in it?

  - Use sequelize migrations from the command line: <http://docs.sequelizejs.com/en/latest/docs/migrations/>

- **filename, **dirname
  - \_\_filename:
    - The file name of the current module. This is the current module file's absolute path with symlinks resolved.
    - The \_\_filename represents the filename of the code being executed.
  - \_\_dirname:
    - The directory name of the current module.
  - Example: running node example.js from /Users/mjr
    ```javascript
    console.log(__filename);
    // Prints: /Users/mjr/example.js
    console.log(__dirname);
    // Prints: /Users/mjr
    console.log(path.dirname(__filename));
    // Prints: /Users/mjr
    ```
  - Given two modules: a and b, where b is a dependency of a and there is a directory structure of:
    - /Users/mjr/app/a.js
    - /Users/mjr/app/node_modules/b/b.js
    - a requires b inside file a
    - References to \_\_filename within b.js will return /Users/mjr/app/node_modules/b/b.js
    - while references to \_\_filename within a.js will return /Users/mjr/app/a.js.
- path.basename

  - The path.basename() method returns the filename part of a file path.
  - The path.basename() method returns the last portion of a path
  - https://nodejs.org/api/path.html#path_path_basename_path_ext
  - Example:

    ```javascript
    path.basename('/foo/bar/baz/asdf/quux.html');
    // Returns: 'quux.html'

    path.basename('/foo/bar/baz/asdf/quux.html', '.html');
    // Returns: 'quux'
    ```

- process.env.NODE_ENV
  - The process.env property returns an object containing the user environment
  - the Express web server framework using an environment variable called NODE_ENV as a flag to
    - indicate whether the server should be running in “development” mode vs “production” mode.
    - At runtime, the script looks up that value by checking process.env.NODE_ENV.
  - NODE_ENV
    - NODE_ENV is a system environment variable that Node exposes into running scripts.
    - It’s used by convention to determine dev-vs-prod behavior, by both server tools, build scripts, and client-side libraries.
    - NODE_ENV is an environment variable made popular by the express web server framework.
    - When a node application is run, it can check the value of the environment variable and do different things based on the value.
    - NODE_ENV specifically is used (by convention) to state whether a particular environment is a production or a development environment.
    - Convention has dictated that there are two 'main' values you should use for NODE_ENV, either production or development, all lowercase.
  - Example
    ```javascript
    var env = process.env.NODE_ENV || 'development';
    // if process.env.NODE_ENV exists, env = "production", if not, env = "development"
    var config = require(__dirname + '/../config/config.json')[env];
    // get the right object from config.json according to the value of env
    ```
- use_env_variable:

  - js file in the models folder, some required node modules were imported, the line with config.
  - use_env_variable checks if any environment variable is set, if it is set then we use the settings for that environment variable otherwise we use the alternative settings provided for that environment. the process.
  - Example

  ```javascript
    production: {
    use_env_variable: process.env.DATABASE_URL,
    dialect: 'postgres',
    dialectOptions: {
      ssl: {
        require: true,
        rejectUnauthorized: false, // <<<<<<< YOU NEED THIS TO FIX UNHANDLED REJECTION
      },
    },

    if (config.use_env_variable) {
      var sequelize = new Sequelize(process.env[config.use_env_variable], config);
    } else {
      var sequelize = new Sequelize(config.database, config.username, config.password, config);
    }

  ```

![Image](https://mdn.mozillademos.org/files/14456/MVC%20Express.png)

- /models/index.js

  - This is file is autogenerated by the command "sequelize init"
    - "sequelize init => initialize project with sequelize cli pacakge
      - If this produces an error, then you may not have the sequelize and the sequelize-cli installed globally.
      - Fix this by running `npm install -g sequelize sequelize-cli` in your terminal and trying again.
  - In this file, we are requiring the modules we’re going to be using.
  - Then, we’re reading the configuration specific to our current Node environment
    - If we don’t have a Node environment defined, we’re defaulting to development.
  - Then, we are establishing a connection with our database,
  - Then , we read our models folder,
    - discovering and importing any and all the models in it
    - adding them to the db object
    - applying relationships between the models, if such relationships exist.
  - code example of /models/index.js
  - If you are windows user

    - correct the config file path in models/index.js
    - windows: var config = require(\_\_dirname + '/../config/config.json')[env]
    - other: var config = require(\_\_dirname + '/..\config\config.json')[env]

    ```javascript
    'use strict';

    var fs = require('fs');
    var path = require('path');
    var Sequelize = require('sequelize');
    var basename = path.basename(module.filename);
    var env = process.env.NODE_ENV || 'development';
    var config = require(__dirname + '/../config/config.json')[env];
    var db = {};

    if (config.use_env_variable) {
      var sequelize = new Sequelize(process.env[config.use_env_variable]);
    } else {
      var sequelize = new Sequelize(
        config.database,
        config.username,
        config.password,
        config
      );
    }

    fs.readdirSync(__dirname)
      .filter(function (file) {
        return (
          file.indexOf('.') !== 0 &&
          file !== basename &&
          file.slice(-3) === '.js'
        );
      })
      .forEach(function (file) {
        var model = sequelize['import'](path.join(__dirname, file));
        db[model.name] = model;
      });

    Object.keys(db).forEach(function (modelName) {
      if (db[modelName].associate) {
        db[modelName].associate(db);
      }
    });

    db.sequelize = sequelize;
    db.Sequelize = Sequelize;

    module.exports = db;
    ```

- Define relationships between models

  - company and employees

    - company has many employees
    - employee can only belongs to one company

  - One to Many => Foreign key

    - where the foreign key would be placed.
      - There is only one option in One-To-Many
      - it the company has many employees, the foreign key must be at employee table
    - the main way to do it used a pair of Sequelize associations (hasMany and belongsTo).

  - Company

    ```javascript
      module.exports = (sequelize, DataTypes) => {
        var Company = sequelize.define('Company', {
          name: {
            type:DataType.STRING,
            allowNull: false,
          },
        });

        Company.associate = function(mdoels) {
          // association is defined here
          Company hasMany(models.Employee, {
            foreignKey: "companyId",
            as: "employees'
          })
        }
        return Company;
      };
    ```

    - as: "employee"
      - every time we query for a company and include it's employee details
      - they'll be included under the key employees, instead of Employees
      - Sequelize defaults to using the pluralized model name

  - Employee

    ```javascript
      module.exports = (sequelize, DataTypes) => {
        var Company = sequelize.define('Employee', {
          name: {
            type:DataType.STRING,
            allowNull: false,
          },
          designation: {
            type:DataType.STRING,
            defaultValue: false,
          }
        });

        Employee.associate = function(mdoels) {
          // association is defined here
          Employee belongsTo(models.Company, {
            foreignKey: "companyId",
            onDelete: 'CASCADE'
          })
        }
        return Employee;
      };
    ```

    - defaultValue:
      - In general, having a default value means that if we don't provide a value for that field when creating it
      - the database is going to use the provided default value for that field.
    - onDelete: 'CASCADE'
      - if we delete a Company, it's associated Employees Details should be deleted as well
      - cascade the delete action

  - Many to Many relationships

    - Junction model is used for the many to many relationship

      - This will be an extra model (and extra table in the database)
      - have two foreign key columns and will keep track of the associations.
      - The junction table is also sometimes called join table or through table.

    - exmaple code https://sequelize.org/master/manual/assocs.html

      - Movie and Actor
      - One actor may have participated in many movies
      - one movie had many actors involved with its production
      - The junction table that will keep track of the associations will be called ActorMovies

        - which will contain the foreign keys movieId and actorId.

      - 1. **_through_** method

        ```javascript
        const Movie = sequelize.define('Movie', { name: DataTypes.STRING });
        const Actor = sequelize.define('Actor', { name: DataTypes.STRING });
        Movie.belongsToMany(Actor, { through: 'ActorMovies' });
        Actor.belongsToMany(Movie, { through: 'ActorMovies' });
        ```

      - the string _ActorMovies_ was given in the _through_ option of the _belongsToMany_ call
      - Sequelize will automatically create the _ActorMovies_ model which act as the junction model

      - 2. passsing a model directly
        ```javascript
        const Movie = sequelize.define('Movie', { name: DataTypes.STRING });
        const Actor = sequelize.define('Actor', { name: DataTypes.STRING });
        const ActorMovies = sequelize.define('ActorMovies', {
          MovieId: {
            type: DataTypes.INTEGER,
            references: {
              model: Movie, // 'Movies' would also work
              key: 'id',
            },
          },
          ActorId: {
            type: DataTypes.INTEGER,
            references: {
              model: Actor, // 'Actors' would also work
              key: 'id',
            },
          },
        });
        Movie.belongsToMany(Actor, { through: ActorMovies });
        Actor.belongsToMany(Movie, { through: ActorMovies });
        ```
      - Optoins:
        - Unlike One-To-One and One-To-Many relationships
          - the defaults for both ON UPDATE and ON DELETE are CASCADE for Many-To-Many relationships.
          -

- Associations

  - https://sequelize.org/master/manual/assocs.html

- DELETE CASCADE:

  - When we create a foreign key using this option, it deletes the referencing rows in the child table when the referenced row is deleted in the parent table which has a primary key.

- UPDATE CASCADE:
  - When we create a foreign key using UPDATE CASCADE the referencing rows are updated in the child table when the referenced row is updated in the parent table which has a primary key.
- The ON DELETE CASCADE and ON DELETE RESTRICT are the foreign key property and you set them when you are creating the relationship between two tables.
  - If you set the relationship to be ON DELETE CASCADE, when you run a DELETE statement on a parent table it will DELETE all the corresponding rows from the CHILD table automatically.
  - But the RESTRICT (which is the default foreign key relationship behavior) is when you try to delete a row from the parent table and there is a row in the child table with the same ID, it will fail complaining about the existing child rows.
- On Delete Cascade: when data is removed from a parent table, automatically data deleted from child table (foreign key table).
- On Delete set Null: when data is removed from a parent table, the foreign key associated cell will be null in a child table.
- On Delete Restrict: when data is removed from a parent table, and there is a foreign key associated with child table it gives error, you can not delete the record.

- RESTRICT prevents the action from happening if there's any foreign keys that rely on the field that's being changed.

- CASCADE
  - ON DELETE CASCADE
    - means that if the parent record is deleted, any child records are also deleted.
  - ON UPDATE CASCADE
    - means that if the parent primary key is changed, the child value will also change to reflect that.
- RESTRICT
  - ON DELETE or ON UPDATE
    - RESTRICT means that any attempt to delete and/or update the parent will fail throwing an error.
    - This is the default behaviour
- NO ACTION
  - In MySQL, equivalent to RESTRICT.
- SET NULL
  - Delete or update the row from the parent table, and set the foreign key column or columns in the child table to NULL.
- SET DEFAULT
  - Allows the developer to specify a value to which to set the foreign key column(s) on an UPDATE or a DELETE.
