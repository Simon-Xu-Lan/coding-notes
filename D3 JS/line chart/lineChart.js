function lineChart(elementId, data) {
  // elementId is the id of div where we put the bar chart

  // svgWidth and svgHeight defien SVG area dimensions
  // Find the actual size of slot in screen and assign it to svgWidth is the
  let svgWidth = document.getElementById(elementId).clientWidth;
  // the ideal width/height ratio is 16/9
  let svgHeight = (svgWidth * 9) / 16;

  // Define the chart's margin as an object
  // Set 5% margtin percent
  let MARGIN_PERCENT = 0.05;
  let chartMargin = {
    top: svgHeight * MARGIN_PERCENT,
    right: svgWidth * MARGIN_PERCENT,
    bottom: svgHeight * MARGIN_PERCENT,
    left: svgWidth * MARGIN_PERCENT,
  };

  // Define dimensions of the chart area
  let chartWidth = svgWidth - chartMargin.left - chartMargin.right;
  let chartHeight = svgHeight - chartMargin.top - chartMargin.bottom;

  // Select the div with id elementId, append SVG area to it, and set the dimensions
  var svg = d3
    .select('#' + elementId)
    .append('svg')
    .attr('height', svgHeight)
    .attr('width', svgWidth);

  // Append a group to the SVG area and shift ('translate') it to the right and to the bottom
  var chartGroup = svg
    .append('g')
    .attr('transform', `translate(${chartMargin.left}, ${chartMargin.top})`);

  // Create a scale for your independent (x) coordinates
  var xScale = d3
    .scaleLinear()
    .domain(d3.extent(data, (d) => d.year))
    .range([0, svgWidth]);

  // Create a scale for your dependent (y) coordinates
  var yScale = d3
    .scaleLinear()
    .domain([0, d3.max(data, (d) => d.lifeExpectancy)])
    .range([svgHeight, 0]);

  // create a line generator function and store as a variable
  // use the scale functions for x and y data
  var createLine = d3
    .line()
    .x((d) => xScale(d.year))
    .y((d) => yScale(d.lifeExpectancy));

  // Append a path element to the svg, make sure to set the stroke, stroke-width, and fill attributes.
  chartGroup
    .append('path')
    .attr('stroke', 'black')
    .attr('stroke-width', '1')
    .attr('fill', 'none')
    .attr('d', createLine(data));
}
