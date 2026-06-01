import type { ReactNode } from "react";

import type { FooterConfig, ViewAccent } from "../../views/types";
import { useViewAccent } from "../../views/useViewAccent";
import CautionStripe from "../CautionStripe/CautionStripe";
import HomeLink from "../HomeLink/HomeLink";
import ThemeToggle from "../ThemeToggle/ThemeToggle";
import Footer from "../Footer/Footer";
import "./ViewLayout.css";


interface ViewLayoutProps {
    accent: ViewAccent;
    footer: FooterConfig;
    children: ReactNode;
}

function ViewLayout({ accent, footer, children }: ViewLayoutProps) {
    useViewAccent(accent);

    return (
        <>
            <CautionStripe />
            <HomeLink />
            <ThemeToggle />

            <main className="app-main">
                {children}
            </main>

            <Footer {...footer} />
        </>
    );
}

export default ViewLayout;
