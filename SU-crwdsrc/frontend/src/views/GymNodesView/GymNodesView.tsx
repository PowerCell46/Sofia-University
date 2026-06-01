import { API_ENDPOINTS } from "../../api/constants";
import CoordinateFormView from "../../components/CoordinateFormView/CoordinateFormView";
import ViewLayout from "../../components/ViewLayout/ViewLayout";
import { GYM_NODES_ACCENT } from "../accents";
import type { FooterConfig } from "../types";


const FOOTER: FooterConfig = {
    label: "GymNodes",
    suffix: "Node Mapper",
};

function GymNodesView() {
    return (
        <ViewLayout accent={GYM_NODES_ACCENT} footer={FOOTER}>
            <CoordinateFormView
                logoText="GymNodes"
                subtitle="Gym Node Coordinate Logger"
                endpoint={API_ENDPOINTS.GYM_NODES}
            />
        </ViewLayout>
    );
}

export default GymNodesView;
