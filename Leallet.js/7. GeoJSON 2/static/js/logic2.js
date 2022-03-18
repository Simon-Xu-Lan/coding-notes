// Creating map object
var myMap = L.map('map', {
  center: [40.7128, -74.006],
  zoom: 12,
});

// Adding tile layer
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

// Get the geojson data
var link = 'static/data/nyc.geojson';

// Creat style object
var mapStyle = {
  color: 'white',
  fillColor: 'pink',
  fillOpacity: 0.5,
  weight: 1.5,
};

// Grabbing geoJSON data
// Then creating a geoJSON with the retrieve data
d3.json(link, function (data) {
  L.geoJson(data, {
    // passing in our style object
    style: mapStyle,
  }).addTo(myMap);
});
