// ===== scaleBend
// imagine you want to visulize student grade information on a bar chart
var testScores = [90, 85, 75, 90];
var students = ['Han', 'Sarah', 'Matt', 'Ruchi'];

var svgHeight = 600;
var svgWidth = 1000;

var xScale = d3.scaleBand().domain(students).range([0, svgWidth]);
console.log(`Han's x-coordinate: ${xScale('Han')}`);
console.log(`Sarah's x-coordinate: ${xScale(students[1])}`);
console.log(`Matt's x-coordinate: ${xScale('Matt')}`);
console.log(`Ruchi's x-coordinate: ${xScale(students[3])}`);

// == bandWidth
console.log(`Each band is ${xScale.bandwidth()} pixels wide.`);

var yScale = d3.scaleLinear().domain([0, 100]).range([0, svgHeight]);

console.log(`The height of Han's bar: ${yScale(testScores[0])}`);
