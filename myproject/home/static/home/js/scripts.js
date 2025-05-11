
document.addEventListener("DOMContentLoaded", function () {
    const toggleButton = document.querySelector('[data-collapse-toggle="navbar-hamburger"]');
    const menu = document.getElementById("navbar-hamburger");

    toggleButton.addEventListener("click", function () {
        menu.classList.toggle("hidden");
    });
});

