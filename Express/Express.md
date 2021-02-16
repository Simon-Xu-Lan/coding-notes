- Express
  - a web application framework for Node.js.
  - free, open-source, fast, and minimalist
- express.urlencoded()
  - is a built-in middleware function in Express.
  - It parses incoming requests with urlencoded payloads
  - is based on body-parser.
  - Return Value: It retuns an Object.
- express.urlencoded({extended: true})
  - If extended is false, you can not post "nested object"
  - If extended is true, you can do whatever way that you like.
  - The “extended” syntax allows for rich objects and arrays to be encoded into the URL-encoded format
  - basically tells the system whether you want to use a simple algorithm for shallow parsing (i.e. false) or complex algorithm for deep parsing that can deal with nested objects (i.e. true).
- URL

  - Uniform Resource Locator
  - Web browsers request pages from web servers by using a URL
  - The URL is the address of a web page, like: https://www.w3schools.com
  - A URL (Uniform Resource Locator) is the address of a resource in the world wide web.
  - Following is an example of a URL that you see more often on the internet
    - https://www.google.com/search?q=hello+world#brs

- URL Encoding

  - URL encoding converts characters into a format that can be transmitted over the Internet.
  - URL Encoding converts reserved, unsafe, and non-ASCII characters in URLs to a format that is universally accepted and understood by all web browsers and servers.
  - URLs can only be sent over the Internet using the ASCII character-set.
  - Since URLs often contain characters outside the ASCII set, the URL has to be converted into a valid ASCII format.
  - URL encoding replaces unsafe ASCII characters with a "%" followed by two hexadecimal digits.
  - URLs cannot contain spaces. URL encoding normally replaces a space with a plus (+) sign or with %20.

- express.json()
  - a built-in middleware function in Express.
  - It parses incoming requests with JSON payloads and is based on body-parser.
- app.use(bodyParser.json()) basically tells the system that you want json to be used.

- JSON parse

  - A common use of JSON is to exchange data to/from a web server.
  - When receiving data from a web server, the data is always a string.
  - Parse the data with JSON.parse(), and the data becomes a JavaScript object.

- URL encoding and JSON encoding both allow to convert a (nested) object to string, but the format is different. An URL encoded string is in general not a valid JSON string.

- app.use(a function)

  - add the function as middlewares/add the function to middleware stack
  - when that function is passed into app.use, it acts just like any other middleware.
  - To setup your middleware, you can invoke app.use(<specific_middleware_layer_here>)
  - for every middleware layer that you want to add (it can be generic to all paths, or triggered only on specific path(s) your server handles),
  - and it will add onto your Express middleware stack.
  - Middleware layers can be added one by one in multiple invocations of use
  - or even all at once in series with one invocation.

  - by adding bodyParser, you're ensuring your server handles incoming requests through the express middleware
  - So, now parsing the body of incoming requests is part of the procedure that your middleware takes when handling incoming requests
    -- all because you called app.use(bodyParser).

  - https://stackoverflow.com/questions/11321635/nodejs-express-what-is-app-use

- res.status

  - res.sendStatus(200) // equivalent to res.status(200).send('OK')
  - res.sendStatus(403) // equivalent to res.status(403).send('Forbidden')
  - res.sendStatus(404) // equivalent to res.status(404).send('Not Found')
  - res.sendStatus(500) // equivalent to res.status(500).send('Internal Server Error')
  - So if you don’t want to customize the message that will be sent back - use sendStatus.
  - res.status(statusCode).send(message) allows you to specify the custom message.

- res.send()

  - The res.send() function basically sends the HTTP response.
  - The body parameter can be
    - a String or
    - a Buffer object or
    - an object or
    - an Array.
  - Syntax:
    - res.send( [body] )
    - parameter:
      - This function accepts a single parameter body
        - that describe the body which is to be sent in the response.
  - If no argument is provided, no response body is sent back—just the status code.
  - The res.send() function is the most basic way to send an HTTP response.

- res.json()

  - If you want to send a dictionary or JSON, use res.json().

- Response

  - Whenever an Express application server receives an HTTP request, it will provide the developer with an object, commonly referred to as res.
  - The res object is an enhanced version of the response object found in Node.js.
  - res => Express response object

- res.end()

  - We can use res.end() if we want to end the response without providing any data.
  - This could be useful for a 404 page, for example:
    - res.status(404).end();
  - In the code above we are explicitly setting the HTTP status code and immediately after that ending the response.

