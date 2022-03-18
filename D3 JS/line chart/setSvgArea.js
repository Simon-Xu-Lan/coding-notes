function setSvgArea(elementId) {
  // elementId is the id of div where we put the bar chart

  // Define result as an empty object
  let result = {};
  // svgWidth and svgHeight defien SVG area dimensions
  // Find the actual size of slot in screen and assign it to svgWidth is the
  let svgWidth = document.getElementById(elementId).clientWidth;
  // the ideal width/height ratio is 16/9
  let svgHeight = (svgWidth * 9) / 16;

  // Define the chart's margin as an object
  // Set 5% margtin percent
  const MARGIN_PERCENT = 0.05;
  let chartMargin = {
    top: svgHeight * MARGIN_PERCENT,
    right: svgWidth * MARGIN_PERCENT,
    bottom: svgHeight * MARGIN_PERCENT,
    left: svgWidth * MARGIN_PERCENT,
  };

  // Define dimensions of the chart area
  result.chartWidth = svgWidth - chartMargin.left - chartMargin.right;
  result.chartHeight = svgHeight - chartMargin.top - chartMargin.bottom;

  // Select the div with id elementId, append SVG area to it, and set the dimensions
  var svg = d3
    .select('#' + elementId)
    .append('svg')
    .attr('height', svgHeight)
    .attr('width', svgWidth);

  // Append a group to the SVG area and shift ('translate') it to the right and to the bottom
  result.chartGroup = svg
    .append('g')
    .attr('transform', `translate(${chartMargin.left}, ${chartMargin.top})`);

  return result;
}
