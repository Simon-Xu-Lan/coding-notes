- React is Component Based:

  - With React we can build encapsulated components that manage their own state, then compose them to make complex UIs.
  - Since our components are written in JavaScript instead of HTML, we can easily pass data into our application and keep our state out of the DOM.

- With React, you can "Learn Once, Write Anywhere":

  - React only tries to be the view layer of our application (the V in MVC).
  - Because of this, it makes no assumptions about the rest of our application,
  - and can be rendered on the client, on the server using node, even in native mobile applications with React Native.

- React component

  - A "Components let you split the UI into independent, reusable pieces, and think about each piece in isolation.
  - Components can be defined as JavaScript functions or ES6 classes.
  - Essentially components are responsible for rendering some part of an application's UI.

- ReactDOM

  - A ReactDOM is a package separate from the React package that provides APIs for DOM specific methods.
  - ReactDOM.render
    - ReactDOM.render takes a React component, or tree of React components and (eventually) renders them to the DOM.
    - For the most part, we generally only run this method **once per React app** to render a single root component containing all of our other components.

- JSX

  - A JSX is a syntax extension to JavaScript that looks like HTML.
  - Facebook recommends JSX because it's familiar HTML-like syntax makes it easy to describe the UI a component should produce.

- Create React App

  - we can use Create React App to quickly scaffold out a React app in seconds with all of the features and configuration we'd need for most applications.
  - syntax:
    - npx create-react-app {project name}

- Babel

  - A Babel is a JavaScript compiler. It takes next generation JavaScript (ES6/ES7/ES8) and compiles it down to widely supported ES5 JavaScript code.
  - It also compiles JSX code down to regular JavaScript functions that browsers can understand.

- What is the significance of { } curly braces in JSX?

  - A The { } single curly braces inside of JSX work similarly to the {{ }} double curly braces in handlebars:
  - they allow us to pass values and expressions into our view.

- What is a component prop?

  - A prop is essentially a function argument that's passed into our component from outside and can be used inside of it.
  - For example, we could write a component for a button that renders different types of buttons depending on the prop it's passed.

- 'npm start'

  - Start the app by running `npm start` in your terminal

- import React library?

  - Why do we import the React library? We aren't using the React keyword anywhere.
  - Whenever we use JSX inside of our JavaScript, we need to import the React library.
    - When Babel translates our `App` component's JSX code to plain old JavaScript

- what the purpose of `ReactDOM.render` in index.js is?
  - We use `ReactDOM.render` to render a single component or tree of components to the DOM.
  - In normal case, `App` is the root of our component tree
    - it renders all of our other components inside.
