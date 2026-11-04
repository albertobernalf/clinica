const abrirModal = document.getElementById('createNewPost');
const miModal = document.getElementById('crearConvenioModel');
// const cerrarModal = document.getElementById('cerrarModal');
// const btnAceptar = document.getElementById('btnAceptarcrearConvenioModel');
const btnCancelar = document.getElementById('btnCancelarcrearConvenioModel');


ingresoId1 = document.getElementById("ingresoId1").value
document.getElementById("ingresoId2").value = ingresoId1;



// Abrir modal
abrirModal.addEventListener('click', () => {
    miModal.style.display = 'flex';
});

// Cerrar modal con la 'X'
 //cerrarModal.addEventListener('click',  () =>
// {
//       event.preventDefault(); // 👈 ESTO evita que la página se recargue
//        $('#crearConvenioModel').modal('hide');
//        // miModal.style.display = 'none';
//  });

// Cerrar modal con botones
// btnAceptar.addEventListener('click',  () =>
// {

//    alert('¡Acción aceptada!');
//     miModal.style.display = 'none';

// });

 btnCancelar.addEventListener('click',  (e) =>
 {

    e.preventDefault();

     miModal.style.display = 'none';
});

// Cerrar al hacer clic fuera del contenido de la modal
window.addEventListener('click', (e) =>
{
        if (e.target === miModal) {
            miModal.style.display = 'none';
        }
});
