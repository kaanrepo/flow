from django.db import models
from employee.models import Employee

# Create your models here.

STATUS_CHOICES = [
    ("new", 'New'),
    ('open', 'Open'),
    ('closed', 'Closed'),
]

class Task(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    customer = models.CharField(max_length=20, null=False, blank=False)
    area = models.CharField(max_length=20, null=False, blank=False)
    subarea_department = models.CharField(max_length=20, null=False, blank=False)
    type = models.CharField(max_length=10, null=False, blank=False)
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=10, null=False, blank=False)
    created_at = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(Employee, on_delete=models.CASCADE)
    participants = models.ManyToManyField(Employee, related_name='participants', blank=True)


class TaskLog(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=False, blank=False)
    date = models.DateField(null=False, blank=False)
    duration = models.DurationField(null=True, blank=True)