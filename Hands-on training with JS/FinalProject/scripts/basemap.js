import { updateHeaderStatus } from "./headerStatus.js";


const arcgisMapElement = document.querySelector("arcgis-map");

const selectBasemapElement = document.querySelector("#select-basemap");
selectBasemapElement.addEventListener("change", (event) => handleBasemapChange(event));


function handleBasemapChange(event) {
    if (arcgisMapElement.getAttribute("basemap") != event.target.value) {
        updateHeaderStatus("Basemap changed.");
        arcgisMapElement.setAttribute("basemap", event.target.value);
    }
}