- res.send() vs res.json()

  - res.json() allows for extra formatting of the JSON data - if this is not required
  - res.send() can also be used to return a response object using Express.
  - Both of these methods also end the response correctly, and there's no further action required.
  - **Basic Response using res.end()**

    - The res.send() function is the most basic way to send an HTTP response.
    - Calling res.send() with a string sends a response with the string as the response body and content type set to 'text/html; charset=utf-8'.

    ```javascript
    const axios = require('axios');
    const express = require('express');
    const app = express();

    app.get('*', function (req, res) {
      res.send('Hello, World');
    });

    const server = await app.listen(3000);

    const response = await axios.get('http://localhost:3000');
    response.data; // 'Hello, World'
    response.headers['content-type']; // 'text/html; charset=utf-8'
    ```

  - **JSON Responses Using res.json()**

    - If you're building a RESTful API or another backend service that sends responses in JSON
      - you should use res.json()
    - The res.json() function converts the given object to JSON using JSON.stringify() and sets the content type to 'application/json; charset=utf-8'.

    ```javascript
    const axios = require('axios');
    const express = require('express');
    const app = express();

    app.get('*', function (req, res) {
      res.json({ answer: 42 });
    });

    const server = await app.listen(3000);

    const response = await axios.get('http://localhost:3000');
    response.data; // { answer: 42 }
    response.headers['content-type']; // 'application/json; charset=utf-8'
    ```

- **Setting the Response Status**

  - res.status()
    - The res.status() function lets you set the response status.
    - res.status() does not actually send the response
    - That's why you will usually see res.status().json() or res.status().send()
    - The res.status() function lets you set HTTP response headers.

- Response Headers

  - Response headers hold additional information about the response, like its location or about the server providing it.
  - A response header is an HTTP header
    - that can be used in an HTTP response
    - and that doesn't relate to the content of the message.

- What Happens if you don't send a Response

  - The response will hang forever if you don't send a response
  - Express will not throw any error if you don't send a response
  - Sending response using res.json(), res.send(), res.end(), res.render()

  ```javascript
  // Express won't throw an error, but any request to this endpoint will hang forever because there's no `res.send()`.
  app.get('*', function (req, res) {
    res.status(201);
  });
  ```

- res.render()

  - The res.render() function is used to render a view and sends the rendered HTML string to the client. Syntax: res.render(view [, locals] [, callback]).
  - Parameters: This function accept two parameters as mentioned above and described below:
    - Locals: It is basically an object whose properties define local variables for the view.
    - Callback It is a callback function.
    - Returns: It retuns an Object.

- req.params, req.query and req.body

  - are part of Express request object.
  - are used by the client to send data to the server.
  - differences
  - https://dev.to/remi/express-req-params-req-query-and-req-body-4lpc

    - req.body

      - Generally used in POST/PUT requests.
      - Use it when you want to send sensitive data(eg. form data)
      - or super long JSON data to the server.
      - how to send data in request body

        ```javascript
        // Using axios
        axios.post('/giraffe', {
          key1: 'value1',
          key2: 'value2'
        })
        .then(response => {
          ...
        })
        .catch(error => {
          ...
        })

        ```

      - How to get data from request body

        ```javascript
        app.get('/giraffe', (req, res) => {
          console.log(req.body.key1); //value1
          console.log(req.body.key2); //value2
        });
        ```

      - **Remember to use express.json() middleware to parse request body else you'll get an error**
        - app.use(express.json())

    - req.params

      - These are properties attached to the url
      - route parameters
      - You prefix the parameter name with a colon(:) when writing your routes.
      - For instance

        ```javascript
        app.get('/giraffe/:number', (req, res) => {
          console.log(req.params.number);
        });

        // To send the parameter from the client, just replace its name with the value
        GET  http://localhost:3000/giraffe/1

        ```

    - req.query

      - mostly used for searching,sorting, filtering, pagination,
      - for instance you want to query an API but only want to get data from page 10
      - It written as key=value

        ```javascript
        GET  http://localhost:3000/animals?page=10

        // To access this in your express server is pretty simple too;
        app.get('/animals', ()=>{
          console.log(req.query.page) // 10
        })
        ```

# Setup

```js
const express = require('express');

const app = express();

app.get('/', function (req, res) {
  res.send('Hello World!');
  res.end();
});

app.listen(3000, () => {
  console.log('Server is listening on PORT: ${3000}');
});
```

# body-parser

- body-parser extract the entire body portion of an incoming request stream and exposes it on req.body.
- To handle HTTP POST request in Express.js version 4 and above, you need to install middleware module called body-parser.
- This body-parser module parses the JSON, buffer, string and URL encoded data submitted using HTTP POST request. Install body-parser using NPM as shown below.

  - npm install body-parser --save

- bodyParser.urlencoded():
  - Parses the text as URL encoded data (which is how browsers tend to send form data from regular forms set to POST)
  - and exposes the resulting object (containing the keys and values) on req.body.
- bodyParser.json():

  - Parses the text as JSON and exposes the resulting object on req.body.

- bodyParser.text():
  - Reads the buffer as plain text and exposes the resulting string on req.body.
- bodyParser.raw():
  - Doesn't actually parse the body, but just exposes the buffered up contents from before in a Buffer on req.body.

## app.use(bodyParser.urlencoded({ extended: true }));

- to parse the information that is sent from the post request
- urlencoded to parse the data from html form
- by setting extended option to be true, it allows us to post nested object

- the extended:
  - true precises that the req.body object will contain values of any type instead of just strings.

## req.body

- The parsed version of http request
