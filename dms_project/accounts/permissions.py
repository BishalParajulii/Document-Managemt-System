from django.contrib.auth.models import Group

def is_employee(user):
    return user.groups.filter(name="employee").exists()

def is_manager(user):
    return user.groups.filter(name="manager").exists()

def is_hr(user):
    return user.groups.filter(name="hr").exists()

def is_admin(user):
    return user.is_superuser or user.groups.filter(name="admin").exists()


def can_view_document(user, document):
    if not user:
        return False
    
    if not document.created_by:
        return False
    
    uploader = document.created_by
    
    if is_admin(user):
        return True
    
    if user == uploader:
        return True
    
    if is_employee(uploader) :
        return True
    
    if is_manager(uploader):
        return is_manager(user) or is_hr(user)
    
    if is_hr(uploader):
        return is_manager(user) or is_hr(user)
    
    return False    


def can_edit_document(user, document):
    if not user:
        return False
    
    if not document.created_by:
        return False
    
    uploader = document.created_by
    
    if is_admin(user):
        return True

    if user == uploader:
        return True

    uploader = document.created_by

    if is_employee(uploader):
        return is_manager(user) or is_hr(user)

    return False
