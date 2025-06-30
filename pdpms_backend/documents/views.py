from django.shortcuts import render
from rest_framework import viewsets
from .models import Document
from .serializers import DocumentSerializer
from .models import CompletedDocument
from .serializers import CompletedDocumentSerializer
from .models import OnGoingDocument
from .serializers import OnGoingDocumentSerializer
from .models import ArchivedDocument
from .serializers import ArchivedDocumentSerializer

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class CompletedDocumentViewSet(viewsets.ModelViewSet):
    queryset = CompletedDocument.objects.all()
    serializer_class = CompletedDocumentSerializer

class OnGoingDocumentViewSet(viewsets.ModelViewSet):
    queryset = OnGoingDocument.objects.all()
    serializer_class = OnGoingDocumentSerializer

class ArchivedDocumentViewSet(viewsets.ModelViewSet):
    queryset = ArchivedDocument.objects.all()
    serializer_class = ArchivedDocumentSerializer