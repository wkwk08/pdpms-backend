from rest_framework import serializers
from .models import Document
from .models import CompletedDocument
from .models import OnGoingDocument
from .models import ArchivedDocument

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'
        read_only_fields = ['document_id']
        extra_kwargs = {
            'reference_code': {'required': True, 'allow_blank': False},
            'subject': {'required': True, 'allow_blank': False},
            'document_type': {'required': True, 'allow_blank': False},
            'document_date': {'required': True},
            'date_received': {'required': True},
            'received_by': {'required': True, 'allow_blank': False},
            'document_status': {'required': True, 'allow_blank': False},
            'remarks': {'required': False, 'allow_blank': True},
            'pdf_file': {'required': False, 'allow_null': True},
            'base_document_id': {'required': False, 'allow_blank': True, 'allow_null': True},
        }       

    def validate_document_type(self, value):
        valid_types = ['Memorandums', 'Endorsements', 'Dispositions', 'Request Letters', 'Special Orders', 'Employee Documents', 'Others', 'Property Records']
        if value not in valid_types:
            raise serializers.ValidationError(f"Invalid document type. Must be one of: {', '.join(valid_types)}")
        return value
    
    def validate_document_status(self, value):
        valid_statuses = ['Ongoing', 'Completed', 'Archived']
        if value not in valid_statuses:
            raise serializers.ValidationError(f"Invalid status. Must be one of: {', '.join(valid_statuses)}")
        return value

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