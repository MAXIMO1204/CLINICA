let menuVisible = false;

// Función que oculta o muestra el menú
function mostrarOcultarMenu() {
    const nav = document.getElementById("nav");

    if (menuVisible) {
        nav.classList.remove("responsive");
        menuVisible = false;
    } else {
        nav.classList.add("responsive");
        menuVisible = true;
    }
}

// Función para manejar la selección de enlaces del menú
function seleccionar(event) {
    event.preventDefault(); // Previene el comportamiento por defecto del enlace

    // Obtener el ID del enlace que ha sido clickeado
    const id = event.target.getAttribute("href").substring(1);

    // Obtener la sección correspondiente
    const section = document.getElementById(id);

    // Hacer scroll a la sección correspondiente
    section.scrollIntoView({ behavior: "smooth" });

    // Ocultar el menú después de la selección (para móvil)
    const nav = document.getElementById("nav");
    nav.classList.remove("responsive");
    menuVisible = false;
}

// Añadir evento de scroll para detectar la sección visible y colorear el enlace activo
document.addEventListener("scroll", function () {
    const sections = document.querySelectorAll("section");
    const navLinks = document.querySelectorAll("#nav a");

    sections.forEach(function (section, index) {
        const top = section.offsetTop - 50; // Ajusta según el tamaño de tu menú fijo
        const bottom = top + section.clientHeight;

        if (window.scrollY >= top && window.scrollY < bottom) {
            navLinks.forEach(function (link) {
                link.style.color = ""; // Reinicia todos los colores
            });
            navLinks[index].style.color = "#07ac96"; // Colorea el enlace activo
        }
    });
});




