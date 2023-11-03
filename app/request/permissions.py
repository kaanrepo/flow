from rest_framework import permissions

class RequestEditPermission(permissions.BasePermission):

    ROLES_ALLOWED_TO_EDIT = ['TC', 'TL', 'HR']
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if all([obj.status == 'pending', request.user.employee == obj.requested_by]):
            return True
        
        if request.user.employee.position in self.ROLES_ALLOWED_TO_EDIT:
            return True