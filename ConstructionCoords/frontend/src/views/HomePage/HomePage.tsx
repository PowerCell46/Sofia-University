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
                        <span className="logo-text">SU·crwdsrc</span>
                        <span className="logo-bracket">]</span>
                    </h1>
                    <p className="home-subtitle">Crowdsourcing GIS portal · Select a tool below.</p>
                </header>

                <section className="home-grid">
                    {VIEWS.map((view) => (
                        <ViewCard key={view.id} view={view} />
                    ))}

                    <div className="view-card view-card--skeleton" aria-hidden="true">
                        <div className="view-card__content">
                            <h2 className="view-card__title skeleton-title">
                                <span className="skeleton-title__full">Constructing...</span>
                                <span className="skeleton-title__short">TODO:</span>
                            </h2>
                            <div className="skeleton-lines">
                                <span className="skeleton-line" />
                                <span className="skeleton-line skeleton-line--short" />
                            </div>
                        </div>
                    </div>
                </section>
            </main>
        </>
    );
}

export default HomePage;
