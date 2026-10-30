from django.shortcuts import render

from django.shortcuts import render
import json
from django import forms
import numpy as np
from django.core.serializers import serialize
from django.db.models.functions import Cast, Coalesce
from django.utils.timezone import now
from django.db.models import Avg, Max, Min, Sum
from django.utils import timezone

from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse, HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.urls import reverse, reverse_lazy
# from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView
from django.http import JsonResponse
import pyodbc
import psycopg2
import json
import datetime
from decimal import Decimal
from admisiones.models import Ingresos
from facturacion.models import ConveniosPacienteIngresos, Liquidacion, LiquidacionDetalle, Facturacion, FacturacionDetalle
from cartera.models import TiposPagos, FormasPagos, Pagos, PagosFacturas, GlosasDetalle, NotasCredito, NotasCreditoDetalle, NotasCreditoDetalleRips, GlosasDetalleRips
from triage.models import Triage
from clinico.models import Servicios
from rips.models  import RipsMedicamentos, RipsConsultas, RipsProcedimientos, RipsOtrosServicios, RipsTransaccion
import pickle
from django.db import transaction, IntegrityError
from django.db.models import Sum
from django.db import transaction, IntegrityError
from django.db.models import Q
from decimal import Decimal
import ast


# Function to convert dictionary keys and values
def convert_keys_and_values(d):
    return {str(k) if isinstance(k, Decimal) else k: (float(v) if isinstance(v, Decimal) else v)
            for k, v in d.items()}


def decimal_serializer(obj):
    if isinstance(obj, Decimal):
        return str(obj)
    raise TypeError("Type not serializable")

def serialize_datetime(obj):
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    raise TypeError("Type not serializable")



# Create your views here.


# Create your views here.
def load_dataAgendasMedicas(request, data):

    print("Entre load_dataAgendasMedicas")

    context = {}
    d = json.loads(data)

    username = d['username']
    sede = d['sede']
    username_id = d['username_id']

    nombreSede = d['nombreSede']
    print("sede:", sede)
    print("username:", username)
    print("username_id:", username_id)

    agendasMedicas = []

    miConexionx = psycopg2.connect(host="192.168.133.128", database="vulner7Particionado", port="5432", user="postgres",
                                   password="123456")
    curx = miConexionx.cursor()

    detalle = 'SELECT agendaMedica.id id, agendaMedica."estadoAgenda", agendaMedica."fechaRegistro" fechaRegistro, agendaMedica."estadoReg", esp.nombre especialidadNombre,  espMed.nombre especialidadMedico, sedes.nombre sede, usu.nombre usuarioRegistro FROM public."citasMedicas_agendasmedicas" agendaMedica, public.clinico_Especialidades esp, public."clinico_especialidadesmedicos" espMed, public."sitios_sedesclinica" sedes, public."usuarios_usuarios" usu WHERE agendaMedica."sedesClinica_id" = ' + "'" + str(sede) + "'"

    print(detalle)

    curx.execute(detalle)

    for id,  estadoAgenda, fechaRegistro,  estadoReg, especialidadNombre,especialidadMedico, sede, usuarioRegistro in curx.fetchall():
        agendasMedicas.append(
            {"model": "citasmedicas.agendas", "pk": id, "fields":
                {'id': id, 'estadoAgenda': estadoAgenda,'fechaRegistro':fechaRegistro, 'estadoReg': estadoReg,'especialidadNombre':especialidadNombre,
                 'especialidadMedico':especialidadMedico,  'sede':sede, 'usuarioRegistro': usuarioRegistro}})

    miConexionx.close()
    print("agendasMedicas "  , agendasMedicas)

    context['AgendasMedicas'] = agendasMedicas

    serialized1 = json.dumps(agendasMedicas,  default=str)

    return HttpResponse(serialized1, content_type='application/json')

