from rest_framework import serializers
from .models import Document
from .models import CompletedDocument

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'

class CompletedDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompletedDocument
        fields = '__all__'