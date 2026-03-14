document
    .querySelectorAll(".preferences-buttons-wrapper button")
    .forEach(btn => btn.addEventListener("click", function hangleClickPreferenceButton(event) {
        if ([...event.target.classList].length === 0) {
            event.target.classList.add("preference-selected");

        } else {
            event.target.classList.remove("preference-selected");
        }
    }));