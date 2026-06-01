import { API_ENDPOINTS, SUBMITTED_POIS_URL } from "../../api/constants";
import CoordinateFormView from "../../components/CoordinateFormView/CoordinateFormView";
import ViewLayout from "../../components/ViewLayout/ViewLayout";
import { GEO_AI_ACCENT } from "../accents";
import type { FooterConfig } from "../types";


const FOOTER: FooterConfig = {
    label: "GeoAI",
    link: {
        href: SUBMITTED_POIS_URL,
        label: "Submitted POIs",
    },
};

function GeoAiView() {
    return (
        <ViewLayout accent={GEO_AI_ACCENT} footer={FOOTER}>
            <CoordinateFormView
                logoText="GeoAI"
                subtitle="Geospatial Coordinate Logger"
                endpoint={API_ENDPOINTS.GEO_AI_LOCATION}
            />
        </ViewLayout>
    );
}

export default GeoAiView;
