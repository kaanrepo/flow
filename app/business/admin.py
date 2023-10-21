from django.contrib import admin
from .models import Employee, Team, Customer

# Register your models here.

admin.site.register(Employee)
admin.site.register(Team)
admin.site.register(Customer)