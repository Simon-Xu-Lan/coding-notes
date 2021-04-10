# what is an object

- Objects in JavaScript are unordered collections of related data built on a key:value structure where values can be any data-type, including functions.

# What is OOP

- Object-Oriented Programming
- OOP is a programming paradigm or pattern of programming centered around objects.
- Problems are thought of in a way in which a collection of objects work together to solve a problem.
- Objects can speak to one another,
- and this ability makes them suitable for managing and solving large and complex problems.

# Encapsulation

- Object data (and often, functions too) can be stored neatly

# Inheritance

- We can create new classed based on other classes

# Abstraction

- Creating a simple model of a more complexing thing

# Polymorphism

- The fancy word for the ability of mulitple object types to implement the same functionality

## constructor

- Constructors are special functions that are extremely useful in creating objects of similar types.
- Constructor function which can be used to create objects containing the properties "raining", "noise", and the "makeNoise()" function

```js
function Animal(raining, noise) {
  this.raining = raining;
  this.noise = noise;
  this.makeNoise = function () {
    if (this.raining === true) {
      console.log(this.noise);
    }
  };
}
```

- Another

```js
// constructor function which can be used to create "digitalpal" objects
var DigitalPal = function () {
  this.hungry = false;
  this.sleepy = false;
  this.bored = true;
  this.age = 0;
  this.houseQuality = 100;
};
```

## prototypes

- Prototypes are JavaScript’s built in system, allowing objects to inherit features from other objects.

- Prototype Inheritance

  - All JavaScript objects inherit properties and methods from a prototype

- The JavaScript prototype property allows you to add new properties and methods to object constructors:

```js
DigitalPal.prototype.feed = function () {
  if (this.hungry) {
    console.log('That was yummy!');
    this.hungry = false;
    this.sleepy = true;
  } else {
    console.log("No thanks, I'm full.");
  }
};
```

## js can not add a new property to an existing object constructor

## class

- ES6 introduced a `class` keyword which allows us to create objects using class structures similar to those found in other OOP programming languages.
- Under the hood, classes are just constructor functions with more intuitive syntax.
- Just like constructor functions, classes can accept arguments

```js
class Shape {
  // Just like constructor functions, classes can accept arguments
  constructor(area, perimeter) {
    this.area = area;
    this.perimeter = perimeter;
  }

  printInfo() {
    console.log(`Area: ${this.area}`);
    console.log(`Perimeter: ${this.perimeter}`);
  }
}
```
