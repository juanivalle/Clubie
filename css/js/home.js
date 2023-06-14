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
    })});