from rest_framework import serializers
from .models import Propietario, Mascota, ConsultaVeterinaria


class PropietarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Propietario
        fields = '__all__'


class MascotaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mascota
        fields = '__all__'

    def validate_nombre(self, value):
        nombre = value.strip()

        if not nombre:
            raise serializers.ValidationError(
                'El nombre de la mascota es obligatorio.'
            )

        return nombre

    def validate_peso(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                'El peso de la mascota debe ser mayor que cero.'
            )

        return value


class ConsultaVeterinariaSerializer(serializers.ModelSerializer):

    class Meta:
        model = ConsultaVeterinaria
        fields = '__all__'

    def validate_motivo(self, value):
        motivo = value.strip()

        if not motivo:
            raise serializers.ValidationError(
                'El motivo de la consulta es obligatorio.'
            )

        return motivo

    def validate_costo(self, value):
        if value < 0:
            raise serializers.ValidationError(
                'El costo de la consulta no puede ser negativo.'
            )

        return value
