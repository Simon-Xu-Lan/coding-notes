# req.body

— A new body Buffer containing the parsed data is populated on the request object after the middleware

- The req.body property contains key-value pairs of data submitted in the request body.
- By default, it is undefined and is populated when you use a middleware called body-parsing such as express.urlencoded() or express.json().
