document.addEventListener("DOMContentLoaded", function() {
    var video = document.getElementById("myVideo");
    var logoMovil = document.getElementById("logo-movil");

    video.addEventListener("click", function() {
      if (video.paused) {
        video.play();
      } else {
        video.pause();
      }
    });
    window.addEventListener("scroll", function() {
        var scrollPosition = window.scrollY;
        var logoPosition = logoMovil.getBoundingClientRect().top;

        if (scrollPosition > logoPosition) {
            logoMovil.style.right = (window.innerWidth / 2) + "px";
        } else {
            logoMovil.style.right = "-1000px";
        }
    });
  });