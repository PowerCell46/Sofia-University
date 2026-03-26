type ImageType = "Natural color" | "False color" | "Highlight optimised color";

interface PanelState {
    imageType: ImageType;
    sourceUrl: string;
    alt: string;
}

const panelState: Record<ImageType, PanelState> = {
    "Natural color": {
        imageType: "False color",
        sourceUrl: "./images/falseColor.png",
        alt: "False color Saint James 21.03.2026"
    },
    "False color": {
        imageType: "Highlight optimised color",
        sourceUrl: "./images/highlightOptimisedColor.png",
        alt: "Highlight optimised color Saint James 21.03.2026"
    },
    "Highlight optimised color": {
        imageType: "Natural color",
        sourceUrl: "./images/naturalColor.png",
        alt: "Natural color Saint James 21.03.2026"
    }
};

const carouselMapPanel: Element | null = document.querySelector(".carousel-map-panel");

if (carouselMapPanel) {
    setInterval(() => {
        const imageTypeParagraph: Element | null = carouselMapPanel.querySelector("p");

        if (imageTypeParagraph) {
            const image: HTMLImageElement | null = carouselMapPanel.querySelector("img");

            image?.classList.add("fading");
            imageTypeParagraph.classList.add("fading");

            setTimeout(() => {
                if (image) {
                    image.src = panelState[imageTypeParagraph.textContent as ImageType].sourceUrl;
                    image.alt = panelState[imageTypeParagraph.textContent as ImageType].alt;
                    image.classList.remove("fading");
                }

                imageTypeParagraph.textContent = panelState[imageTypeParagraph.textContent as ImageType].imageType;
                imageTypeParagraph.classList.remove("fading");
            }, 600); // 600ms
        }
    }, 1_000 * 5); // every 5 seconds
}
