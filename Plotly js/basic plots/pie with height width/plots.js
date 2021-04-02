// Create an array of each country's numbers
var us = Object.values(data.us);
var uk = Object.values(data.uk);
var canada = Object.values(data.canada);

console.log(us);

var datasets = data;

// @ADD YOUR CODE HERE
var body = d3.select('body');
var select = body.append('select').attr('id', 'selDataset');
Object.entries(data).forEach(([key]) => {
  select.append('option').attr('value', key).text(key);
});

d3.selectAll('#selDataset').on('change', updatePlotly);

function updatePlotly() {
  var dropdownMenu = d3.select('#selDataset');
  var dataset = dropdownMenu.property('value');
  console.log(datasets[dataset]);

  Plotly.restyle('pie', 'values', [window[dataset]]);
}

data = [{ type: 'pie', values: us }];
var layout = {
  height: 600,
  width: 800,
};
Plotly.newPlot('pie', data, layout);
