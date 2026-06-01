import { ROUTES } from "../api/routes";
import { CONSTRUCTION_ACCENT, GEO_AI_ACCENT, GYM_NODES_ACCENT } from "./accents";
import ConstructionCoordsView from "./ConstructionCoordsView/ConstructionCoordsView";
import GeoAiView from "./GeoAiView/GeoAiView";
import GymNodesView from "./GymNodesView/GymNodesView";
import type { ViewDefinition } from "./types";


export const VIEWS: ViewDefinition[] = [
    {
        id: "construction-coords",
        path: ROUTES.CONSTRUCTION_COORDS,
        accent: CONSTRUCTION_ACCENT,
        card: {
            title: "Construction Coords",
            description: "Log construction site coordinates in the field.",
        },
        element: <ConstructionCoordsView />,
    },
    {
        id: "geo-ai",
        path: ROUTES.GEO_AI,
        accent: GEO_AI_ACCENT,
        card: {
            title: "GeoAI",
            description: "Submit geospatial points of interest for analysis.",
        },
        element: <GeoAiView />,
    },
    {
        id: "gym-nodes",
        path: ROUTES.GYM_NODES,
        accent: GYM_NODES_ACCENT,
        card: {
            title: "Gym Nodes",
            description: "Log gym network node coordinates in the field.",
        },
        element: <GymNodesView />,
    },
];
