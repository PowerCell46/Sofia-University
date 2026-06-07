/**
 * Formats a coordinate with its hemisphere suffix,
 * e.g. `formatCoord(42.6977, 'N', 'S')` → `"42.6977° N"`
 */
export const formatCoord = (value: number, positive: string, negative: string): string =>
    `${Math.abs(value).toFixed(4)}° ${value >= 0 ? positive : negative}`;
