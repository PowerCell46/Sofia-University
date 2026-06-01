export const BASE_URL = import.meta.env.VITE_API_BASE_URL || "";


export const SUBMITTED_POIS_URL = "https://arcg.is/1WTWvi2";


export const API_ENDPOINTS = {
    CONSTRUCTION_LOCATION: `${BASE_URL}/api/construction-location`,
    // TODO: point GeoAI to its dedicated backend route once it exists.
    GEO_AI_LOCATION: `${BASE_URL}/api/construction-location`,
    // TODO: gym-nodes backend route is not implemented yet.
    GYM_NODES: `${BASE_URL}/api/gym-nodes`,
} as const;
