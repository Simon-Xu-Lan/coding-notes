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

# Hello React

In this activity, we will dissect a simple React application.

## Instructions

- If you haven't already, generate a starter React app using Create React App. You can do this by running `npx create-react-app reactpractice`. We will run all of the activity code today inside of this boilerplate, as to avoid constantly reinstalling the same node modules.

- Once you have a `reactpractice` React app generated, delete the `src` folder inside of your starter app and replace it with the [src](Unsolved/src) provided with this activity.

- Start the app by running `npm start` in your terminal, take a moment to study the HTML code being rendered in the browser at [http://localhost:3000](http://localhost:3000).

### HelloReact.js

- Then go into the `src` folder and with your partner, try to answer the following questions:

  - What's happening inside of `src/components/HelloReact.js`? How does it relate to the content being rendered to the browser?

### App.js

- Open the `src/App.js` file, what's going on in this file? Try to answer the following questions:

  - What does the `App` function return?

  - Why do we import the React library? We aren't using the React keyword anywhere. Is it possible to remove this and still have our code work?

### index.js

- Open the `src/index.js` file and go over the code. Notice that we're importing the `ReactDOM` library. Try to answer the following questions:

  - Do you remember what the purpose of `ReactDOM.render` is? What is it doing?

  - Is this where our components are rendered to the DOM?

  - Instead of splitting our files up into `App`, `components/HelloReact` and `index`, is it possible to just write our entire Hello World app in the `index.js` file?

### important

- In order to return separate JSX elements from a function, all of the higher level elements need a single parent, e.g., usually a `div`.

- All JSX tags must either have an adjacent tag or else have a self-closing forward slash.

- `className` must be used to describe an element's `class` property since `class` is a reserved word in JavaScript.

- Remember to import the `react` library in any file where JSX is utilized. Inspect some of the other files provided with the starter code if you're having difficulty remembering the syntax for this.
