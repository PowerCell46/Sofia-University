import CautionStripe from "../../components/CautionStripe/CautionStripe";
import ThemeToggle from "../../components/ThemeToggle/ThemeToggle";
import ViewCard from "../../components/ViewCard/ViewCard";
import { HOME_ACCENT } from "../accents";
import { useViewAccent } from "../useViewAccent";
import { VIEWS } from "../registry";
import "./HomePage.css";


function HomePage() {
    useViewAccent(HOME_ACCENT);

    return (
        <>
            <CautionStripe />
            <ThemeToggle />

            <main className="home-main">
                <header className="home-header">
                    <h1 className="home-title">
                        <span className="logo-bracket">[</span>
                        <span className="logo-text">Workspaces</span>
                        <span className="logo-bracket">]</span>
                    </h1>
                    <p className="home-subtitle">Select a tool to get started.</p>
                </header>

                <section className="home-grid">
                    {VIEWS.map((view) => (
                        <ViewCard key={view.id} view={view} />
                    ))}
                </section>
            </main>
        </>
    );
}

export default HomePage;
