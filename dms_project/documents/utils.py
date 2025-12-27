# documents/utils.py

def can_view(user, document):
    if user.is_superuser:
        return True
    if user.groups.filter(name='manager').exists():
        return True
    if document.permissions.filter(user=user, permission="view").exists():
        return True
    if document.created_by == user:
        return True
    return False

def can_edit(user, document):
    if user.is_superuser:
        return True
    if user.groups.filter(name='manager').exists():
        return True
    if document.permissions.filter(user=user, permission="edit").exists():
        return True
    return False
