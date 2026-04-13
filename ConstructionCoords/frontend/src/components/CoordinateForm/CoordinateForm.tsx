import { useState, useRef, useEffect } from "react";
import "./CoordinateForm.css";


interface CoordinateFormProps {
    onSuccess: (lat: number, lon: number) => void;
    autoFocus?: boolean;
}

const COORDINATE_FORMAT_PATTERN = /^\(\s*(-?\d+(?:\.\d+)?)\s*,\s*(-?\d+(?:\.\d+)?)\s*\)$/;

type ParseResult =
    | { ok: true; lat: number; lon: number }
    | { ok: false; error: string };

function validateLatitude(value: number): string | null {
    if (!(value >= -90 && value <= 90)) {
        return "Latitude must be between -90 and 90 degrees.";
    }
    return null;
}

function validateLongitude(value: number): string | null {
    if (!(value >= -180 && value <= 180)) {
        return "Longitude must be between -180 and 180 degrees.";
    }
    return null;
}

function parseCoordinates(input: string): ParseResult {
    const match = input.trim().match(COORDINATE_FORMAT_PATTERN);
    if (!match) {
        return {
            ok: false,
            error: "Invalid input. Use format (latitude, longitude).",
        };
    }

    const lat = parseFloat(match[1]);
    const lon = parseFloat(match[2]);

    if (isNaN(lat) || isNaN(lon)) {
        return {
            ok: false,
            error: "Invalid input. Use format (latitude, longitude).",
        };
    }

    const latError = validateLatitude(lat);
    if (latError) {
        return { ok: false, error: latError };
    }

    const lonError = validateLongitude(lon);
    if (lonError) {
        return { ok: false, error: lonError };
    }

    return { ok: true, lat, lon };
}

function CoordinateForm({ onSuccess, autoFocus }: CoordinateFormProps) {
    const [value, setValue] = useState("");
    const [error, setError] = useState("");
    const [shaking, setShaking] = useState(false);
    const inputRef = useRef<HTMLInputElement>(null);

    useEffect(() => {
        if (autoFocus && inputRef.current) {
            inputRef.current.focus();
        }
    }, [autoFocus]);

    const handleSubmit = () => {
        const result = parseCoordinates(value);
        if (!result.ok) {
            setError(result.error);
            setShaking(true);
            setTimeout(() => setShaking(false), 450);
            return;
        }
        setError("");
        onSuccess(result.lat, result.lon);
    };

    const handleKeyDown = (e: React.KeyboardEvent) => {
        if (e.key === "Enter") {
            handleSubmit();
        }
    };

    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setValue(e.target.value);
        if (error) {
            setError("");
        }
    };

    return (
        <div className="coordinate-form">
            <div className="form-logo load-slide-down">
                <span className="logo-bracket">[</span>
                <span className="logo-text">CC</span>
                <span className="logo-bracket">]</span>
            </div>
            <p className="form-subtitle load-slide-down-delay">
                Construction Coordinate Logger
            </p>

            <div className="load-slide-up">
                <div className={`input-wrapper${shaking ? " shake" : ""}`}>
                    <input
                        ref={inputRef}
                        type="text"
                        className={`coord-input${error ? " input-error" : ""}`}
                        placeholder="(40.7128, -74.0060)"
                        value={value}
                        onChange={handleChange}
                        onKeyDown={handleKeyDown}
                        aria-label="Coordinate input"
                        autoFocus={autoFocus}
                    />
                    {error && (
                        <p className="error-message" role="alert">
                            {error}
                        </p>
                    )}
                </div>
            </div>

            <button
                className="submit-button load-slide-up-delay"
                onClick={handleSubmit}
                type="button"
            >
                Submit Coordinates
            </button>
        </div>
    );
}

export default CoordinateForm;
