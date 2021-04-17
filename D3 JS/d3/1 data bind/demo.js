// d3.select('ul')
//   .selectAll('li')
//   .each(function (d, i) {
//     console.log('element', this);
//     console.log('data', d);
//     console.log('index', i);
//   });

// d3.select('ul')
//   .selectAll('li')
//   .each((d, i) => {
//     console.log('element1', this);
//     console.log('data1', d);
//     console.log('index1', i);
//   });

var arr = [50, 55, 53];

// returns an array of undefined items
// d3.select('ul').selectAll('li').data();

// // assign data to elements in the selector object
// d3.select('ul').selectAll('li').data(arr);

// // get an arr of [50, 55, 53]
// d3.select('ul').selectAll('li').data();

// === no data bind
var elements = d3.select('ul').selectAll('li').data();
console.log('no data', elements);
// output: [undefined, undefined, undefined]

// === not enough
var arr = [50, 55];
d3.select('ul').selectAll('li').data(arr);

var elements = d3.select('ul').selectAll('li').data();
console.log('not enough', elements);
// output: [50, 55, undefined]

// === just right
var arr = [50, 55, 53];
d3.select('ul').selectAll('li').data(arr);
var elements = d3.select('ul').selectAll('li').data();
console.log('just right', elements);
// output: [50, 55, 53]

// === too many
var arr = [50, 55, 53, 56, 68];
d3.select('ul').selectAll('li').data(arr);
var elements = d3.select('ul').selectAll('li').data();
console.log('too many', elements);
// output: [50, 55, 53]

// === update existing elements
// Use `enter` to create new elements
var arr = [50, 55, 53, 56, 68];
// First, update existing elements
// d3.select('ul')
//   .selectAll('li')
//   .data(arr)
//   .text(function (d) {
//     return d;
//   });

// === Second, create new elements for extra data points
d3.select('ul')
  .selectAll('li')
  .data(arr)
  .enter()
  .append('li')
  .text(function (d) {
    return d;
  });

// Together updating existing elements and create new elements for extra data points
// d3.select('ul')
//   .selectAll('li')
//   .data(arr)
//   .text(function (d) {
//     return d;
//   })
//   .enter()
//   .append('li')
//   .text(function (d) {
//     return d;
//   });

// === remove extra data points
// var arr = [50, 55];
// d3.select('ul').selectAll('li').data(arr).exit().remove();
