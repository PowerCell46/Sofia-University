function handleSectionDiv(e) {
    const hiddenElement = e.target.parentNode.parentNode.querySelector(".hidden");
    const iconElement = e.target.parentNode.parentNode.querySelector('i');

    if (hiddenElement.classList.contains('active')) {
        hiddenElement.classList.remove('active');
        iconElement.classList.remove("fa-arrow-up");
        iconElement.classList.add("fa-arrow-down");
        
        setTimeout(() => {
            hiddenElement.style.height = '0';
        }, 1000);
    } else {
        hiddenElement.classList.add('active');
        hiddenElement.style.height = 'auto'; 
        iconElement.classList.remove("fa-arrow-down");
        iconElement.classList.add("fa-arrow-up");
    }
}
