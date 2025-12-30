from rest_framework.permissions import BasePermission , SAFE_METHODS
from accounts.permissions import can_edit_document, can_view_document

class DocumentPermission(BasePermission):
    
    def has_permission(self , request , view):
        return request.user.is_authenticated and request.user
    
    def has_object_permission(self , request , view , obj):
        
        if request.method in SAFE_METHODS:
            return can_view_document(request.user , obj)
        
        if request.method in ['PUT' , 'PATCH' , 'DELETE' ]:
            return can_edit_document(request.user , obj)
        
        return False