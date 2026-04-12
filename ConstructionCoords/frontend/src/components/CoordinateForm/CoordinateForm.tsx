import { useState, useRef, useEffect } from "react";
import "./CoordinateForm.css";


interface CoordinateFormProps {
    onSuccess: (lat: number, lon: number) => void;
    autoFocus?: boolean;
}

function parseCoordinates(input: string): { lat: number; lon: number } | null {
    const cleaned = input.replace(/[()]/g, "").trim();
    const parts = cleaned.split(/[\s,]+/).filter(Boolean);

    if (parts.length !== 2) {
        return null;
    }

    const lat = parseFloat(parts[0]);
    const lon = parseFloat(parts[1]);

    if (isNaN(lat) || isNaN(lon)) {
        return null;
    }

    if (lat < -90 || lat > 90 || lon < -180 || lon > 180) {
        return null;
    }

    return { lat, lon };
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
        if (!result) {
            setError("Invalid input. Use format (40.7128, -74.0060).");
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
                        placeholder="40.7128, -74.0060"
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
