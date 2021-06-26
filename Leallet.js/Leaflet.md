# Map Object

- `L.map` accepts two arguments:

  1. The `id` of the HTML element which Leaflet should insert the map into.

  2. An object containing initial options for the new map ("center" and "zoom" in this example).

# Title layer

- The tile layer serves as a background image for the map.
- Leaflet doesn't provide us with a tile layer out of the box.
- Instead, it gives us the option to use various tile layer APIs.
- Mapbox API
  - We configure our tile layer by passing in a formatted queryURL to the tileLayer method,
  - and then adding our layer to our map with the `addTo` method.
  - Mapbox is a free API, but you'll need to create a free account at <https://mapbox.com> and [generate a token](https://www.mapbox.com/studio/account/tokens/) in order to use it.

# addTO method

- We will invoke the `addTo` method whenever we want to add something to a map!

```js
// Creating our initial map object
// We set the longitude, latitude, and the starting zoom level
// This gets inserted into the div with an id of 'map'
var myMap = L.map('map', {
  center: [38.9072, -77.0369],
  zoom: 13,
});

// Adding a tile layer (the background map image) to our map
// We use the addTo method to add objects to our map
L.tileLayer(
  'https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}',
  {
    attribution:
      "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
    tileSize: 512,
    maxZoom: 18,
    zoomOffset: -1,
    id: 'mapbox/streets-v11',
    accessToken: API_KEY,
  }
).addTo(myMap);
```

# Marker

- L.marker method
- create a new marker using the `L.marker` method. To do this, we pass two arguments into `L.marker`:
  1. An array containing coordinates for where the marker should be placed.
  2. An object containing initial options for the marker. (`draggable` and `title` in this example).
- The `L.marker` method returns a new marker object, which we can run the `addTo` method on, and pass it a reference to our map.

```js
// Create a new marker
// Pass in some initial options, and then add it to the map using the addTo method
var marker = L.marker([38.9072, -77.0369], {
  draggable: true,
  title: 'My First Marker',
}).addTo(myMap);
```

# popup

- Add a popup to marker
- add a popup to the new marker using the `bindPopup` method
- pass in text we want to appear when the marker is clicked.

```js
// Binding a pop-up to our marker
marker.bindPopup('Hello There!');
```

- Pop-ups take in a string of HTML.

```js
 L.marker(city.location)
    .bindPopup("<h1>" + city.name + "</h1> <hr> <h3>Population " + city.population + "</h3>")
    .addTo(myMap);
}

```

# Marker - other kind

## circle

- `L.circle` method
- pass in two arguments into `L.circle`:
  1. The coordinates for where to place the circle layer.
  2. Some initial options for the circle vector layer. In this example, the following are being used:
     1. `color`
     2. `fillColor`
     3. `fillOpacity`
     4. `radius`

```js
// Create a circle and pass in some initial options
L.circle([45.52, -122.69], {
  color: 'green',
  fillColor: 'green',
  fillOpacity: 0.75,
  radius: 500,
}).addTo(myMap);
```

## Polygon

- `L.polygon` method

```js
// Create a Polygon and pass in some initial options
L.polygon(
  [
    [45.54, -122.68],
    [45.55, -122.68],
    [45.55, -122.66],
  ],
  {
    color: 'yellow',
    fillColor: 'yellow',
    fillOpacity: 0.3,
  }
).addTo(myMap);
```

## Line

- `L.line` method

```js
// Coordinates for each point to be used in the polyline
var line = [
  [45.51, -122.68],
  [45.5, -122.6],
  [45.48, -122.7],
  [45.54, -122.75],
];

// Create a polyline using the line coordinates and pass in some initial options
L.polyline(line, {
  color: 'red',
}).addTo(myMap);
```

## Rectangle

- `L.rectangle` method

```js
// Create a rectangle and pass in some initial options
L.rectangle(
  [
    [45.55, -122.64],
    [45.54, -122.61],
  ],
  {
    color: 'black',
    weight: 3,
    stroke: true, // False is with out edge
  }
).addTo(myMap);
```

# Vector Layers

- http://leafletjs.com/reference-1.0.3.html#toc

# Leaflet docs for Path Options

## Funciton for marker

- Notice how we've defined a `markerSize` function, which takes in a `population` argument and returns the `population` divided by 40.
- This function will be used to determine the radius, in pixels, of the circle layer for each city.
- We're dividing by 40 because the circles would be too large if we set their radius equal to the population without scaling down.
- Notice that when we create each circle, we set its radius with the `markerSize` function.
- We repeat this process for each city's marker.

