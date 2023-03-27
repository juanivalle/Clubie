const bdark = document.querySelector("#bdark");
const body = document.querySelector('body');
const isChecked = localStorage.getItem('isChecked');

// para subir perfil::::::: const btnperfil = document.getElementById('btn-perfil');
// para subir perfil::::::: const fileInput = document.getElementById('file-input');

// Si el estado guardado es "true", agregar la clase "darkmode" al body
if (isChecked === 'true') {
  body.classList.add('darkmode');
  bdark.classList.add('active');
}


// Agregar un event listener al checkbox
bdark.addEventListener('click', () => {
    // Agregar o quitar la clase "darkmode" dependiendo del estado del checkbox
    body.classList.toggle('darkmode');
    
    // Agregar o quitar la clase "active" dependiendo del estado del checkbox
    bdark.classList.toggle('active', body.classList.contains('darkmode'));
    
    // Guardar el estado del checkbox en localStorage
    localStorage.setItem('isChecked', body.classList.contains('darkmode'));
});

///SUBIR PERFIL JS
/*fileInput.addEventListener('change', (event) => {
  const file = event.target.files[0];
  const reader = new FileReader();
  reader.readAsDataURL(file);
  reader.onload = (event) => {
    const imageUrl = event.target.result;
    btnperfil.style.backgroundImage = `url(${imageUrl})`;
  }
});*/










































//PAGINA LOGIN

  
  // Establecer el foco en el elemento del formulario
  
  

const $btnSignIn= document.querySelector('.sign-in-btn'),
      $btnSignUp = document.querySelector('.sign-up-btn'),  
      $signUp = document.querySelector('.sign-up'),
      $signIn  = document.querySelector('.sign-in');
     
document.addEventListener('click', e => {
    if (e.target === $btnSignIn || e.target === $btnSignUp) {
        $signIn.classList.toggle('active');
        $signUp.classList.toggle('active')
    }
});
///////////////////////////////////////////////////////////////////////////