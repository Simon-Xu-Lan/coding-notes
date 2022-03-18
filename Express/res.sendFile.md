- The Express framework provides a sendFile() method available on the response object which can be used to send static files to the client.
- sendFile() can be used to serve static files.

- Here is an example of using res.sendFile() to deliver an HTML page.

```js
var express = require('express');
var app = express();
var path = require('path');

// viewed at http://localhost:8080
app.get('/', function (req, res) {
  res.sendFile(path.join(__dirname + '/index.html'));
});

app.listen(8080);
```
