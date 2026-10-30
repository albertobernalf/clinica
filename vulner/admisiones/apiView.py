from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer , JSONRenderer
#from django.contrib.auth.models import User
from admisiones.models import Furips
#from django.shortcuts import get_object_or_404
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse, HttpResponseRedirect
from rest_framework import status
from admisiones.serializers import FuripsSerializer
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from rest_framework import permissions, generics
import json
from django.http import JsonResponse
import traceback # Para poder imprimir el error real
from admisiones.serializers import FuripsSerializer, TiposDocumentoSerializer, SedesClinicaSerializer, UsuariosSerializer, IngresosSerializer

from admisiones.models import Furips, Ingresos
from usuarios.models import  TiposDocumento, Usuarios
from sitios.models import  SedesClinica
from django.db import transaction, IntegrityError

#class FuripsDetailView(generics.RetrieveUpdateAPIView):

    # If testing locally without auth, you might temporarily use AllowAny
    #permission_classes = [permissions.IsAuthenticated]
    #permission_classes = [permissions.AllowAny]

@method_decorator(csrf_exempt, name='dispatch') # 👈 Desactiva CSRF para esta vista
class FuripsDetailView(APIView):
    # Soportamos HTML para el formulario y JSON para la respuesta del PUT
    print("Acceso una clase FuripsDetalView")
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
    template_name = 'editarFurips.html'

    def get(self, request, pk=None, ingresoId= None):
        """Renderiza el formulario con los datos actuales de la tarea."""
        print("Entre por GET FuripsDetaIlView = ")
        tiposDocumento = TiposDocumento.objects.all()
        serializerTiposDocumento = TiposDocumentoSerializer(tiposDocumento, many=True)
        sedesClinica = SedesClinica.objects.all()
        serializerSedesClinica = SedesClinicaSerializer(sedesClinica, many=True)
        usuarios = Usuarios.objects.all()
        serializerUsuarios = UsuariosSerializer(usuarios, many=True)

        pk = request.query_params.get('pk', None)
        ingresoId = request.query_params.get('ingresoId', 0)
        print("Entre por GET FuripsDetaIlView_2 admision = ", ingresoId)
        print("Entre por GET FuripsDetaIlView_2 pk = ", pk)

        try:
            with transaction.atomic():
                # fur  = Furips.objects.get(id=pk)
                fur = Furips.objects.filter(admision_id=ingresoId)
                # fur = Furips.objects.filter(admision_id=1)
                print("Encontre FURIPS")
                print("furips = ", fur)
                serializer = FuripsSerializer(fur, many=True)
                print("serializer.data = ", serializer.data)
                print("serializer = ", serializer)
                # 3. Construir y enviar la respuesta combinada
                print("Armo RESPONSE")
                response_data = {
                    'furips': serializer.data,
                    'tiposDocumento': serializerTiposDocumento.data,
                    'sedesClinica': serializerSedesClinica.data,
                    'usuarios': serializerUsuarios.data,
                }
                print("response_data = ", response_data)

                return Response(response_data, status=status.HTTP_200_OK, template_name=self.template_name)

        except Exception as e:
            # Aquí ya se hizo rollback automáticamente
            print("Se hizo rollback por PRONO SE HACE NADA:", e)
            # Manejo personalizado si no existe
            print("Entre no existe pk", ingresoId)
            furips = None
            serializer = None
            response_data = {
                'furips': '',
                'tiposDocumento': serializerTiposDocumento.data,
                'sedesClinica': serializerSedesClinica.data,
                'usuarios': serializerUsuarios.data,
            }
            print("response_data = ", response_data)

            return Response(response_data, status=status.HTTP_200_OK, template_name=self.template_name)

        finally:
            print("No haga nada")


    # 2. Método POST: Crear un nuevo artículo
    def post(self, request, pk=None):
        print("Entre por POST FuripsDetaIlView_2 ")

        try:
             #furips = get_object_or_404(Furips, pk=None)
             serializer = FuripsSerializer()
             print("datos = " ,  request.data)
             serializer = FuripsSerializer(data=request.data)
             print("Entre por POST FuripsDetalView con estos datos", serializer)
             if serializer.is_valid():
                 print("Voy a guardar el serialize POST 1 ...")
                 serializer.save()
                 print("Voy a guardar el serialize POST 2 ...")
                 return Response({'mensaje': serializer.data, 'status':'ok'}, status=status.HTTP_201_CREATED)
             else:
                 print ("Entre serializaer errores")
                 print(serializer.errors)
                 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            # This helps you see the error in the console during development
            print(f"Error: {e}")
            return JsonResponse({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

#@csrf_protect
    def put(self, request, pk=None, ingresoId= None):
        """Procesa la actualización via PUT."""
        print("Entre por PUT FuripsDetalView con self.args = ", self.args)
        print("Entre por PUT FuripsDetalView con self.kwargs = ", self.kwargs)
        pk = request.query_params.get('pk', None)
        print("Entre por PUT FuripsDetaIlView_2 admision = ", pk)
        serializer = FuripsSerializer(Furips, data=request.data)
        #if not pk:
        #    return Response({"error": "Método PUT requiere un ID (pk)"}, status=status.HTTP_400_BAD_REQUEST)

        try:
             furips = get_object_or_404(Furips, pk=pk)
             serializer = FuripsSerializer()
             serializer = FuripsSerializer(furips, data=request.data)
             print("Entre por PUT FuripsDetalView con estos datos", serializer)
             if serializer.is_valid():
                 print("VOy PUT  guardar el serialize ")
                 serializer.save()
                 #return JsonResponse({'status': 'success'})
                 return JsonResponse({'mensaje': 'datos Actualizados !', 'status':'ok'}, status=status.HTTP_202_ACCEPTED)
                 #return Response({'mensaje': 'datos Actualizados !', 'status':'ok'}, status=status.HTTP_202_ACCEPTED)

             else:
                 print(serializer.errors)
                 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            # This helps you see the error in the console during development
            print(f"Error: {e}")
            #return JsonResponse({'error': str(e)}, status=500)
            return JsonResponse({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class load_dataAdmisionesApiView(APIView):

    def get(self, request , data=None, *args, **kwargs):
        try:
            print("Entre a load_dataAdmisionesApiView")
            tiposDocumento = TiposDocumento.objects.all()
            serializerTiposDocumento = TiposDocumentoSerializer(tiposDocumento, many=True)
            sedesClinica = SedesClinica.objects.all()
            serializerSedesClinica = SedesClinicaSerializer(sedesClinica, many=True)
            usuarios = Usuarios.objects.all()
            serializerUsuarios = UsuariosSerializer(usuarios, many=True)

            context = {}
            print ("data PURO = ", data)
            #d = json.loads(data)
            #print("d = ", d)
            #print("d = ", d['sede'])

            #Sede = d['sede']
            #Sede = data.get("sede")
            Sede=1

            print("sede = ", Sede)

            detalle = 'SELECT i.id id, tp.nombre tipoDoc,  i.documento_id , u.nombre AS nombre_Paciente , i.consec consec , i."fechaIngreso" , sd.nombre AS servicioNombreIng, dep.nombre camaNombreIng , diag.nombre dxActual, (select count(*)  from facturacion_conveniospacienteingresos conv where conv."tipoDoc_id" = i."tipoDoc_id" and conv.documento_id=i.documento_id  and conv."consecAdmision"=i.consec) numConvenios,	(select count(*)  from cartera_pagos pag where pag."tipoDoc_id" = i."tipoDoc_id" and pag.documento_id=i.documento_id  and pag.consec=i.consec) numPagos,	i.empresa_id, date_part(' + "'" + str('YEAR') + "'" + ' ,  AGE(CURRENT_DATE , U."fechaNacio")) edad, i."salidaClinica" salidaClinica FROM admisiones_ingresos i inner join usuarios_usuarios u on ( u."tipoDoc_id" = i."tipoDoc_id"  and u.id = i.documento_id) left join facturacion_empresas empresa on (empresa.id = i.empresa_id) inner join sitios_dependencias dep on (dep.id = i."dependenciasActual_id" and dep."sedesClinica_id" =  i."sedesClinica_id" AND dep.disponibilidad = ' + "'" + str('O') + "')" + ' inner join sitios_serviciosSedes sd on (sd."sedesClinica_id" = i."sedesClinica_id" and sd.id= dep."serviciosSedes_id" and sd.id  = i."serviciosActual_id")  inner join clinico_servicios ser on (ser.id = sd.servicios_id and ser.nombre != ' + "'" + str('TRIAGE') + "')" + ' inner join usuarios_tiposDocumento tp on (tp.id = u."tipoDoc_id") inner join sitios_dependenciastipo deptip on ( deptip.id = dep."dependenciasTipo_id") left join  clinico_Diagnosticos diag on (diag.id = i."dxActual_id")  WHERE  i."sedesClinica_id" = ' + "'" + str(Sede) + "'" + ' AND i."salidaDefinitiva" = ' + "'" + str('N') + "'" + ' AND i."fechaSalida" is null'
            #detalle = 'SELECT i.id id, tp.nombre tipoDoc,  u.nombre  nombre , i.consec consec , i."fechaIngreso" , sd.nombre servicioNombreIng, dep.nombre camaNombreIng , diag.nombre dxActual, (select count(*)  from facturacion_conveniospacienteingresos conv where conv."tipoDoc_id" = i."tipoDoc_id" and conv.documento_id=i.documento_id  and conv."consecAdmision"=i.consec) numConvenios,	(select count(*)  from cartera_pagos pag where pag."tipoDoc_id" = i."tipoDoc_id" and pag.documento_id=i.documento_id  and pag.consec=i.consec) numPagos,	date_part(' + "'" + str('YEAR') + "'" + ' ,  AGE(CURRENT_DATE , U."fechaNacio")) edad, i."salidaClinica" salidaClinica FROM admisiones_ingresos i inner join usuarios_usuarios u on ( u."tipoDoc_id" = i."tipoDoc_id"  and u.id = i.documento_id) left join facturacion_empresas empresa on (empresa.id = i.empresa_id) inner join sitios_dependencias dep on (dep.id = i."dependenciasActual_id" and dep."sedesClinica_id" =  i."sedesClinica_id" AND dep.disponibilidad = ' + "'" + str('O') + "')" + ' inner join sitios_serviciosSedes sd on (sd."sedesClinica_id" = i."sedesClinica_id" and sd.id= dep."serviciosSedes_id" and sd.id  = i."serviciosActual_id")  inner join clinico_servicios ser on (ser.id = sd.servicios_id and ser.nombre != ' + "'" + str('TRIAGE') + "')" + ' inner join usuarios_tiposDocumento tp on (tp.id = u."tipoDoc_id") inner join sitios_dependenciastipo deptip on ( deptip.id = dep."dependenciasTipo_id") left join  clinico_Diagnosticos diag on (diag.id = i."dxActual_id")  WHERE  i."sedesClinica_id" = ' + "'" + str(Sede) + "'" + ' AND i."salidaDefinitiva" = ' + "'" + str('N') + "'" + ' AND i."fechaSalida" is null'
            #detalle = """SELECT i.id id, tp.nombre tipoDoc,  u.documento documento, u.nombre  nombre , i.consec consec , i."fechaIngreso" , sd.nombre servicioNombreIng, dep.nombre camaNombreIng , diag.nombre dxActual, (select count(*)  from facturacion_conveniospacienteingresos conv where conv."tipoDoc_id" = i."tipoDoc_id" and conv.documento_id=i.documento_id  and conv."consecAdmision"=i.consec) numConvenios,	(select count(*)  from cartera_pagos pag where pag."tipoDoc_id" = i."tipoDoc_id" and pag.documento_id=i.documento_id  and pag.consec=i.consec) numPagos,	empresa.nombre Empresa, date_part(' + "'" + str('YEAR') + "'" + ' ,  AGE(CURRENT_DATE , U."fechaNacio")) edad, i."salidaClinica" salidaClinica FROM admisiones_ingresos i inner join usuarios_usuarios u on ( u."tipoDoc_id" = i."tipoDoc_id"  and u.id = i."documento_id" ) left join facturacion_empresas empresa on (empresa.id = i.empresa_id) inner join sitios_dependencias dep on (dep.id = i."dependenciasActual_id" and dep."sedesClinica_id" =  i."sedesClinica_id" AND dep.disponibilidad = ' + "'" + str('O') + "')" + ' inner join sitios_serviciosSedes sd on (sd."sedesClinica_id" = i."sedesClinica_id" and sd.id= dep."serviciosSedes_id" and sd.id  = i."serviciosActual_id")  inner join clinico_servicios ser on (ser.id = sd.servicios_id and ser.nombre != ' + "'" + str('TRIAGE') + "')" + ' inner join usuarios_tiposDocumento tp on (tp.id = u."tipoDoc_id") inner join sitios_dependenciastipo deptip on ( deptip.id = dep."dependenciasTipo_id") left join  clinico_Diagnosticos diag on (diag.id = i."dxActual_id")  WHERE  i."sedesClinica_id" = ' + "'" + str(Sede) + "'" + ' AND i."salidaDefinitiva" = ' + "'" + str('N') + "'" + ' AND i."fechaSalida" is null"""

            print("query NUEVO = ", detalle)
            # Ejecutamos la consulta cruda
            admisiones_raw = Ingresos.objects.raw(detalle)
            print("admisiones_raw = ", admisiones_raw)
            # Construimos la lista de diccionarios para responder en formato JSON
            #ingresos = []
            print (" A barrer admisiones_raw ULT_VERSION ")
            #for barre in admisiones_raw:
            #    print("Entro al FOR barre : ", barre)

            #    ingresos.append({"id": barre.id,
                                 # "tipoDoc": getattr(barre, 'tipoDoc', 'Sin tipoDoc'),
                                 # "sede": prod.sede,
            #                     "tipoDoc": getattr(barre, 'tipoDoc', 'Sin TipoDoc'),
                                 #"Documento": getattr(barre, 'documento', 'Sin documento'),
            #                     "Documento": barre.documento,
            #                     "NombrePaciente": barre.NombrePaciente,
            #                     "consec": barre.consec,
            #                     "fechaIngreso": barre.fechaIngreso,
                                 # "servicioNombreIng": barre.servicioNombreIng,
            #                     "servicioNombreIng": getattr(barre, 'servicioNombreIng', 'Sin servicioNombreIng'),
                                 # "camaNombreIng": barre.camaNombreIng,
            #                    "camaNombreIng": getattr(barre, 'camaNombreIng', 'Sin camaNombreIng'),
                                 # "dxActual": barre.dxActual,
            #                     "dxActual": getattr(barre, 'dxActual', 'Sin dxActual'),
            #                     "numConvenios": barre.numConvenios,
            #                     "numPagos": barre.numPagos,
                                 # "Empresa": barre.Empresa,
                                 #"Empresa": getattr(barre, 'Empresa', 'Sin Empresa'),
            #                     "edad": barre.edad,
            #                     "salidaClinica": barre.salidaClinica, })
            #print("data de Ingresos = ", ingresos)


            # DataTables espera una estructura, para este ejemplo básico enviamos la lista en una llave "data"
            # return Response({"data": data,'status':"ok"}, status=status.HTTP_200_OK)

            #serialized1 = json.dumps(ingresos, default=str)

            #return HttpResponse(serialized1, content_type='application/json')

            admisionesList_raw = list(admisiones_raw)
            print ("admisionesList_raw =" , admisionesList_raw )
            serializer = IngresosSerializer(admisionesList_raw, many=True)
            print ("me voy")

            return Response(serializer.data, status=status.HTTP_200_OK)


            #return 'ok'


        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
