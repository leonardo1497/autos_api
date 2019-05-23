from .models import Auto
from rest_framework import serializers

class AutoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Auto
        fields = ('__all__')
