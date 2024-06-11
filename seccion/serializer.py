from rest_framework import serializers
from .models import Seccion

class SeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seccion
        fields = '__all__'