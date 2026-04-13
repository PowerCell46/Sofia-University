import { useState, useCallback } from "react";

import { API_ENDPOINTS } from "./api/constants";
import CautionStripe from "./components/CautionStripe/CautionStripe";
import CoordinateForm from "./components/CoordinateForm/CoordinateForm";
import SuccessView from "./components/SuccessView/SuccessView";
import Footer from "./components/Footer/Footer";
import ThemeToggle from "./components/ThemeToggle/ThemeToggle";
import "./App.css";


type ViewState = "form" | "success";

interface SubmittedCoords {
    latitude: number;
    longitude: number;
}

function App() {
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
        const response = await fetch(API_ENDPOINTS.CONSTRUCTION_LOCATION, {
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
    }, [transitionTo]);

    const handleBack = useCallback(() => {
        transitionTo("form");
    }, [transitionTo]);

    return (
        <>
            <CautionStripe />
            <ThemeToggle />

            <main className="app-main">
                <div className={`view-container${hidden ? " view-hidden" : ""}`}>
                    {view === "form" ? (
                        <CoordinateForm
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
            </main>

            <Footer />
        </>
    );
}

export default App;
