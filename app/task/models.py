from django.db import models
from business.models import Employee
from .validators import validate_task_participant

# Create your models here.

STATUS_CHOICES = [
    ('open', 'Open'),
    ('closed', 'Closed'),
]

TASK_TYPE_CHOICES = [
    ('meeting/call', 'Meeting/Call'),
    ('support', 'Support'),
    ('customer_management', 'Customer Mgt'),
    ('project', 'Project'),
    ('report', 'Report')
]


class Task(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    customer = models.ForeignKey('business.customer', on_delete=models.SET_NULL, null=True, blank=True)
    department = models.CharField(max_length=20, null=False, blank=False)
    type = models.CharField(max_length=20, null=False, blank=False, choices=TASK_TYPE_CHOICES)
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=10, null=False, blank=False, default='open')
    created_at = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='created_tasks')
    participants = models.ManyToManyField(Employee, related_name='related_tasks', blank=True)

    def __str__(self):
        if self.customer:
            return f' {self.customer.name}/ {self.name}'
        return self.name
    
    def __repr__(self) -> str:
        return super().__str__()
    

class TaskLog(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True )
    date = models.DateField(null=False, blank=False)
    duration = models.DurationField(null=True, blank=True)

    def clean(self) -> None:
        validate_task_participant(self.task, self.employee)
        return super().clean()
    
    def __str__(self):
        return f'{self.task.name} - {self.employee.name} - {self.date} - {self.duration}'