- config

  - INITIATES THE CONNECTION TO MYSQL
  - example code

  ```javascript
  // Dependencies
  var Sequelize = require('sequelize');

  // Creates mySQL connection using Sequelize, the empty string in the third argument spot is our password.
  var sequelize = new Sequelize('sequelize_library', 'root', '', {
    host: 'localhost',
    port: 3306,
    dialect: 'mysql',
    pool: {
      max: 5,
      min: 0,
      idle: 10000,
      acquire: 30000,
    },
  });

  // Exports the connection for other files to use
  module.exports = sequelize;
  ```

  - max -maximum number of connections permissible in a pool
  - min – minimum number of connections permissible in a pool
  - idle – maximum time, in terms of milliseconds, that a connection can be held idly before being released
  - acquire – maximum time, in terms of milliseconds, that the pool seeks to make the connection before an error message pops up on screen
