var $ = jQuery;
const abrirModal = document.getElementById('miModal');
// const cancelarModal = document.getElementById('btnCancelarFolio');

$("#btnGuardarFolio").click(function (e) {
  e.preventDefault();

  alert("Entre Guardar Folio ultimo");
});
// Abrir modal
abrirModal.addEventListener('click', () => {
	alert ("Entre a modal-salir");
    miModal.style.display = 'flex';       
});
$("#btnCancelarFolio").click(function (e) {
  e.preventDefault();

  alert("Entre Cancelar Folio modal");
  miModal.style.display = "none";
  alert("YA desactive  modal");
});
