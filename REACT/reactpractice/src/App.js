import React from 'react';
import Navbar from './components/Navbar';
import Card from './components/Card';
import Jumbotron from './components/Jumbotron';
import JSXVariables from './components/JSXVariables';
import JSXVariables2 from './components/JSXVariables2';

function App() {
  return (
    <div className="container">
      <Navbar />
      <Jumbotron />
      <Card />
      <JSXVariables />
      <JSXVariables2 />
    </div>
  );
}

export default App;