```js
// Loop through the cities array and create one marker for each city object
for (var i = 0; i < cities.length; i++) {
  L.circle(cities[i].location, {
    fillOpacity: 0.75,
    color: 'white',
    fillColor: 'purple',
    // Setting our circle's radius equal to the output of our markerSize function
    // This will make our marker's size proportionate to its population
    radius: markerSize(cities[i].population),
  })
    .bindPopup(
      '<h1>' +
        cities[i].name +
        '</h1> <hr> <h3>Population: ' +
        cities[i].population +
        '</h3>'
    )
    .addTo(myMap);
}
```

# overlay, base layer, layer control

- `L.LayerGoup`, `L.control`, `baseMap`, `overlayMaps`
- Leaflet Layers Control Docs](http://leafletjs.com/examples/layers-control/)
- the `layer control` in the top right corder of the screen, you can `toggle the markers on or off`. Notice how we can also `switch between light and dark maps`.
- we create two tile layers:

  1.  A light map. This is the same, day-time map we've been using so far.

  2.  A dark map. This is a dark, night-time version of the map we've been using so far.

- We then create two objects: `baseMaps` and `overlayMaps`.

  1.  `baseMaps` contains layers that can be shown only one a time.

  - In this case, we can either show light maps or dark maps, but never both at the same time.
  - One base layer must always be visible.

  2.  `overlayMaps` contains layers that can appear simultaneously with other layers of the same type and can be toggled off completely.

  - Generally this refers to markers. Note how we can toggle cities on and off.

```js
// An array of cities and their locations
var cities = [
  {
    name: 'Paris',
    location: [48.8566, 2.3522],
  },
  {
    name: 'Lyon',
    location: [45.764, 4.8357],
  },
  {
    name: 'Cannes',
    location: [43.5528, 7.0174],
  },
  {
    name: 'Nantes',
    location: [47.2184, -1.5536],
  },
];

// An array which will be used to store created cityMarkers
var cityMarkers = [];

for (var i = 0; i < cities.length; i++) {
  // loop through the cities array, create a new marker, push it to the cityMarkers array
  cityMarkers.push(
    L.marker(cities[i].location).bindPopup('<h1>' + cities[i].name + '</h1>')
  );
}

// Add all the cityMarkers to a new layer group.
// Now we can handle them as one group instead of referencing each individually
var cityLayer = L.layerGroup(cityMarkers);

// Define variables for our tile layers
var light = L.tileLayer(
  'https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}',
  {
    attribution:
      'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'light-v10',
    accessToken: API_KEY,
  }
);

var dark = L.tileLayer(
  'https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}',
  {
    attribution:
      'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'dark-v10',
    accessToken: API_KEY,
  }
);

// Only one base layer can be shown at a time
var baseMaps = {
  Light: light,
  Dark: dark,
};

// Overlays that may be toggled on or off
var overlayMaps = {
  Cities: cityLayer,
};

// Create map object and set default layers
var myMap = L.map('map', {
  center: [46.2276, 2.2137],
  zoom: 6,
  layers: [light, cityLayer],
});

// Pass our map layers into our layer control
// Add the layer control to the map
L.control.layers(baseMaps, overlayMaps).addTo(myMap);
```

# GeoJSON

- [Leaflet's Docs for GeoJSON](http://leafletjs.com/examples/geojson/)
- See Leaflet Documentation on GeoJSON:
  - <http://leafletjs.com/reference.html#geojson>
  - <http://leafletjs.com/examp\les/geojson/>
- `L.geoJSON`
- geoJSON is a data format
- Features in GeoJSON contain a Geometry object and additional properties, and a FeatureCollection contains a list of Features

- a simple GeoJSON feature

```js
var geojsonFeature = {
  type: 'Feature',
  properties: {
    name: 'Coors Field',
    amenity: 'Baseball Stadium',
    popupContent: 'This is where the Rockies play!',
  },
  geometry: {
    type: 'Point',
    coordinates: [-104.99404, 39.75621],
  },
};
```

## GeoJSON layer

- GeoJSON objects are added to the map through a `GeoJSON layer`.
  To create it and add it to a map, we can use the following code:

```js
L.geoJSON(geojsonFeature).addTo(map);
```

- Alternatively, we could create an empty GeoJSON layer and assign it to a variable so that we can add more features to it later.

```js
var myLayer = L.geoJSON().addTo(map);
myLayer.addData(geojsonFeature);
```
