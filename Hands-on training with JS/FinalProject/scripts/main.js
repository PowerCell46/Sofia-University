import { updateHeaderStatus } from "./headerStatus.js";
import "./zoom.js";
import "./basemap.js";


// ---- Search city functionality ----

const arcgisMapElement = document.querySelector("arcgis-map");
const goToButtons = document.querySelectorAll(".go-to-bttn");
goToButtons
    .forEach(goToButtonElement => {
        const toLocationName = goToButtonElement.getAttribute("to");
        goToButtonElement.addEventListener("click", () => handleGoTo(toLocationName));
    });


function handleGoTo(locationName) {
    let mapZoomLevel = "14";
    let selectedLocationCoordinates = "";

    switch (locationName) {
        case "sofia": {
            selectedLocationCoordinates = "23.318681731456497,42.68468598841034";
            updateHeaderStatus(`Moved to ${locationName}.`);
            break;
        }
        case "plovdiv": {
            selectedLocationCoordinates = "24.74588682891758,42.135134467613184";
            updateHeaderStatus(`Moved to ${locationName}.`);
            break;
        }
        case "varna": {
            selectedLocationCoordinates = "27.91001711521919,43.21708328465066";
            updateHeaderStatus(`Moved to ${locationName}.`);
            break;
        }
        case "burgas": {
            selectedLocationCoordinates = "27.46698428248819,42.50250089837629";
            updateHeaderStatus(`Moved to ${locationName}.`);
            break;
        }
        case "ruse": {
            selectedLocationCoordinates = "25.953673800453025,43.83872509175729";
            updateHeaderStatus(`Moved to ${locationName}.`);
            break;
        }
        case "default": {
            selectedLocationCoordinates = "26.159806082947494,42.841653763545565";
            updateHeaderStatus("Resetting the map view.");
            mapZoomLevel = "8";
            break;
        }
        default: {
            updateHeaderStatus("City not found.");
            break;
        }
    }

    if (selectedLocationCoordinates !== "") {
        arcgisMapElement.setAttribute("center", selectedLocationCoordinates);
        arcgisMapElement.setAttribute("zoom", mapZoomLevel);
    }
}

// ---- Search city functionality ----

const searchCityForm = document.getElementById("search-city-form");
searchCityForm.addEventListener("submit", (event) => handleSearchCityFormSubmit(event));


function handleSearchCityFormSubmit(event) {
    event.preventDefault();

    const cityNames = new Set(["sofia", "plovdiv", "varna", "burgas", "ruse"]);
    const enteredCityNameByUser = event.target.city.value.trim().toLowerCase();

    if (cityNames.has(enteredCityNameByUser)) {
        handleGoTo(enteredCityNameByUser);

    } else {
        updateHeaderStatus("City not found.");
    }
}
