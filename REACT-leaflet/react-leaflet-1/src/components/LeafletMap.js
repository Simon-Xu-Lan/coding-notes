import React from 'react';
import { Map, Tilelayer, Marker, Popup } from 'react-leaflet';

function LeafletMap() {
    const mapPosition = [11.1271, 78.6569];

    return (
        <Map
            className="map"
            center={[mapPosition[0], mapPosition[1]]}
            zoom={5}
        >
            <Tilelayer
        </Map>

        
    )
}