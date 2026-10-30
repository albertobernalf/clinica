from rest_framework import serializers
from admisiones.models import Furips
from sitios.models import Departamentos, Municipios, Localidades, SedesClinica
from usuarios.models import TiposDocumento, Usuarios
from clinico.models import Diagnosticos , Ips, Servicios
from planta.models import Planta
from admisiones.models import Ingresos
from basicas.models import Eventos

class SedesClinicaSerializer(serializers.ModelSerializer):
    # Configuración clave para permitir nulos

    class Meta:
        model = SedesClinica
        fields = '__all__'

class TiposDocumentoSerializer(serializers.ModelSerializer):
    # Configuración clave para permitir nulos

    class Meta:
        model = TiposDocumento
        fields = '__all__'

class UsuariosSerializer(serializers.ModelSerializer):
    # Configuración clave para permitir nulos

    nombre_Paciente = serializers.CharField(source='nombre')

    class Meta:
        model = Usuarios
        #fields = '__all__'
        fields = ['id','nombre_Paciente']

#class IngresosSerializer(serializers.ModelSerializer):
    # Configuración clave para permitir nulos

#    class Meta:
#        model = Ingresos
#        fields = '__all__'

class EventosSerializer(serializers.ModelSerializer):
    # Configuración clave para permitir nulos

    class Meta:
        model = Eventos
        fields = '__all__'

class DepartamentosSerializer(serializers.ModelSerializer):
    # Configuración clave para permitir nulos

    class Meta:
        model = Departamentos
        fields = '__all__'

class MunicipiosSerializer(serializers.ModelSerializer):
    # Configuración clave para permitir nulos

    class Meta:
        model = Municipios
        fields = '__all__'

class LocalidadesSerializer(serializers.ModelSerializer):
    # Configuración clave para permitir nulos

    class Meta:
        model = Localidades
        fields = '__all__'

class DiagnosticosSerializer(serializers.ModelSerializer):
    # Configuración clave para permitir nulos

    class Meta:
        model = Diagnosticos
        fields = '__all__'


class IpsSerializer(serializers.ModelSerializer):
    # Configuración clave para permitir nulos

    class Meta:
        model = Ips
        fields = '__all__'



class PlantaSerializer(serializers.ModelSerializer):
        # Configuración clave para permitir nulos

    class Meta:
        model = Planta
        fields = '__all__'
        print("Cargue serializador")
        # read_only_fields = ('id','created_at')


class FuripsSerializer(serializers.ModelSerializer):
    # Configuración clave para permitir nulos

    class Meta:
        model = Furips
        fields = '__all__'
        print("Cargue serializador")
        # read_only_fields = ('id','created_at')

    def create(self, validated_data):
        # Extraemos datos adicionales pasados desde la vista (ej. el usuario que hace la petición)
        #usuario_operador = self.context.get('usuario_operador', 'Sistema')
        #validated_data['actualizado_por'] = usuario_operador

        # Creamos y retornamos el nuevo objeto en la base de datos
        print("Entre a guardar la actualizacion por serializers POS-PUT")
        #Furips.objects.create(**validated_data)
        #return "ok"

        return Furips.objects.create(**validated_data)

class ServiciosSerializer(serializers.ModelSerializer):

    # Configuración clave para permitir nulos

    servicioNombreIngSer = serializers.CharField(source='servicioNombreIng')

    class Meta:
        model = Servicios
        #fields = '__all__'
        fields = ['id','servicioNombreIngSer']
        print("Cargue serializador Servicios ")
        # read_only_fields = ('id','created_at')

class IngresosSerializer(serializers.ModelSerializer):
    # Configuración clave para permitir nulos

    documento = UsuariosSerializer(read_only=True)
    tipoDoc = TiposDocumentoSerializer(read_only=True)

    class Meta:
        model = Ingresos
        fields = '__all__'
        # fields = ['id','documento', 'tipoDoc','consec','fechaIngreso','salidaClinica']
        print("Cargue serializador Ingresos")
        # read_only_fields = ('id','created_at')

    def create(self, validated_data):
        # Extraemos datos adicionales pasados desde la vista (ej. el usuario que hace la petición)
        #usuario_operador = self.context.get('usuario_operador', 'Sistema')
        #validated_data['actualizado_por'] = usuario_operador

        # Creamos y retornamos el nuevo objeto en la base de datos
        print("Entre a guardar la actualizacion por serializers POS-PUT")
        #Furips.objects.create(**validated_data)
        #return "ok"

        return Ingresos.objects.create(**validated_data)


