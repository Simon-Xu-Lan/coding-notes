function barChart(elementId, data) {
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

  // Configure a band scale for the horizontal axis with a padding of 0.1 (10%)
  var xBandScale = d3
    .scaleBand()
    .domain(data.map((d) => d.name))
    .range([0, chartWidth])
    .padding(0.1);

  // Create a linear scale for the vertical axis.
  // Here the 0 of y correspond to chartHeight of range, the max of y correspond to 0 of range
  var yLinearScale = d3
    .scaleLinear()
    .domain([0, d3.max(data.map((d) => d.hours))])
    .range([chartHeight, 0]);

  // Create two new functions passing our scales in as arguments
  // These will be used to create the chart's axes
  var bottomAxis = d3.axisBottom(xBandScale);
  var leftAxis = d3.axisLeft(yLinearScale).ticks(10);

  // Append two SVG group elements to the chartGroup area,
  // and create the bottom and left axes inside of them
  chartGroup.append('g').call(leftAxis);

  chartGroup
    .append('g')
    .attr('transform', `translate(0, ${chartHeight})`)
    .call(bottomAxis);

  // Create one SVG rectangle per piece of tvData
  // Use the linear and band scales to position each rectangle within the chart
  chartGroup
    .selectAll('.bar')
    .data(data)
    .enter()
    .append('rect')
    .attr('class', 'bar')
    .attr('x', (d) => xBandScale(d.name))
    .attr('y', (d) => yLinearScale(d.hours))
    .attr('width', xBandScale.bandwidth())
    .attr('height', (d) => chartHeight - yLinearScale(d.hours));
}
