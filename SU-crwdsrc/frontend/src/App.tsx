import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";

import { ROUTES } from "./api/routes";
import HomePage from "./views/HomePage/HomePage";
import { VIEWS } from "./views/registry";


function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path={ROUTES.HOME} element={<HomePage />} />

                {VIEWS.map((view) => (
                    <Route key={view.id} path={view.path} element={view.element} />
                ))}

                <Route path="*" element={<Navigate to={ROUTES.HOME} replace />} />
            </Routes>
        </BrowserRouter>
    );
}

export default App;
