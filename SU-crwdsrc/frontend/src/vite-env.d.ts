/// <reference types="vite/client" />

interface ImportMetaEnv {
    readonly VITE_CONSTRUCTION_COORDS_URL: string;
    readonly VITE_GEO_AI_URL: string;
    readonly VITE_GYM_NODES_URL: string;
}

interface ImportMeta {
    readonly env: ImportMetaEnv;
}
