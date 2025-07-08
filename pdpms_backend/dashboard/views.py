from rest_framework.response import Response
from rest_framework.views import APIView

from documents.models import Document, OnGoingDocument, CompletedDocument
from properties.models import (
    Property,
    ServiceableProperty,
    UnserviceableProperty,
    ForRepairProperty,
    CondemnedProperty,
)

class DocumentStatusView(APIView):
    """
    Provides a summary of document statuses for the dashboard.
    """
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        total_docs = Document.objects.count()
        complete = CompletedDocument.objects.count()
        in_progress = OnGoingDocument.objects.count()
        not_started = Document.objects.filter(document_status__iexact='Not Started').count()
        pending = Document.objects.filter(document_status__iexact='Pending').count()

        from documents.models import ArchivedDocument
        archived = ArchivedDocument.objects.count()

        data = {
            "complete": complete,
            "inProgress": in_progress,
            "archived": archived,
            "notStarted": not_started,
            "pending": pending,
            "total": total_docs,
        }
        return Response(data)


class PropertyStatusView(APIView):
    """
    Provides a summary of property statuses for the dashboard.
    """
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        total_properties = Property.objects.count()
        
        statuses = [
            {"model": ServiceableProperty, "label": "Serviceable"},
            {"model": UnserviceableProperty, "label": "Unserviceable"},
            {"model": ForRepairProperty, "label": "For Repair"},
            {"model": CondemnedProperty, "label": "Condemned"},
        ]
        
        response_data = []
        for status_info in statuses:
            count = status_info["model"].objects.count()
            percentage = round((count / total_properties) * 100) if total_properties > 0 else 0
            response_data.append({
                "status": status_info["label"],
                "count": count,
                "percentage": percentage
            })
            
        return Response(response_data)
