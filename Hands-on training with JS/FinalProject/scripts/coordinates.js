import { updateHeaderStatus } from "./headerStatus.js";


const arcgisMapElement = document.querySelector("arcgis-map");

arcgisMapElement.addEventListener("arcgisViewReadyChange", (event) => {
    if (event.target.ready) {
        event.target.view.on("click", (event) => {
            const selectedPointLat = event.mapPoint.latitude.toFixed(3);
            const selectedPointLon = event.mapPoint.longitude.toFixed(3);

            updateHeaderStatus(`{ Lat: ${selectedPointLat}, Lon: ${selectedPointLon} }`);
        });
    }
});
