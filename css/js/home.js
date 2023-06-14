document.addEventListener("DOMContentLoaded", function() {
    var video = document.getElementById("myVideo");
    var logoMovil = document.getElementById("logo-movil");
    let sec = document.querySelectorAll('section');
    let links = document.querySelectorAll('nav a');

    video.addEventListener("click", function() {
      if (video.paused) {
        video.play();
      } else {
        video.pause();
      }
    });
    window.onscroll = () => {
      sec.forEach(section => {
        let top = window.scrollY;
        let offset = section.offsetTop - 60;
        let height = section.offsetHeight;
        let id = section.getAttribute("id");

        if (top >= offset && top < offset + height) {
          links.forEach(link => {
            document.querySelector('nav a[href*=' + id + ']');
  })}})}});