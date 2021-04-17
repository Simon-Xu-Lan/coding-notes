# Map Object:

     `L.map` accepts two arguments:

     1. The `id` of the HTML element which Leaflet should insert the map into.

     2. An object containing initial options for the new map ("center" and "zoom" in this example).

# Tile Layer:

- The tile layer serves as a background image for the map.
- Leaflet doesn't provide us with a tile layer out of the box.
- Instead, it gives us the option to use various tile layer APIs.
- Here we're using the Mapbox API. We configure our tile layer by passing in a formatted queryURL to the tileLayer method,
- and then adding our layer to our map with the `addTo` method. We will invoke the `addTo` method whenever we want to add something to a map!

# Mapbox

Mapbox is a free API, but you'll need to create a free account at <https://mapbox.com> and [generate a token](https://www.mapbox.com/studio/account/tokens/) in order to use it.

# Marker

1. Notice how we can create a new marker using the `L.marker` method. To do this, we pass two arguments into `L.marker`:

   1. An array containing coordinates for where the marker should be placed.

   2. An object containing initial options for the marker. (`draggable` and `title` in this example).

2. The `L.marker` method returns a new marker object, which we can run the `addTo` method on, and pass it a reference to our map.

3. Then, we add a popup to the new marker using the `bindPopup` method and pass in text we want to appear when the marker is clicked.
