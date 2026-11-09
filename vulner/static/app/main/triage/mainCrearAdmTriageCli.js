
//const abrirModal = document.getElementById('abrirModal');
const miModal = document.getElementById('crearAdmTriage');
// const cerrarModal = document.getElementById('cerrarModal');
const btnAceptar = document.getElementById('btnAceptar');
const btnCancelar = document.getElementById('btnCancelar');

// Abrir modal
//abrirModal.addEventListener('click', () => {
//    miModal.style.display = 'flex';
//});

// Cerrar modal con la 'X'
 cerrarModal.addEventListener('click', () => {
    miModal.style.display = 'none';
 });

// Cerrar modal con botones
btnAceptar.addEventListener('click', () => {
    alert('¡Acción aceptada!');
    miModal.style.display = 'none';
});

btnCancelar.addEventListener('click', () => {
    miModal.style.display = 'none';
});

// Cerrar al hacer clic fuera del contenido de la modal
window.addEventListener('click', (e) => {
    if (e.target === miModal) {
        miModal.style.display = 'none';
    }
});


