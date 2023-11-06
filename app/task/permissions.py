from rest_framework import permissions

class TaskUpdateDeletePermission(permissions.BasePermission):

    def has_permission(self, request, view,):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if request.user.employee.position == 'agent':
            return False