d3.csv('hours-of-tv-watched.csv')
  .then((tvData) => {
    // Cast the hours value to a number for each piece of tvData
    tvData.forEach(function (d) {
      d.hours = +d.hours;
    });

    barChart('bar', tvData);
  })
  .catch((error) => console.log(error));
