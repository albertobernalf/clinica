
//const abrirModal = document.getElementById('abrirModal');
const miModal1 = document.getElementById('modalActualizaTriage');
const cerrarModal1 = document.getElementById('cerrarModal');
const btnAceptar1 = document.getElementById('btnAceptar');
const btnCancelar1 = document.getElementById('btnCancelar');

// Abrir modal
//abrirModal.addEventListener('click', () => {
//    miModal.style.display = 'flex';       
//});

// Cerrar modal con la 'X'
 //cerrarModal1.addEventListener('click', () => {
 //   miModal1.style.display = 'none';
// });

// Cerrar modal con botones
btnAceptar1.addEventListener('click', () => {
    alert('¡Acción aceptada!');
    miModal1.style.display = 'none';
});

btnCancelar1.addEventListener('click', (e) => {
    e.preventDefault(); // 👈 Esto evita que la página se recargue

    miModal1.style.display = 'none';
});

// Cerrar al hacer clic fuera del contenido de la modal
window.addEventListener('click', (e) => {
    if (e.target === miModal1) {
    e.preventDefault(); // 👈 Esto evita que la página se recargue
        miModal1.style.display = 'none';
    }
});


$('#tablaDatosTriage tbody').on('click', '.miEditaTriage', function(e) {

	 var post_id = $(this).data('pk');
	var row = $(this).closest('tr'); // Encuentra la fila
	// alert("post_id=" + post_id);
	// alert("row=" + row);
	var triageId= post_id;
	 var sede =  document.getElementById("sede").value;
	 var username =  document.getElementById("username").value;


	var table = $('#tablaDatosTriage').DataTable();  // Inicializa el DataTable jquery 	      
        var rowindex = table.row(row).data(); // Obtiene los datos de la fila
        dato1 = Object.values(rowindex);
	console.log(" fila seleccionad d evuelta dato1 = ",  dato1);
        dato3 = dato1[2];
	console.log(" fila selecciona de vuelta dato3 = ",  dato3);
	console.log(" fila selecciona de vuelta dato3 = ",  dato3);
	// alert(" fila selecciona de vuelta dato3  glosaId= " +   dato3.Documento);
	// alert(" fila selecciona de vuelta dato3 factura = " + dato3.tipoDoc);
	// alert("Voy ajax editar Triage");
	

      $.ajax({
		type: 'POST',
    	url: '/encuentraTriageModal/',
		data: {'triageId':triageId,'sede':sede,'tiposDoc':dato3.tipoDoc,'documento':dato3.Documento},
		success: function (response_data) {

       
		var dato =   JSON.parse(response_data['Triage'].servicioSedes);
		// alert("REGRESE dato = " + dato);

                $('#busServicioT').val(response_data['Triage'].servicioSedes);
 
          	    $('#busSubServicioP').val(response_data['Triage'].subServiciosSedes);
				$('#dependenciasP').val(response_data['Triage'].dependencias);
          		$('#tiposDoc').val(response_data['Triage'].tiposDoc);
				$('#busDocumentoSel').val(response_data['Triage'].documento);
				$('#motivo').val(response_data['Triage'].motivo);
				$('#examenFisico').val(response_data['Triage'].examenFisico);
				$('#frecCardiaca').val(response_data['Triage'].frecCardiaca);
				$('#frecRespiratoria').val(response_data['Triage'].frecRespiratoria);
				$('#taSist').val(response_data['Triage'].taSist);
				$('#taDiast').val(response_data['Triage'].taDiast);
				$('#taMedia').val(response_data['Triage'].taMedia);
				$('#glasgow').val(response_data['Triage'].glasgow);
				$('#peso').val(response_data['Triage'].peso);
				$('#temperatura').val(response_data['Triage'].temperatura);
				$('#estatura').val(response_data['Triage'].estatura);
				$('#glucometria').val(response_data['Triage'].glucometria);
				$('#saturacion').val(response_data['Triage'].saturacion);
				$('#escalaDolor').val(response_data['Triage'].escalaDolor);
				$('#tipoIngreso').val(response_data['Triage'].tipoIngreso);
				$('#observaciones').val(response_data['Triage'].observaciones);
				$('#clasificacionTriage').val(response_data['Triage'].clasificacionTriage);
				// alert("Voy a abrit la modal = ");

			alert("Voy a abrir la  ventana");
  e.preventDefault(); // 👈 Esto evita que la página se recargue		
				//  $('#modalActualizaTriage').modal('show');

			alert("ya abri la vengtana .. Modal ...");
			 const miModal1 = document.getElementById('modalActualizaTriage');
			  
			 miModal1.style.display = 'flex';


		//	$('#modalActualizaTriage').modal({show:true});
			$('#clasificacionTriage').val(response_data['Triage'].clasificacionTriage);
                    },
   		   			 error: function(data){
		       		document.getElementById("mensajesError").innerHTML =  data.responseText

	   	    	}
	});
	});


