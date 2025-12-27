from django.contrib import admin
from .models import Document,DocumentContent, DocumentPermission


# Register your models here.
admin.register(Document)
admin.register(DocumentPermission)
admin.register(DocumentContent)