from rest_framework import generics, permissions
from .models import Document
from .serializers import DocumentSerializer


class EmployeeDocumentView(generics.ListCreateAPIView):
    serializer_class = DocumentSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Document.objects.filter(created_by = self.request.user)
    
    def perform_create(self , serializer):
        serializer.save(created_by = self.request.user)
        
    