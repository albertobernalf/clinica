from django.contrib import admin

# Register your models here.

from citasMedicas.models import Calendario,TiposCitasMedicas, TiposAtencion, EstadosCitasMedicas, EstadosConsultorios, EstadosProgramacionCitasMedicas, Consultorios, AgendasMedicas, AgendasMedicasProgramacion, EstadoRestriccionAgendas, AgendasMedicasRestriccionProgramacion,  CitasMedicas, CitasMedicasDetalle , CronologiaCitasMedicas
from sitios.models import Dependencias


@admin.register(Calendario)
class calendarioAdmin(admin.ModelAdmin):

   list_display = ("id", "sedesClinica", "fechaDia","nombre")
   search_fields = ("id", "sedesClinica__nombre",  "fechaDia","nombre")
   # Filtrar
   list_filter = ("id", "sedesClinica",   "fechaDia","nombre")


@admin.register(TiposCitasMedicas)
class tiposCitasMedicasAdmin(admin.ModelAdmin):
   list_display = ("id", "nombre")
   search_fields = ("id", "nombre")
   # Filtrar
   list_filter = ("id", "nombre")


@admin.register(TiposAtencion)
class tiposAtencionAdmin(admin.ModelAdmin):
   list_display = ("id", "nombre")
   search_fields = ("id", "nombre")
   # Filtrar
   list_filter = ("id", "nombre")

@admin.register(EstadosCitasMedicas)
class estadosCitasMedicasAdmin(admin.ModelAdmin):
   list_display = ("id", "nombre")
   search_fields = ("id", "nombre")
   # Filtrar
   list_filter = ("id", "nombre")

@admin.register(EstadosConsultorios)
class estadosConsultoriosAdmin(admin.ModelAdmin):
   list_display = ("id", "nombre")
   search_fields = ("id", "nombre")
   # Filtrar
   list_filter = ("id", "nombre")

@admin.register(EstadosProgramacionCitasMedicas)
class estadosProgramacionCitasMedicasAdmin(admin.ModelAdmin):
   list_display = ("id", "nombre")
   search_fields = ("id", "nombre")
   # Filtrar
   list_filter = ("id", "nombre")

@admin.register(Consultorios)
class consultoriosAdmin(admin.ModelAdmin):
   list_display = ("id", "sedesClinica", "dependencia", "nombre","diaDesde","diaHasta","estadosConsultorio")
   search_fields = ("id", "sedesClinica__nombre", "dependencia", "nombre","diaDesde","diaHasta","estadosConsultorio")
   # Filtrar
   list_filter = ("id", "sedesClinica", "dependencia",  "nombre","diaDesde","diaHasta","estadosConsultorio")

@admin.register(AgendasMedicas)
class agendasMedicasAdmin(admin.ModelAdmin):
   list_display = ("id", "sedesClinica", "especialidad", "especialidadesMedicos", "estadoAgenda")
   search_fields = ("id", "sedesClinica", "especialidad", "especialidadesMedicos", "estadoAgenda")
   # Filtrar
   list_filter = ("id", "sedesClinica", "especialidad", "especialidadesMedicos", "estadoAgenda")


@admin.register(AgendasMedicasProgramacion)
class agendasMedicasProgramacionAdmin(admin.ModelAdmin):
   list_display = ("id", "sedesClinica", "agendaMedica", "consultorio", "atiendeDesde","atiendeHasta","desDeHoraDeAlmuerzo","hastaHoraDeAlmuerzo","duracionCita","estadosProgramacioncitasMedicas")
   search_fields = ("id", "sedesClinica__NOMBRE", "agendaMedica", "consultorio", "atiendeDesde","atiendeHasta","desDeHoraDeAlmuerzo","hastaHoraDeAlmuerzo","duracionCita","estadosProgramacioncitasMedicas__nombre")
   # Filtrar
   list_filter = ("id", "sedesClinica", "agendaMedica", "consultorio", "atiendeDesde","atiendeHasta","desDeHoraDeAlmuerzo","hastaHoraDeAlmuerzo","duracionCita","estadosProgramacioncitasMedicas")



@admin.register(EstadoRestriccionAgendas)
class estadoRestriccionAgendasAdmin(admin.ModelAdmin):
   list_display = ("id", "nombre")
   search_fields = ("id", "nombre")
   # Filtrar
   list_filter = ("id", "nombre")

@admin.register(AgendasMedicasRestriccionProgramacion)
class agendasMedicasRestriccionProgramacionAdmin(admin.ModelAdmin):
   list_display = ("id", "sedesClinica","agendasMedicasProgramacion","noAtiendeDesde","noAatiendeHasta","estadoRestriccionAgendas")
   search_fields = ("id", "sedesClinica__nombre","agendasMedicasProgramacion","noAtiendeDesde","noAatiendeHasta","estadoRestriccionAgendas")
   # Filtrar
   list_filter = ("id", "sedesClinica","agendasMedicasProgramacion","noAtiendeDesde","noAatiendeHasta","estadoRestriccionAgendas")

@admin.register(CitasMedicas)
class citasMedicasAdmin(admin.ModelAdmin):
   list_display = ("id", "sedesClinica","agendasMedicasProgramacion","admision","soatAccidente","furips","fechaReserva","fechaSolicitada","fechaAtencion")
   search_fields = ("id", "sedesClinica__nombre","agendasMedicasProgramacion","admision","soatAccidente","furips","fechaReserva","fechaSolicitada","fechaAtencion")
   # Filtrar
   list_filter = ("id", "sedesClinica","agendasMedicasProgramacion","admision","soatAccidente","furips","fechaReserva","fechaSolicitada","fechaAtencion")


@admin.register(CitasMedicasDetalle)
class citasMedicasDetalleAdmin(admin.ModelAdmin):
   list_display = ("id", "citasMedicas" )
   search_fields = ("id", "citasMedicas")
   # Filtrar
   list_filter = ("id", "citasMedicas")

@admin.register(CronologiaCitasMedicas)
class cronologiaCitasMedicasAdmin(admin.ModelAdmin):
   list_display = ("id", "citasMedicas","estadosCitasMedicas")
   search_fields = ("id", "citasMedicas","estadosCitasMedicas")
   # Filtrar
   list_filter = ("id", "citasMedicas","estadosCitasMedicas")

