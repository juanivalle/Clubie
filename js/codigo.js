window.addEventListener("load",inicio);

//lista que almacena los usuarios
let listaUsuarios = new Array();

//lista que almacena las plantas
let listaPlantas = new Array();

//lista que almacena las flores
let listaFlores = new Array();

function inicio(){
    document.querySelector("#btnRegister").addEventListener("click",registrarUsuario);
}

function registrarUsuario() {
    let name = document.querySelector("#txtName").value;
    let pwd = document.querySelector("#txtPwd").value;
    let email = document.querySelector("#txtEmail").value;

    if (name == "" || pwd == "" || email == ""){
        alert("Debe completar todos los campos")
    }
    else {
        if (addUser(name, pwd, 1, email)){
            alert("Usuario registrado correctamente")
            document.querySelector("#txtName").value = "";
            document.querySelector("#txtPwd").value = "";
            document.querySelector("#txtEmail").value = "";
        }
        else {
            alert("Usuario ya existente")
        }
    }
}

function addUser(name, pwd, type, email) {
    let result;
    let exist = userExist(name); //verifica si existe usuario
    if (exist){
        result = false; //No se puede agregar por eso retorna false
    }
    else {
        let aUser = new Usuario(name, pwd, type, email);//Creo el obj usuario guardandolo en una variable
        //Agrego el obj usuario a la lista de usuarios
        listaUsuarios.push(aUser);
        result = true;
    }
    return result;
}

function userExist(name){
    let exist = false;
    for (let i = 0; i < listaUsuarios.length && !exist; i++){
        let objUsuario = listaUsuarios[pos];
        if (objUsuario.nombre.toLowerCase() == name.toLowerCase()){
            exist = true;
        }
    }

    return exist;
}

function addPlant(name, state){
    //funcion que agrega una planta a la lista de plantas
    let objPlant = new Plantas(name, state);
    listaPlantas.push(objPlant);
}

function addFlor(raza, stock, precio){
    //funcion que añade un tipo de flor y su cantidad a la lista de flores
    let objFlor = new Cogollos(raza, stock, precio);
    listaFlores.push(objFlor);
}
