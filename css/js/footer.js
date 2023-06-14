window.addEventListener('scroll', function() {
    var footer = document.getElementById('myFooter');
    var footerHeight = footer.offsetHeight;
    var windowHeight = window.innerHeight;
    var scrollPosition = window.scrollY || window.pageYOffset || document.documentElement.scrollTop;

    if ((scrollPosition + windowHeight) >= (document.body.offsetHeight - footerHeight)) {
        // Mostrar el footer cuando se llega al final de la página
        footer.style.display = 'block';
    } else {
        // Ocultar el footer en cualquier otra posición
        footer.style.display = 'none';
    }
});