from rest_framework import serializers
from .models import Property
from .models import ServiceableProperty

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'

class ServiceablePropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceableProperty
        fields = '__all__'