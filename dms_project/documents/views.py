from rest_framework import generics, permissions
from .models import Document
from .serializers import DocumentSerializer
from rest_framework.viewsets import ModelViewSet
from .permissions import DocumentPermission
from accounts.permissions import can_edit_document , can_view_document


class EmployeeDocumentView(generics.ListCreateAPIView):
    serializer_class = DocumentSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Document.objects.filter(created_by = self.request.user)
    
    def perform_create(self , serializer):
        serializer.save(created_by = self.request.user)
        
    
class DocumentViewSet(ModelViewSet):
    serializer_class = DocumentSerializer
    permission_classes = [permissions.IsAuthenticated, DocumentPermission]

    def get_queryset(self):
        user = self.request.user
        queryset = Document.objects.all()

        # IMPORTANT: filter documents based on permission
        return [doc for doc in queryset if can_view_document(user, doc)]