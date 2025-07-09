from django.shortcuts import render
from rest_framework import viewsets
from .models import Property
from .serializers import PropertySerializer
from .models import ServiceableProperty
from .serializers import ServiceablePropertySerializer
from .models import UnserviceableProperty
from .serializers import UnserviceablePropertySerializer
from .models import ForRepairProperty
from .serializers import ForRepairPropertySerializer
from .models import CondemnedProperty
from .serializers import CondemnedPropertySerializer

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    lookup_field = 'property_no' # Use property_no as the lookup field

class ServiceablePropertyViewSet(viewsets.ModelViewSet):
    queryset = ServiceableProperty.objects.all()
    serializer_class = ServiceablePropertySerializer

class UnserviceablePropertyViewSet(viewsets.ModelViewSet):
    queryset = UnserviceableProperty.objects.all()
    serializer_class = UnserviceablePropertySerializer

class ForRepairPropertyViewSet(viewsets.ModelViewSet):
    queryset = ForRepairProperty.objects.all()
    serializer_class = ForRepairPropertySerializer

class CondemnedPropertyViewSet(viewsets.ModelViewSet):
    queryset = CondemnedProperty.objects.all()
    serializer_class = CondemnedPropertySerializer