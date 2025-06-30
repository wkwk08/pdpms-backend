from rest_framework import serializers
from .models import Document
from .models import CompletedDocument
from .models import OnGoingDocument

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'

class CompletedDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompletedDocument
        fields = '__all__'

class OnGoingDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnGoingDocument
        fields = '__all__'