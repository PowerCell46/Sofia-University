import ViewLayout from "../../components/ViewLayout/ViewLayout";
import { GYM_NODES_ACCENT } from "../accents";
import type { FooterConfig } from "../types";
import "./GymNodesView.css";


const FOOTER: FooterConfig = {
    label: "GymNodes",
    suffix: "Coming Soon",
};

function GymNodesView() {
    return (
        <ViewLayout accent={GYM_NODES_ACCENT} footer={FOOTER}>
            <div className="placeholder-view">
                <div className="placeholder-logo">
                    <span className="logo-bracket">[</span>
                    <span className="logo-text">GymNodes</span>
                    <span className="logo-bracket">]</span>
                </div>
                <p className="placeholder-message">
                    This view is under construction.
                </p>
            </div>
        </ViewLayout>
    );
}

export default GymNodesView;
