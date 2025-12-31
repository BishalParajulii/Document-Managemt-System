from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import DocumentSerializer , DocumentContentSerializer
from .permissions import DocumentPermission
from .models import Document , DocumentContent
from accounts.permissions import can_edit_document , can_view_document
from rest_framework.generics import ListAPIView , RetrieveUpdateAPIView
from .permissions import DocumentPermission

class DocumentViewSet(ModelViewSet):
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated, DocumentPermission]

    def get_queryset(self):
        return Document.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        allowed_docs = [
            doc for doc in queryset
            if can_view_document(request.user, doc)
        ]
        serializer = self.get_serializer(allowed_docs, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        doc = serializer.save(created_by = self.request.user)
        DocumentContent.objects.create(document=doc , content="")


class MyDocumentView(ListAPIView):
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Document.objects.filter(created_by=self.request.user)
    
    
class DocumentContentView(RetrieveUpdateAPIView):
    serializer_class = DocumentContentSerializer
    permission_classes = [IsAuthenticated , DocumentPermission]
    
    def get_queryset(self):
        return DocumentContent.objects.all()
    
    def perform_update(self):
        serializer.save(last_edited_by=self.request.user)
