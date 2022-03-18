var apiKey = 'fa9a2T6WDwbdKHqG1apo';

/* global Plotly */
var url = `https://www.quandl.com/api/v3/datasets/WIKI/AMZN.json?start_date=2016-10-01&end_date=2017-10-01&api_key=${apiKey}`;

d3.json(url).then((data) => console.log(data));
/**
 * Helper function to select stock data
 * Returns an array of values
 * @param {array} rows
 * @param {integer} index
 * index 0 - Date
 * index 1 - Open
 * index 2 - High
 * index 3 - Low
 * index 4 - Close
 * index 5 - Volume
 */
function unpack(rows, index) {
  return rows.map(function (row) {
    return row[index];
  });
}

/**
 * Fetch data and build the timeseries plot
 */
function buildPlot() {
  // @TODO: YOUR CODE HERE
  d3.json(url).then((data) => {
    var name = data.dataset.name;
    var stock = data.dataset.dataset_code;
    var startDate = data.dataset.start_date;
    var endDate = data.dataset.end_date;
    var dates = unpack(data.dataset.data, 0);
    var closingPrices = unpack(data.dataset.data, 4);

    var trace1 = {
      type: 'scatter',
      mode: 'lines',
      name: name,
      x: dates,
      y: closingPrices,
      line: {
        color: '#17BECF',
      },
    };

    var data = [trace1];

    var layout = {
      title: `${stock} closing price`,
      xaxis: {
        range: [startDate, endDate],
        type: 'date',
      },
      yaxis: {
        autorange: true,
        type: 'linear',
      },
    };

    Plotly.newPlot('plot', data, layout);
  });
}

buildPlot();
