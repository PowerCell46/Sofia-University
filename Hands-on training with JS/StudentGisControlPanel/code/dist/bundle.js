"use strict";
const panelState = {
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
const carouselMapPanel = document.querySelector(".carousel-map-panel");
if (carouselMapPanel) {
    setInterval(() => {
        const imageTypeParagraph = carouselMapPanel.querySelector("p");
        if (imageTypeParagraph) {
            const image = carouselMapPanel.querySelector("img");
            image === null || image === void 0 ? void 0 : image.classList.add("fading");
            imageTypeParagraph.classList.add("fading");
            setTimeout(() => {
                if (image) {
                    image.src = panelState[imageTypeParagraph.textContent].sourceUrl;
                    image.alt = panelState[imageTypeParagraph.textContent].alt;
                    image.classList.remove("fading");
                }
                imageTypeParagraph.textContent = panelState[imageTypeParagraph.textContent].imageType;
                imageTypeParagraph.classList.remove("fading");
            }, 600); // 600ms
        }
    }, 1000 * 5); // every 5 seconds
}
const greetingFormElement = document.querySelector(".greeting-form");
greetingFormElement === null || greetingFormElement === void 0 ? void 0 : greetingFormElement.addEventListener("submit", handleSubmissionOfGreetingForm);
function handleSubmissionOfGreetingForm(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const name = formData.get("name");
    const greetingHeadingElement = document.getElementById("greeting-heading");
    if (greetingHeadingElement) {
        greetingHeadingElement.textContent = name ? `Здравей, ${name}!` : "Добре дошли";
    }
}
