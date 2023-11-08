from rest_framework import permissions


class EmployeeEditPermission(permissions.BasePermission):

    ALLOWED_TO_EDIT_ROLES = ['GM', 'HR']

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.employee.position in self.ALLOWED_TO_EDIT_ROLES:
            return True
        return False
