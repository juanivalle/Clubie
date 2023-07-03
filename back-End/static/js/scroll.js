ScrollReveal({
    reset: true,
    distance: '40px',
    duration: '1000',
    delay: 300
});

ScrollReveal().reveal('.main-title, .section-title', { delay: 400, origin: 'left' });
ScrollReveal().reveal('.sec-1 .imagen-map', { delay: 400, origin: 'bottom' });
ScrollReveal().reveal('.text-box, .info, .media-info', { delay: 500, origin: 'right' });
ScrollReveal().reveal('.sec-2 .imagen-map, .sec-4 .imagen-map', { delay: 500, origin: 'top' });
ScrollReveal().reveal('.sec-3 .imagen-map', { delay: 500, origin: 'bottom' });