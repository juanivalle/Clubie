var txtTelefono = document.getElementById('txtTelefono');
var txtCi = document.getElementById('txtCi');
var edad = document.getElementById("edad");
var txtEmail = document.getElementById("txtEmail")
var txtName = document.getElementById("txtName");
var campotexto = document.getElementById("campotexto");
var campolargo = document.getElementById("campolargo");

let form = document.getElementById("registerform");

form.addEventListener("submit", (e) => {
    e.preventDefault();
    if (validar_form_miembros() === false) return;
    // e.submit();
    console.log('test');
})

function validar_form_miembros() {
    return valortelefono() &&
        valorcedula() &&
        valormail() &&
        valorusuario();
}
// function validar_form_trazabilidad() {
//     valortelefono();
//     valoredad();
//     valorcedula();
// }
// function validar_login() {
//     valormail();
// }
// function validar_contacto(){
//     valormail();
//     valorusuario();
//     textos();
// }

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
        return false;
    }
    return true;
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
    var txtCiValue = txtCi.value;
    soloNumeros(e);
    if (txtCiValue.length > 8 || txtCiValue.length < 7) {
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

