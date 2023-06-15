document.addEventListener("DOMContentLoaded", function() {
  // Obtener todos los enlaces de la navbar
  const navbarLinks = document.querySelectorAll("nav ul li a");

  // Agregar el evento de clic a cada enlace
  navbarLinks.forEach(function(link) {
    link.addEventListener("click", function(event) {
      event.preventDefault(); // Evitar el comportamiento predeterminado del enlace

      // Obtener el identificador de la sección objetivo del enlace
      const target = link.getAttribute("href");

      // Desplazarse suavemente a la sección objetivo
      document.querySelector(target).scrollIntoView({
      });
    });
  });
});