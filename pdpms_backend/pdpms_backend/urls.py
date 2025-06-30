"""
URL configuration for pdpms_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from activity_logs.views import ActivityLogViewSet
from documents.views import DocumentViewSet
from documents.views import OnGoingDocumentViewSet
from documents.views import CompletedDocumentViewSet
from documents.views import ArchivedDocumentViewSet
from employees.views import EmployeeViewSet
from properties.views import PropertyViewSet
from properties.views import ServiceablePropertyViewSet
from properties.views import UnserviceablePropertyViewSet
from users.views import UserViewSet

router = DefaultRouter()
router.register(r'activity-logs', ActivityLogViewSet)
router.register(r'documents', DocumentViewSet)
router.register(r'ongoing-documents', OnGoingDocumentViewSet)
router.register(r'completed-documents', CompletedDocumentViewSet)
router.register(r'archived-documents', ArchivedDocumentViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'properties', PropertyViewSet)
router.register(r'serviceable-properties', ServiceablePropertyViewSet)
router.register(r'unserviceable-properties', UnserviceablePropertyViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pdpms/manila-city-hall/', include(router.urls)),
]
