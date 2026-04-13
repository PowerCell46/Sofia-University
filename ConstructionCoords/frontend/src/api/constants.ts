export const BASE_URL = import.meta.env.VITE_API_BASE_URL;


export const API_ENDPOINTS = {
    CONSTRUCTION_LOCATION: `${BASE_URL}/api/construction-location`,
} as const;
