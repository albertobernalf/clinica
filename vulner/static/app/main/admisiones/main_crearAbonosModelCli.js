const createNewPostAbonos = document.getElementById('createNewPostAbonos');
const miModalcreateNewPostAbonos = document.getElementById('crearAbonosModel');
// const cerrarModal = document.getElementById('cerrarModal');
// const btnAceptar = document.getElementById('btnAceptarcrearConvenioModel');
const btnCancelarcreateNewPostAbonos = document.getElementById('btnCancelarcrearAbonosModel');


ingresoId1 = document.getElementById("ingresoId1").value
document.getElementById("ingresoId2").value = ingresoId1;


// Abrir modal
createNewPostAbonos.addEventListener('click', () => {
    miModalcreateNewPostAbonos.style.display = 'flex';
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

 btnCancelarcreateNewPostAbonos.addEventListener('click',  (e) =>
 {

    e.preventDefault();

     miModalcreateNewPostAbonos.style.display = 'none';
});

// Cerrar al hacer clic fuera del contenido de la modal
window.addEventListener('click', (e) =>
{
        if (e.target === miModal) {
            miModalcreateNewPostAbonos.style.display = 'none';
        }
});


    	/*------------------------------------------
        --------------------------------------------
        Click to Button
        --------------------------------------------
        --------------------------------------------*/
        $('#createNewPostAbonos').click(function () {

	    var ingresoId= document.getElementById("ingresoId1").value;
	    document.getElementById("ingresoId2").value = ingresoId;

        alert("ingresoId" + ingresoId);

	    if (ingresoId=='undefined')
		{
		// alert("Debe seleccionar Ingreso");
		return;
		}

        // Tiene que hace run ajax para leer los convenios del paciente

		   $.ajax({
	           url: '/buscaConveniosAbonoAdmision/' ,
	            data : {'ingresoId':ingresoId},
	           type: 'POST',
	           dataType : 'json',
	  		success: function (data2) {
	  		// alert("llegue con : " + JSON.stringify(data2));

			if (data2 == '')
				{
				// alert("Debe crear un Convenio");
				document.getElementById("mensajesErrorAbonos").value = 'Debe crear un Convenio';
				return;
				}

	  	    var options = '<option value="=================="></option>';
	  		//var dato = JSON.parse(data2);
            const $id2 = document.querySelector("#convenioPaciente");
 	      	$("#convenioPaciente").empty();
			// alert("voy a llenar combo conveniospaciente");
	                 $.each(data2, function(key,value) {
                                    options +='<option value="' + value.id + '">' + value.nombre + '</option>';
                                    option = document.createElement("option");
                                    option.value = value.id;
                                    option.text = value.nombre;
                                    $id2.appendChild(option);
 	      		      });

            $('#saveBtnCrearAbonos').val("Create Post");
            $('#post_id').val('');
            $('#postFormCrearAbonos').trigger("reset");
            $('#modelHeading').html("Creacion Abonos en admision");
            miModalcreateNewPostAbonos

            // $('#crearAbonosModel').modal('show');
                    },
	   		                error: function(data){
		       		document.getElementById("mensajesErrorAbonos").value =  data.responseText
			        },
      });
        });


                /*------------------------------------------
        --------------------------------------------
        Create Post Code Abonos
        --------------------------------------------
        --------------------------------------------*/
        $('#saveBtnCrearAbonos').click(function (e) {
            e.preventDefault();
            $(this).html('Sending..');

            $.ajax({
                data: $('#postFormCrearAbonos').serialize(),
		  url: "/guardaAbonosAdmision/",
                type: "POST",
                dataType: 'json',
                success: function (data) {

			if (data.success==true)
			{
			document.getElementById("mensajes").value = data.Mensaje;
			}

                    $('#crearAbonosModel').modal('hide');
                    $('#postFormCrearAbonos').trigger("reset");
		  	var sedeSeleccionada = document.getElementById("sedeSeleccionada").value;
		        var username = document.getElementById("username").value;
		        var nombreSede = document.getElementById("nombreSede").value;
		    	var sede = document.getElementById("sede").value;
		        var username_id = document.getElementById("username_id").value;
		        var ingresoId  = document.getElementById("ingresoId22").value;
		         var data =  {}   ;
		        data['username'] = username;
		        data['sedeSeleccionada'] = sedeSeleccionada;
		        data['nombreSede'] = nombreSede;
		        data['sede'] = sede;
		        data['username_id'] = username_id;
			data['ingresoId'] = ingresoId;

          		 data = JSON.stringify(data);

			arrancaAdmisiones(3,data);
		        dataTableAbonosAdmisionesInitialized = true;


                },
                error: function (data) {


			document.getElementById("mensajesErrorAbonoscrearAbonosModel").value =   data.responseText;

		  var tableA = $('#tablaAbonosAdmisiones').DataTable(); // accede de nuevo a la DataTable.
	          tableA.ajax.reload();
                }
            });
        });


/*------------------------------------------
        --------------------------------------------
        Delete Post Code Abonos
        --------------------------------------------
        --------------------------------------------*/
        $("body").on("click",".deletePostAbonos",function(){
            var current_object = $(this);
            var action = current_object.attr('data-action');
            var token = $("input[name=csrfmiddlewaretoken]").val();
            var id = current_object.attr('data-pk');

            alert("Entre a borrar Abono");

		   $.ajax({
	           url: '/postDeleteAbonosAdmision/' ,
	            data : {'id':id},
	           type: 'POST',
	           dataType : 'json',
	  		success: function (data) {

        alert("De regreso de borrar Abono_1");

			if (data.success==false)
            {
		document.getElementById("mensajesError").value =   data.Mensajes;
			}
			else
			{
		document.getElementById("mensajes").value =   data.Mensajes;
			}

			            var table = $('#tablaAbonosAdmisiones').DataTable(); // accede de nuevo a la DataTable.
		                table.ajax.reload();
                        alert("De regreso de borrar Abono");
                    },
	   		    error: function (data) {

                   alert("ERROR de regreso de borrar Abono");

				document.getElementById("mensajesErrorAbonoscrearAbonosModel").value =  data.JresponseText;

	   	    	}


	           });
	});

