import React, { useEffect, useState } from "react";
import Map, { Geolocation } from "./components/map";
import { baseApi } from "./api";

function App() {
  const [geolocations, setGeolocations] = useState<Geolocation[]>([]);

  useEffect(() => {
    (async () => {
      try {
        const response = await baseApi.get("/geolocation");

        const parseLocationsToFloat = response.data.map((content: any) => ({
          latitude: parseFloat(content.LATITUDE),
          longitude: parseFloat(content.LONGITUDE),
        }));
        setGeolocations(parseLocationsToFloat);
      } catch (e) {
        console.log(e);
      }
    })();
  }, []);

  console.log("that");
  return (
    <div className="App">
      <Map locations={geolocations} />
    </div>
  );
}

export default App;
