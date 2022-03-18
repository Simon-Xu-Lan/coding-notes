var booksReadThisYear = [17, 23, 20, 34];

// Setting the dimension for the svg container
var svgHeight = 600;
var svgWidth = 400;

var svg = d3
  .select('#svg-area')
  .append('svg')
  .attr('height', svgHeight)
  .attr('width', svgWidth);

// svgGroup now refers to the 'g' group element appended
// The SVG group would normally be aligned to the top left edge of the chart
// Now it is offset to the right and down using the tranform attribute
svgGroup = svg.append('g').attr('transform', 'translate(50, 100)');

// ===== vertical bar chart
// Select all rectangles currently on the page - which is none -
// and binds our dataset to them.
// it there is no rectangles, it will append one for each piece of data
svgGroup
  .selectAll('rect')
  .data(booksReadThisYear)
  .enter()
  .append('rect')
  .attr('width', 50)
  .attr('height', (data) => data * 10)
  .attr('x', (data, index) => index * 60)
  .attr('y', (data) => svgHeight - data * 10)
  .attr('class', 'bar');

// ===== horizontal bar chart

svgGroup
  .selectAll('rect')
  .data(booksReadThisYear)
  .enter()
  .append('rect')
  .attr('height', 50)
  .attr('width', (data) => data * 10)
  .attr('x', 50)
  .attr('y', (data, index) => svgHeight - 100 - (index + 1) * 60)
  .attr('class', 'bar');
