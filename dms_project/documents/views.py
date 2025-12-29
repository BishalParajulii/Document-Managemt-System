from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import DocumentSerializer
from .permissions import DocumentPermission
from .models import Document
from accounts.permissions import can_edit_document , can_view_document

class DocumentViewSet(ModelViewSet):
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated, DocumentPermission]

    def get_queryset(self):
        # DO NOT FILTER HERE
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
        serializer.save(created_by=self.request.user)
