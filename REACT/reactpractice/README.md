- **Q** What are some benefits of using ReactJS?

  - **A**

    - **Fast Learning Curve:** React _is_ more complicated to learn and use than jQuery, but this is an unfair comparison because the two aren't even in the same league. Compared to other competing JavaScript libraries and frameworks such as Angular or Ember, React has much less code that we as developers need to memorize or worry about, making it much faster to learn.

    - **React is Component Based:** With React we can build encapsulated components that manage their own state, then compose them to make complex UIs. Since our components are written in JavaScript instead of HTML, we can easily pass data into our application and keep our state out of the DOM.

    - **With React, you can "Learn Once, Write Anywhere":** React only tries to be the view layer of our application (the V in MVC). Because of this, it makes no assumptions about the rest of our application, and can be rendered on the client, on the server using node, even in native mobile applications with React Native.

- **Q** What is a React component?

  - **A** "Components let you split the UI into independent, reusable pieces, and think about each piece in isolation. Components can be defined as JavaScript functions or ES6 classes." Essentially components are responsible for rendering some part of an application's UI.

- **Q** What is the significance of the `ReactDOM.render` method?

  - **A** `ReactDOM` is a package separate from the `React` package that provides APIs for DOM specific methods.

  * `ReactDOM.render` takes a React component, or tree of React components and (eventually) renders them to the DOM.
    - For the most part, we generally only run this method once per React app to render a single root component containing all of our other components.

- **Q** What is JSX? Why does Facebook recommend it?

  - **A** JSX is a syntax extension to JavaScript that _looks like_ HTML.

  * Facebook recommends JSX because it's familiar HTML-like syntax makes it easy to describe the UI a component should produce.
  * It is possible to write React applications without using JSX, but the process is less intuitive.

- **Q** What does Facebook recommend as the “best way to start building a new React single page application”?

  - **A** They recommend everyone begin with [Create React App](https://github.com/facebookincubator/create-react-app).

  * Normally, setting up a robust React application from scratch requires a deep understanding of build tools such as
    - [Webpack](https://webpack.js.org/) (used for bundling an application's assets) and
    - [Babel](http://babeljs.io/) (used for transpiling JSX and ES6+ code to plain, widely supported, ES5 JavaScript).
  * Thankfully, we can use Create React App to quickly scaffold out a React app in seconds with all of the features and configuration we'd need for _most_ applications.

- **Q** What is Babel? And what role does it play in converting JSX into vanilla JavaScript?

  - **A** [Babel](http://babeljs.io/) is a JavaScript compiler.

  * It takes next generation JavaScript (ES6/ES7/ES8) and compiles it down to widely supported ES5 JavaScript code.
  * It also compiles JSX code down to regular JavaScript functions that browsers can understand.
  * Developers can also extend the JavaScript syntax and add on their own features, and share them with others in the form of a Babel plugin.

- **Q** What is the significance of { } curly braces in JSX?

  - **A** The { } single curly braces inside of JSX work similarly to the {{ }} double curly braces in handlebars:

  * they allow us to pass values and expressions into our view.

- **Q** What is a component prop?

  - **A** A prop is essentially a function argument that's passed into our component from outside and can be used inside of it.

  * For example, we could write a component for a button that renders different types of buttons depending on the prop it's passed.

# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `yarn start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.

### `yarn test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `yarn build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `yarn eject`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

If you aren’t satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn’t feel obligated to use this feature. However we understand that this tool wouldn’t be useful if you couldn’t customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `yarn build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)
