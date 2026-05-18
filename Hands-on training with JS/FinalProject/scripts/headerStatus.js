const headerStatus = document.querySelector("#header-status");


export function updateHeaderStatus(statusMessage) {
    setTimeout(() => headerStatus.textContent = statusMessage, 250);
    setTimeout(() => headerStatus.textContent = "Hello there, GIS explorer!", 2_500);
}
