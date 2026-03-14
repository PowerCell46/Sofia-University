document
    .getElementById("arrow-left")
    .addEventListener("click", function handleSwitchLeft(event) {
        const contentParentDiv = event.target.parentNode;
        contentParentDiv.classList.add("fade");

        setTimeout(() => {
            switch (contentParentDiv.querySelector("h2").innerText) {
                case "Софтуерно тестване": {
                    contentParentDiv.querySelector("h2").innerText = "ArcGIS JS API";
                    contentParentDiv.querySelector("img").src = "../assets/courses/arc-gis-js.png";
                    contentParentDiv.querySelectorAll("p")[0].innerHTML = "<span>Стартира на: </span>10.06.2026";
                    contentParentDiv.querySelectorAll("p")[1].innerHTML = "<span>Продължение: </span>4 - месечен курс";
                    contentParentDiv.querySelectorAll("p")[2].innerHTML = "<span>Ниво: </span>За напреднали";
                    break;
                }
                case "Web програмиране с HTML, CSS и JS": {
                    contentParentDiv.querySelector("h2").innerText = "Софтуерно тестване";
                    contentParentDiv.querySelector("img").src = "../assets/courses/software-testing.png";
                    contentParentDiv.querySelectorAll("p")[0].innerHTML = "<span>Стартира на: </span>10.04.2026";
                    contentParentDiv.querySelectorAll("p")[1].innerHTML = "<span>Продължение: </span>2 - месечен курс";
                    contentParentDiv.querySelectorAll("p")[2].innerHTML = "<span>Ниво: </span>За начинаещи";
                    break;
                }
                case "ArcGIS JS API": {
                    contentParentDiv.querySelector("h2").innerText = "Web програмиране с HTML, CSS и JS";
                    contentParentDiv.querySelector("img").src = "../assets/courses/web-programming.png";
                    contentParentDiv.querySelectorAll("p")[0].innerHTML = "<span>Стартира на: </span>10.05.2026";
                    contentParentDiv.querySelectorAll("p")[1].innerHTML = "<span>Продължение: </span>2 - месечен курс";
                    contentParentDiv.querySelectorAll("p")[2].innerHTML = "<span>Ниво: </span>За начинаещи";
                    break;
                }
            }

            contentParentDiv.classList.remove("fade");
        }, 300);
    });

document
    .getElementById("arrow-right")
    .addEventListener("click", function handleSwitchRight(event) {
        const contentParentDiv = event.target.parentNode;
        contentParentDiv.classList.add("fade");

        setTimeout(() => {
            switch (contentParentDiv.querySelector("h2").innerText) {
                case "Софтуерно тестване": {
                    contentParentDiv.querySelector("h2").innerText = "Web програмиране с HTML, CSS и JS";
                    contentParentDiv.querySelector("img").src = "../assets/courses/web-programming.png";
                    contentParentDiv.querySelectorAll("p")[0].innerHTML = "<span>Стартира на: </span>10.05.2026";
                    contentParentDiv.querySelectorAll("p")[1].innerHTML = "<span>Продължение: </span>2 - месечен курс";
                    contentParentDiv.querySelectorAll("p")[2].innerHTML = "<span>Ниво: </span>За начинаещи";
                    break;
                }
                case "Web програмиране с HTML, CSS и JS": {
                    contentParentDiv.querySelector("h2").innerText = "ArcGIS JS API";
                    contentParentDiv.querySelector("img").src = "../assets/courses/arc-gis-js.png";
                    contentParentDiv.querySelectorAll("p")[0].innerHTML = "<span>Стартира на: </span>10.06.2026";
                    contentParentDiv.querySelectorAll("p")[1].innerHTML = "<span>Продължение: </span>4 - месечен курс";
                    contentParentDiv.querySelectorAll("p")[2].innerHTML = "<span>Ниво: </span>За напреднали";
                    break;
                }
                case "ArcGIS JS API": {
                    contentParentDiv.querySelector("h2").innerText = "Софтуерно тестване";
                    contentParentDiv.querySelector("img").src = "../assets/courses/software-testing.png";
                    contentParentDiv.querySelectorAll("p")[0].innerHTML = "<span>Стартира на: </span>10.04.2026";
                    contentParentDiv.querySelectorAll("p")[1].innerHTML = "<span>Продължение: </span>2 - месечен курс";
                    contentParentDiv.querySelectorAll("p")[2].innerHTML = "<span>Ниво: </span>За начинаещи";
                    break;
                }
            }

            contentParentDiv.classList.remove("fade");
        }, 300);
    });
