import { SUBMITTED_POIS_URL } from "../../api/constants";
import "./Footer.css";


function Footer() {
    return (
        <footer className="footer">
            GeoAI &mdash;{" "}
            <a
                className="footer__link"
                href={SUBMITTED_POIS_URL}
                target="_blank"
                rel="noopener noreferrer"
            >
                Submitted POIs
            </a>
        </footer>
    );
}

export default Footer;
