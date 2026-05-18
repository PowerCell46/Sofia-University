import { updateHeaderStatus } from "./headerStatus.js";


const arcgisMapElement = document.querySelector("arcgis-map");
const zoomButtons = document.querySelectorAll(".zoom-btn");

const zoomOutButton = zoomButtons.item(0);
zoomOutButton.addEventListener("click", () => handleZoomLevelChange("out"));

const zoomInButton = zoomButtons.item(1);
zoomInButton.addEventListener("click", () => handleZoomLevelChange("in"));


function handleZoomLevelChange(zoomDirection) {
    const currentZoomLevel = Number(arcgisMapElement.getAttribute("zoom"));

    if (zoomDirection === "in") {
        updateHeaderStatus("Zoomed in.");
        arcgisMapElement.setAttribute("zoom", currentZoomLevel + 1);

    } else if (zoomDirection === "out") {
        updateHeaderStatus("Zoomed out.");
        arcgisMapElement.setAttribute("zoom", currentZoomLevel - 1);

    } else {
        updateHeaderStatus("Invalid zoom command!");
    }
}
