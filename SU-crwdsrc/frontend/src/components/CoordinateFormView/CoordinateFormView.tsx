import { useState, useCallback } from "react";

import CoordinateForm from "../CoordinateForm/CoordinateForm";
import SuccessView from "../SuccessView/SuccessView";
import "./CoordinateFormView.css";


type ViewState = "form" | "success";

interface SubmittedCoords {
    latitude: number;
    longitude: number;
}

interface CoordinateFormViewProps {
    logoText: string;
    subtitle: string;
    endpoint: string;
}

function CoordinateFormView({ logoText, subtitle, endpoint }: CoordinateFormViewProps) {
    const [view, setView] = useState<ViewState>("form");
    const [hidden, setHidden] = useState(false);
    const [coords, setCoords] = useState<SubmittedCoords | null>(null);
    const [shouldAutoFocus, setShouldAutoFocus] = useState(true);

    const transitionTo = useCallback((nextView: ViewState) => {
        setHidden(true);

        setTimeout(() => {
            setView(nextView);

            requestAnimationFrame(() => {
                requestAnimationFrame(() => {
                    setHidden(false);
                    if (nextView === "form") {
                        setShouldAutoFocus(true);
                    }
                });
            });
        }, 300);
    }, []);

    const handleSubmit = useCallback(async (lat: number, lon: number) => {
        const response = await fetch(endpoint, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ latitude: lat, longitude: lon }),
        });

        if (!response.ok) {
            throw new Error(`Server error: ${response.status}`);
        }

        setCoords({ latitude: lat, longitude: lon });
        setShouldAutoFocus(false);
        transitionTo("success");
    }, [endpoint, transitionTo]);

    const handleBack = useCallback(() => {
        transitionTo("form");
    }, [transitionTo]);

    return (
        <div className={`view-container${hidden ? " view-hidden" : ""}`}>
            {view === "form" ? (
                <CoordinateForm
                    logoText={logoText}
                    subtitle={subtitle}
                    onSubmit={handleSubmit}
                    autoFocus={shouldAutoFocus}
                />
            ) : (
                coords && (
                    <SuccessView
                        latitude={coords.latitude}
                        longitude={coords.longitude}
                        onBack={handleBack}
                    />
                )
            )}
        </div>
    );
}

export default CoordinateFormView;
