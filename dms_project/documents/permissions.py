from rest_framework.permissions import BasePermission
from accounts.permissions import can_edit_document, can_view_document

class DocumentPermission(BasePermission):
    
    def has_object_permission(self , request , view , obj):
        
        if request.method in ['GET']:
            return can_view_document(request.user , obj)
        
        if request.method in ['PUT' , 'PATCH' , 'DELETE' ]:
            return can_edit_document(request.user , obj)
        
        return False