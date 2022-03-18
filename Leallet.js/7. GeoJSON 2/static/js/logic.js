// Create the initial  map object
// This gets insert into the dive with an id of 'map'
// We set the longitude and latitude, and the starting zoom level
var myMap = L.map('map', {
  center: [40.7128, -74.006],
  zoom: 12,
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

// Use this link to get the geojson data
var link = 'static/data/nyc.geojson';

// Grabbing our GeoJSON data
d3.json(link, function (data) {
  // Creating a GeoJSON layer with the retrieve data
  L.geoJson(data).addTo(myMap);
});
