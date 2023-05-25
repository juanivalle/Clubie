var swiper = new Swiper(".mySwiper", {
    effect: "coverflow",
    grabCursor:true,
    centeredSlides:true,
    slidesPerView: "auto",
    coverflowEffect: {
        rotate: 15,
        strech: 0,
        depth: 300,
        modifier: 1,
        slideShadows: false,
    },
    loop: true,
    autoplay: {
        delay: 3000, // Tiempo de espera entre cada transición de diapositiva en milisegundos
        disableOnInteraction: false, // Permite la reproducción automática incluso cuando el usuario interactúa con el slider
      },
});