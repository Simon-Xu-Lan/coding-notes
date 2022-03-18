To serve static files such as images, CSS files, and JavaScript files, use the express.static built-in middleware function in Express.
express.static() expects the first parameter to be a path of a directory, not a filename.

```js
// Static directory to be served
app.use(express.static('app/public'));
```
