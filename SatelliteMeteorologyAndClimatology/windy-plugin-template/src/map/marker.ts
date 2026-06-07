import { map } from '@windy/map';

import type { LatLon } from '@windy/interfaces';


/** Orange map pin (SVG), anchored at its tip */
const pinIcon = new L.DivIcon({
    className: '', // prevent Leaflet's default white-box divIcon styling
    iconSize: [34, 34],
    iconAnchor: [17, 31],
    html: `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="34" height="34"
            style="filter: drop-shadow(0 2px 3px rgba(0, 0, 0, 0.45));">
            <path
                fill="#ff5722"
                stroke="#fff"
                stroke-width="1"
                d="M12 2C8.13 2 5 5.13 5 8.5c0 5.25 7 13.5 7 13.5s7-8.25 7-13.5C19 5.13 15.87 2 12 2zm0 9.5a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"
            />
        </svg>`,
});

let marker: L.Marker | null = null;

/** Places the pin at the given coordinates, replacing any previous one */
export const showPin = ({ lat, lon }: LatLon): void => {
    removePin();
    marker = new L.Marker({ lat, lng: lon }, { icon: pinIcon }).addTo(map);
};

/** Removes the pin from the map (no-op if none is shown) */
export const removePin = (): void => {
    if (marker) {
        marker.remove();
        marker = null;
    }
};
