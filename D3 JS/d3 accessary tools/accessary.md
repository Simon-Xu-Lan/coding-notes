# Configure a parseTime function which will return a new Date object from a string

```js
var parseTime = d3.timeParse('%B');
```

# Configure a time scale

- d3.extent returns the an array containing the min and max values for the property specified

```js
var xTimeScale = d3
  .scaleTime()
  .domain(d3.extent(forceData, (data) => data.date))
  .range([0, chartWidth]);
```

# Format the data and convert to numerical and date values

- Create a function to parse date and time

```js
var parseTime = d3.timeParse('%d-%b');
```


The pageX read-only property of the MouseEvent interface returns the X (horizontal) coordinate (in pixels) at which the mouse was clicked, relative to the left edge of the entire document.