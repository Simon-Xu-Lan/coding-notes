var dataArr = [10, 20, 2000];

console.log('min value ', d3.min(dataArr));
console.log('max value ', d3.max(dataArr));
console.log('min and max value', d3.extent(dataArr)); // output: [0, 2000]

// ===== scaleLinear
// Imagine you have test scores with possible scores from 0 to 100
// and you want to graph them in an SVG that is 1000 pixels high
var testScores = [50, 90, 95, 75, 85];

// == Solution 1: hard coded
var yScale = d3.scaleLinear().domain([0, 100]).range([0, 1000]);

// yScale is a function
console.log(yScale);
console.log('50 returns ', yScale(50));
console.log('75 returns ', yScale(75));
console.log('100 returns ', yScale(100));

// == Solution 2: with max and min
var svgHeight = 1000;
var yScale = d3
  .scaleLinear()
  .domain([0, d3.max(testScores)])
  .range([0, svgHeight]);

console.log('50 returns ', yScale(50));
console.log('75 returns ', yScale(75));
console.log('100 returns ', yScale(100));

// == Solution 3: extent
var svgHeight = 1000;
var yScale = d3
  .scaleLinear()
  .domain(d3.extent(testScores))
  .range([0, svgHeight]);

console.log('50 returns ', yScale(50));
console.log('75 returns ', yScale(75));
console.log('100 returns ', yScale(100));
