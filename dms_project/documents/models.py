from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Document(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to="documents/" , blank=True , null=True)
    
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="created_document")
    
    is_locked = models.BooleanField(default=False)
    locked_password = models.CharField(max_length=100, blank=True , help_text="Hashed password for locked documents")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

    
class DocumentContent(models.Model):
    document = models.OneToOneField(Document, on_delete=models.CASCADE, related_name="content")
    content = models.TextField()
    last_edited_by = models.ForeignKey(User, on_delete=models.SET_NULL , null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"content of {self.document.title}"

    
    
    
class DocumentPermission(models.Model):
    VIEW = "view"
    EDIT = "edit"
    
    PERMISSION_CHOICES = [
        (VIEW, "view"),
        (EDIT, "edit")
    ]
    
    document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name="permissions")
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="document_permissions")
    
    permission = models.CharField(max_length=10, choices=PERMISSION_CHOICES)
    
    granted_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="granted_permissions", null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ("document", "user", "permission")
        
    def __str__(self):
        return f"{self.user} -> {self.permission} -> {self.document}"
