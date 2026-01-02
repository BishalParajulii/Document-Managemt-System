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
    if not user or not document:
        return False

    uploader = document.created_by

    if is_admin(user):
        return True

    if is_employee(user):
        return uploader == user

    if is_hr(user) or is_manager(user):
        if is_employee(uploader):
            return True
        
        if is_admin(uploader):
            return False

        if (is_manager(user) and is_hr(uploader)) or (is_hr(user) and is_manager(uploader)):
            return True

    return False
   


def can_edit_document(user, document):
    if not user or not document:
        return False

    uploader = document.created_by

    
    if is_admin(user):
        return True

    
    if is_employee(user):
        return uploader == user


    if is_hr(user) or is_manager(user):
        
        if is_employee(uploader):
            return True
        
        if is_admin(uploader):
            return False
        
        if (is_manager(user) and is_hr(uploader)) or (is_hr(user) and is_manager(uploader)):
            return True

    return False

