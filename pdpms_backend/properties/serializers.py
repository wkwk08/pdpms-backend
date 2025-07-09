from rest_framework import serializers
from .models import Property
from .models import ServiceableProperty
from .models import UnserviceableProperty
from .models import ForRepairProperty
from .models import CondemnedProperty

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'
        extra_kwargs = {
            'property_no': {'required': False},  # Not required in POST since trigger sets it
            'serial_no': {'required': False, 'allow_blank': True, 'allow_null': True},
            'unit_cost': {'required': False, 'allow_null': True},
            'estimated_life_use': {'required': False, 'allow_null': True},
        }

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

class CondemnedPropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = CondemnedProperty
        fields = '__all__'