import { BACKEND_URL } from '../config/consts';

import type { LatLon } from '@windy/interfaces';


/**
 * Submits a picked point to the GeoAI backend.
 * Throws on network failure or a non-2xx response.
 */
export const submitPoint = async ({ lat, lon }: LatLon): Promise<void> => {
    const response = await fetch(BACKEND_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            latitude: lat,
            longitude: lon,
        }),
    });

    if (!response.ok) {
        throw new Error(`Server responded with ${response.status}`);
    }
};
