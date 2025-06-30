from rest_framework import serializers
from .models import Property
from .models import ServiceableProperty
from .models import UnserviceableProperty
from .models import ForRepairProperty

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'

class ServiceablePropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceableProperty
        fields = '__all__'

class UnserviceablePropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = UnserviceableProperty
        fields = '__all__'

class ForRepairPropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = ForRepairProperty
        fields = '__all__'