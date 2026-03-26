const greetingFormElement: Element | null = document.querySelector(".greeting-form");

greetingFormElement?.addEventListener("submit", handleSubmissionOfGreetingForm);


function handleSubmissionOfGreetingForm(event: Event): void {
    event.preventDefault();

    const formData: FormData = new FormData(event.target as HTMLFormElement);

    const name: FormDataEntryValue | null = formData.get("name");

    const greetingHeadingElement: Element | null = document.getElementById("greeting-heading");

    if (greetingHeadingElement) {
        greetingHeadingElement.textContent = name ? `Здравей, ${name}!` : "Добре дошли";
    }
}
