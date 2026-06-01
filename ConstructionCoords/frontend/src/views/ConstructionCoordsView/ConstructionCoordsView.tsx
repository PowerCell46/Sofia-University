import { API_ENDPOINTS } from "../../api/constants";
import CoordinateFormView from "../../components/CoordinateFormView/CoordinateFormView";
import ViewLayout from "../../components/ViewLayout/ViewLayout";
import { CONSTRUCTION_ACCENT } from "../accents";
import type { FooterConfig } from "../types";


const FOOTER: FooterConfig = {
    label: "ConstructionCoords",
    suffix: "Field Tool",
};

function ConstructionCoordsView() {
    return (
        <ViewLayout accent={CONSTRUCTION_ACCENT} footer={FOOTER}>
            <CoordinateFormView
                logoText="CC"
                subtitle="Construction Coordinate Logger"
                endpoint={API_ENDPOINTS.CONSTRUCTION_LOCATION}
            />
        </ViewLayout>
    );
}

export default ConstructionCoordsView;
