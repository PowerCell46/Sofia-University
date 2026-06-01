import type { ReactNode } from "react";


export interface ViewAccent {
    accent: string;
    accentDark: string;
    accentHover: string;
    accentGlow: string;
    accentGlowFaint: string;
}

export interface FooterConfig {
    label: string;
    suffix?: string;
    link?: {
        href: string;
        label: string;
    };
}

export interface ViewCardConfig {
    title: string;
    description: string;
    image?: string;
}

export interface ViewDefinition {
    id: string;
    path: string;
    accent: ViewAccent;
    card: ViewCardConfig;
    element: ReactNode;
}
