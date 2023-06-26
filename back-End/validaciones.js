var txtTelefono = document.getElementById('txtTelefono');
var txtCi = document.getElementById('txtCi');
var edad = document.getElementById("edad");
var txtEmail = document.getElementById("txtEmail")
var txtName = document.getElementById("txtName");
var campotexto = document.getElementById("campotexto");
var campolargo = document.getElementById("campolargo");

function validar_form_miembros() {
    valortelefono;
    valorcedula();
    valormail();
    valorusuario();
}
function validar_form_trazabilidad() {
    valortelefono();
    valoredad();
    valorcedula();
}
function validar_login() {
    valormail();
}
function validar_contacto(){
    valormail();
    valorusuario();
    textos();
}

function valormail() {
    var emailValue = txtEmail.value;
    if (!emailValue.includes("@") || emailValue.length <= 5 || /[<>\(\)\[\]\{\}]/.test(emailValue)) {
        Swal.fire({
            icon: 'error',
            title: 'Not a valid email',
        });
    }
}

function valorusuario(e) {
    var key = e.key;
    var texto = e.target.value;

    soloLetras(e);
    var espacios = (texto.match(/\s/g) || []).length;
    var contarespacio = (espacios > 4 || espacios == 0);
    if (contarespacio && key === ' ') {
        e.preventDefault();
    }
}

document.addEventListener('keydown', valorusuario);


function valortelefono(e) {
    soloNumeros(e);
    if (txtTelefono.value.length != 9) {
        txtTelefono.disabled = true;
    } else {
        txtTelefono.disabled = false;
    }
}



function valorcedula(e) {
    soloNumeros(e);
    if (txtCi.value.length >= 9 || txtCi.value.length < 7) {
        txtCi.disabled = true;
    } else {
        txtCi.disabled = false;
    }
}

document.addEventListener('keydown', valorcedula);

function soloNumeros(e) {
    var key = e.key;
    if (key < '0' || key > '9') {
        e.preventDefault();
    }
}

function soloLetras(e) {
    var key = e.key;
    if (!/^[a-zA-Z]$/.test(key)) {
        e.preventDefault();
    }
}

function textos() {
    var textos = campolargo.value;
    var textos2 = campotexto.value;
    if (/[<>\(\)\[\]\{\}]/.test(textos) && (/^[a-zA-Z\s\p{P}]+$/.test(textos))) {
        e.preventDefault();
      }
    else{
        textos.value = "";
        Swal.fire(
            'Invalid text',
            'Try again',
            'question'
          )
    }
    if (/[<>\(\)\[\]\{\}]/.test(textos2) && (/^[a-zA-Z\s\p{P}]+$/.test(textos2))) {
        e.preventDefault();
    }
    else{
        textos2.value = "";
        Swal.fire(
            'Invalid text',
            'Try again',
            'question'
          )
    }
}




function valoredad() {
    if (edad.value.length > 3) {
        edad.disabled = true;
    } else {
        edad.disabled = false;
    }
    if (edad.value < 18) {
        Swal.fire({
            icon: 'error',
            title: 'Can´t be younger than 18 years old',
        });
        edad.value = "";
    }
    if (edad.value > 120) {
        Swal.fire({
            icon: 'error',
            title: 'Too old, right?',
        });
    }
}
