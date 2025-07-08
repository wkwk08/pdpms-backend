from django.urls import path

from .views import DocumentStatusView, PropertyStatusView

urlpatterns = [
    path('document-status/', DocumentStatusView.as_view(), name='dashboard-document-status'),
    path('property-status/', PropertyStatusView.as_view(), name='dashboard-property-status'),
]
