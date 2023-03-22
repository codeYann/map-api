import React from "react";
import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";

export type Geolocation = {
  latitude: number;
  longitude: number;
};

type MapProps = {
  locations: Geolocation[];
};

const Map: React.FC<MapProps> = ({ locations = [] }) => {
  const center = [-3.7319, -38.5267];
  console.log("This");
  return (
    <MapContainer center={center} zoom={13} style={{ height: "500px" }}>
      <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
      {locations.map(({ latitude, longitude }, index) =>
        latitude && longitude ? (
          <Marker
            key={`${latitude}-${longitude}`}
            position={[latitude, longitude]}
          >
            <Popup>{`Location ${index + 1}`}</Popup>
          </Marker>
        ) : (
          console.log("VIsh")
        )
      )}
    </MapContainer>
  );
};

export default Map;
