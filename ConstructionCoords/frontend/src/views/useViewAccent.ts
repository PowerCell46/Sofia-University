import { useEffect } from "react";

import type { ViewAccent } from "./types";


const ACCENT_VARIABLE_MAP: Record<keyof ViewAccent, string[]> = {
    accent: ["--accent"],
    accentDark: ["--accent-dark"],
    accentHover: ["--accent-hover"],
    accentGlow: ["--accent-glow", "--accent-glow-strong"],
    accentGlowFaint: ["--accent-glow-faint", "--toggle-bg"],
};


export function useViewAccent(accent: ViewAccent): void {
    useEffect(() => {
        const rootStyle = document.documentElement.style;

        const appliedVariables = Object.entries(ACCENT_VARIABLE_MAP)
            .flatMap(([accentKey, cssVariables]) => {
                const accentValue = accent[accentKey as keyof ViewAccent];

                cssVariables.forEach((cssVariable) => {
                    rootStyle.setProperty(cssVariable, accentValue);
                });

                return cssVariables;
            });

        return () => {
            appliedVariables.forEach((cssVariable) => {
                rootStyle.removeProperty(cssVariable);
            });
        };
    }, [accent]);
}
