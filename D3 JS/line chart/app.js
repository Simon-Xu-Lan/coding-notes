d3.csv('NCHS_life_expectancy_at_birth.csv')
  .then((lifeData) => {
    // cast the data from the csv as numbers
    lifeData.forEach(function (data) {
      data.year = +data.year;
      data.lifeExpectancy = +data.lifeExpectancy;
    });

    // Create line chart
    lineChart('svg-area', lifeData);
  })
  .catch((error) => console.log(error));
