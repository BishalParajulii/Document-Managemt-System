from rest_framework import serializers
from .models import Document , DocumentContent

class DocumentSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source="created_by.username" , read_only = True)
    class Meta:
        model = Document
        fields = ['id' , 'title' , 'file' , 'created_at' , 'created_by']
        read_only_fields = ['id' , 'created_at']
        
        
class DocumentContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentContent
        fields = ['id' , 'document' , 'content' , 'last_edited_by' , 'updated_at']
        read_only_fields = ['last_edited_by' , 'updated_at']