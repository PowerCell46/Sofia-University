import type { FooterConfig } from "../../views/types";
import "./Footer.css";


function Footer({ label, suffix, link }: FooterConfig) {
    return (
        <footer className="footer">
            {label} &mdash;{" "}
            {link ? (
                <a
                    className="footer__link"
                    href={link.href}
                    target="_blank"
                    rel="noopener noreferrer"
                >
                    {link.label}
                </a>
            ) : (
                suffix
            )}
        </footer>
    );
}

export default Footer;
