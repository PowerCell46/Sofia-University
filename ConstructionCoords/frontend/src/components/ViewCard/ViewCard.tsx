import type { CSSProperties } from "react";
import { Link } from "react-router-dom";

import type { ViewDefinition } from "../../views/types";
import "./ViewCard.css";


interface ViewCardProps {
    view: ViewDefinition;
}

function ViewCard({ view }: ViewCardProps) {
    const cardStyle = {
        "--card-accent": view.accent.accent,
        "--card-accent-glow": view.accent.accentGlow,
        ...(view.card.image ? { "--card-image": `url(${view.card.image})` } : {}),
    } as CSSProperties;

    return (
        <Link
            className={`view-card${view.card.image ? " view-card--image" : ""}`}
            to={view.path}
            style={cardStyle}
        >
            <div className="view-card__overlay" />

            <div className="view-card__content">
                <h2 className="view-card__title">{view.card.title}</h2>
                <p className="view-card__description">{view.card.description}</p>
            </div>

            <span className="view-card__arrow" aria-hidden="true">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                    <line x1="5" y1="12" x2="19" y2="12" />
                    <polyline points="12 5 19 12 12 19" />
                </svg>
            </span>
        </Link>
    );
}

export default ViewCard;
