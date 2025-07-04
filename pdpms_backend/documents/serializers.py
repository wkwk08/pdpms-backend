from rest_framework import serializers
from .models import Document
from .models import CompletedDocument
from .models import OnGoingDocument
from .models import ArchivedDocument

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.pdf_file:
            request = self.context.get('request')
            representation['pdf_file'] = request.build_absolute_uri(instance.pdf_file.url)
        return representation

class CompletedDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompletedDocument
        fields = '__all__'

class OnGoingDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnGoingDocument
        fields = '__all__'

class ArchivedDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArchivedDocument
        fields = '__all__'