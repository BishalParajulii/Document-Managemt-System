from rest_framework import serializers
from .models import Document , DocumentContent
from django.contrib.auth.hashers import make_password

class DocumentSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source="created_by.username" , read_only = True)
    password = serializers.CharField(write_only=True, required=False , allow_blank = True)
    is_locked = serializers.BooleanField(read_only=True)
    
    class Meta:
        model = Document
        fields = ['id' , 'title' , 'file' , 'created_at' , 'created_by' , 'password' , 'is_locked']
        read_only_fields = ['id' , 'created_at' , 'created_by' , 'is_locked']
        
    def create(self, validated_data):
        password = validated_data.pop("password" , None)
        doc = Document.objects.create(**validated_data)
        
        if password:
            doc.locked_password = make_password(password)
            doc.save()
            
        return doc
        
        
class DocumentContentSerializer(serializers.ModelSerializer):
    document = serializers.CharField(source="document.title" , read_only = True)
    updated_at = serializers.DateTimeField(
        format = "%Y-%m-%d %H:%M:%S",
        read_only = True
    )
    last_edited_by = serializers.CharField(source="last_edited_by.username" , read_only = True)
    class Meta:
        model = DocumentContent
        fields = ['id' , 'document' , 'content' , 'last_edited_by' , 'updated_at']
        read_only_fields = ['last_edited_by' , 'updated_at']