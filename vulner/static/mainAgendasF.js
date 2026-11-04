
console.log('Hola Alberto Hi!')
let dataTable;
let dataTableB;
let dataTableC;
let dataTableAgendasMedicasInitialized =false;


$(document).ready(function() {
    var table = $('#tablaAgendasMedicas').DataTable();
    
       $('#search').on('keyup', function() {
        var searchValue = this.value.split(' '); // Supongamos que los términos de búsqueda están separados por espacios
        
        // Aplica la búsqueda en diferentes columnas
        table
            .columns([3]) // Filtra en la primera columna
            .search(searchValue[0]) // Primer término de búsqueda
            .draw();

	  table
            .columns([9]) // Filtra en la segunda columna
            .search(searchValue[1]) // Segundo término de búsqueda
            .draw();


        
        table
            .columns([14]) // Filtra en la segunda columna
            .search(searchValue[1]) // Segundo término de búsqueda
            .draw();
    });

});

function arrancaAgendasMedicas(valorTabla,valorData)
{
    data = {}
    data = valorData;

    dataApi = {}
    dataApi = valorData;


    if (valorTabla == 1)
    {
        let dataTableOptionsAgendasMedicas  ={

  //dom: "<'row mb-0'<'col-sm-1'B><'col-sm-8'><'col-sm-2'f>>" + // B = Botones a la izquierda, f = filtro a la derecha
  //      dom: '<"d-flex align-items-center mb-3"<"dt-buttons-small"B>r>t<"d-flex justify-content-between"ip>' +
  //           "<'row'<'col-sm-12'tr>>" +  "<'row mt-0'<'col-sm-5'i><'col-sm-7'p>>",

  dom: 'Bfrtilp',
  buttons: [
    {
      extend: 'excelHtml5',
      text: '<i class="fas fa-file-excel"></i> ',
      // text: '<i class="bi bi-file-earmark-excel-fill"></i> Exportar Excel',
      titleAttr: 'Exportar a Excel',
      className: 'btn btn-success btn-sm',
    },
    {
      extend: 'pdfHtml5',
      text: '<i class="fas fa-file-pdf"></i> ',
      titleAttr: 'Exportar a PDF',
      className: 'btn btn-danger btn-sm',
    },
    {
      extend: 'print',
      text: '<i class="fa fa-print"></i> ',
      titleAttr: 'Imprimir',
      className: 'btn btn-info btn-sm',
    },
  ],
	autoWidth: false,
  lengthMenu: [2, 4, 15],
           processing: true,
            serverSide: false,
            scrollY: '450px',
	    scrollX: true,
	    scrollCollapse: true,
            paging:false,
             "rowClass": function( row, data, index ) {
      return 'my-row-class';
    },

 // select: {
  //          style: 'single' // o 'multi'
  //      },

            columnDefs: [
            { width: '1%', targets: [0,1] },
		{ className: 'centered', targets: [0, 1, 2, 3, 4, 5] },
		{   targets: [5,6,7,8], // índice de la columna que quieres evitar que haga wrap

		    },
		{
                    "targets": 8
               }
            ],
	 pageLength: 3,
	  destroy: true,
	  language: {
		    processing: 'Procesando...',
		    lengthMenu: 'Mostrar _MENU_ registros',
		    zeroRecords: 'No se encontraron resultados',
		    emptyTable: 'Ningún dato disponible en esta tabla',
		    infoEmpty: 'Mostrando registros del 0 al 0 de un total de 0 registros',
		    infoFiltered: '(filtrado de un total de _MAX_ registros)',
		    search: "<i class='fa fa-search'></i> Buscar: _INPUT_",
		    infoThousands: ',',
		    loadingRecords: 'Cargando...',
		    paginate: {
			      first: 'Primero',
			      last: 'Último',
			      next: 'Siguiente',
			      previous: 'Anterior',
		    }
			},
           ajax: {
                 url:"/load_dataAgendasMedicas/" +  data,
                 type: "POST",
                 dataSrc: ""
            },
            columns: [

	{
	  "render": function ( data, type, row ) {
                        var btn = '';

              btn = btn + " <input type='radio' id='ingresoId'  name='ingresoId' style='width:15px;height:15px;accent-color: purple;border-color: purple;background-color: purple;' class='miIngresoId form-check-input ' data-pk='"  + row.pk + "'>" + "</input>";


                       return btn;
                    },
	},
                 { data: "fields.id"},
                 { data: "fields.estadoAgenda" },
                { data: "fields.fechaRegistro"},
                { data: "fields.estadoReg"},
                { data: "fields.especialidadNombre"},
                { data: "fields.especialidadMedico"},
                { data: "fields.sede"},
                { data: "fields.usuarioRegistro"},
            ]  ,
	  initComplete: function(settings, json) {
            // Selecciona la primera fila (índice 0)
		var primeraFila = $('#tablaAgendasMedicas tbody tr:eq(0) input[type="radio"]').prop('checked', true);
             $(primeraFila).change();
                 primeraFila.addClass('selected');
        }

             }

	        dataTable = $('#tablaAgendasMedicas').DataTable(dataTableOptionsAgendasMedicas);


  }

}


const initDataTableAgendasMedicas = async () => {
	if  (dataTableAgendasMedicasInitialized)  {
		dataTable.destroy();

}
    	var sedeSeleccionada = document.getElementById("sedeSeleccionada").value;
        var username = document.getElementById("username").value;
        var nombreSede = document.getElementById("nombreSede").value;
    	var sede = document.getElementById("sede").value;
        var username_id = document.getElementById("username_id").value;
        var data =  {}   ;
        data['username'] = username;
        data['sedeSeleccionada'] = sedeSeleccionada;
        data['nombreSede'] = nombreSede;
        data['sede'] = sede;
        data['username_id'] = username_id;

         var valor = $('input[name="ingresoId"]:checked').val();

	 var sede = document.getElementById("sede").value;


              data['sede'] = sede;
       
 	    data = JSON.stringify(data);

        arrancaAgendasMedicas(1,data);
	    dataTableAgendasMedicasInitialized = true;




}

 // COMIENZA ONLOAD

window.addEventListener('load', async () => {
 await  initDataTableAgendasMedicas();


});
 /* FIN ONLOAD */

const abrirModal = document.getElementById('abrirModal');
const miModal = document.getElementById('miModal');
// const cerrarModal = document.getElementById('cerrarModal');
const btnAceptar = document.getElementById('btnAceptar');
const btnCancelar = document.getElementById('btnCancelar');

// Abrir modal
abrirModal.addEventListener('click', () => {
    miModal.style.display = 'flex';
});

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


