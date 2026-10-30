from django.contrib import admin

# Register your models here.


from admisiones.models import Ingresos, Furips


@admin.register(Ingresos)
class ingresosAdmin(admin.ModelAdmin):

    list_display=("id","sedesClinica","tipoDoc","documento","consec","fechaIngreso","fechaSalida","dependenciasActual","salidaClinica","especialidadesMedicosActual")
    search_fields =("id","sedesClinica__nombre","tipoDoc__nombre","documento","consec","fechaIngreso","fechaSalida","dependenciasActual__nombre","salidaClinica","especialidadesMedicosActual")

@admin.register(Furips)
class furipsAdmin(admin.ModelAdmin):


    list_display=("id","sedesClinica","tipoDoc","documento","consec","admision","primerNombreVictima","segundoNombreVictima","primerApellidoVictima","segundoApellidoVictima")
    search_fields = ("id","sedesClinica","tipoDoc","documento","consec","admision","primerNombreVictima","segundoNombreVictima","primerApellidoVictima","segundoApellidoVictima")


