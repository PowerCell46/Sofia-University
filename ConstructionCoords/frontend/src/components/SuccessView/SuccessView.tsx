import "./SuccessView.css";


interface SuccessViewProps {
    latitude: number;
    longitude: number;
    onBack: () => void;
}

function SuccessView({ latitude, longitude, onBack }: SuccessViewProps) {
    return (
        <div className="success-view" aria-live="polite">
            <div className="check-circle">
                <svg
                    className="check-svg"
                    width="32"
                    height="32"
                    viewBox="0 0 32 32"
                    fill="none"
                >
                    <path
                        className="check-path"
                        d="M9 17l5 5 9-11"
                        stroke="var(--bg-primary)"
                        strokeWidth="3"
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        strokeDasharray="30"
                        strokeDashoffset="30"
                    />
                </svg>
            </div>

            <h2 className="success-title">Coordinate Submitted</h2>

            <div className="coord-display">
                <div className="coord-group">
                    <span className="coord-label">LAT</span>
                    <span className="coord-value">{latitude.toFixed(4)}</span>
                </div>
                <div className="coord-divider" />
                <div className="coord-group">
                    <span className="coord-label">LON</span>
                    <span className="coord-value">{longitude.toFixed(4)}</span>
                </div>
            </div>

            <button className="back-button" onClick={onBack} type="button">
                Submit Another
            </button>
        </div>
    );
}

export default SuccessView;
