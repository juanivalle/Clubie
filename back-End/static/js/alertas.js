//MIEMBROS

let btnMiembro = document.getElementById('btnmiembro');
btnMiembro.addEventListener('click', function() {
    alert('El miembro se cargó correctamente.');
});

let btnDelete = document.getElementById('btndelete');
btnDelete.addEventListener('click', function(event) {
    var confirmation = confirm('¿Estás seguro de que deseas eliminar el miembro?');
    if (!confirmation) {
        event.preventDefault();
        console.log('La eliminación del miembro fue cancelada.');
    }
});

let btnEdit = document.getElementById('btnedit');
btnEdit.addEventListener('click', function() {
    alert('Seguro que desea editar el miembro?');
});

//VENTAS

let btnSave = document.getElementById('btnsave');
btnSave.addEventListener('click', function() {
  alert('La venta se cargó correctamente.');
});

//TRAZABILIDAD

let btnTrzbld = document.getElementById('btnTrazabilidad');
btnTrzbld.addEventListener('click', function() {
  alert('Datos actualizados.');
});

//CONTROL PLANTAS misma funcion que se usa para editar y borrar miembros
/*
let btnDelete = document.getElementById('btndelete');
btnDelete.addEventListener('click', function(event) {
  var confirmation = confirm('¿Estás seguro de que deseas eliminar el miembro?');
  if (!confirmation) {
    event.preventDefault();
    console.log('La eliminación del miembro fue cancelada.');
  }
});

let btnEdit = document.getElementById('btnedit');
btnEdit.addEventListener('click', function() {
  alert('Seguro que desea editar el miembro?');
});
*/

//HOME - CONTACTOS

let btnOk = document.getElementById('btnok');
btnOk.addEventListener('click', function() {
    alert('Mensaje enviado correctamentes');
});


