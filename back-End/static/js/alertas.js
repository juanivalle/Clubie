//MIEMBROS

let btnMiembro = document.getElementById('btnmiembro');
btnMiembro.addEventListener('click', function() {
    alert('El miembro se cargó correctamente.');
});

let btnDelete = document.getElementById('btndelete');
btnDelete.addEventListener('click', function(event) {
    event.preventDefault();
    var confirmation = confirm('¿Estás seguro de que deseas eliminar el miembro?');
    if (confirmation) {
        window.location.href = btnDelete.getAttribute('href');
    } else {
        console.log('La eliminación del miembro fue cancelada.');
    }
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


