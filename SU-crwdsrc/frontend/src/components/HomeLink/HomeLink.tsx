import { Link } from "react-router-dom";

import { ROUTES } from "../../api/routes";
import "./HomeLink.css";


function HomeLink() {
    return (
        <Link
            className="home-link"
            to={ROUTES.HOME}
            aria-label="Back to home"
            title="Back to home"
        >
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                <path d="M3 12l9-9 9 9" />
                <path d="M5 10v10a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V10" />
            </svg>
        </Link>
    );
}

export default HomeLink;
