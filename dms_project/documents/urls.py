from django.urls import path
from .views import EmployeeDocumentView

urlpatterns = [
    path('docs/' , EmployeeDocumentView.as_view() , name='document')
]
