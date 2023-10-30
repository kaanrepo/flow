from django.db import models
from business.models import Employee
import uuid

# Create your models here.

STATUS_CHOICES = [
    ('open', 'Open'),
    ('closed', 'Closed'),
]

# CUSTOMER_CHOICES = [
#     ('af', 'AF'),
#     ('af it', 'AF IT'),
#     ('afkl', 'AFKL'),
#     ('ams/bi', 'AMS/BI'),
#     ('ams/cx', 'AMS/CX'),
#     ('ams/sz', 'AMS/SZ'),
#     ('cargo', 'Cargo'),
#     ('cargo_ops', 'Cargo Ops.'),
#     ('flying_blue', 'Flying Blue'),
#     ('kl', 'KL'),
#     ('klc', 'KLC'),
#     ('medeam', 'Medeam'),
#     ('ndc', 'NDC'),
#     ('ota', 'OTA'),
#     ('skyteam', 'Skyteam'),
#     ('transavia_hv', 'Transavia HV'),
#     ('transavio_to', 'Transavia TO'),
# ]

TASK_TYPE_CHOICES = [
    ('meeting/call', 'Meeting/Call'),
    ('support', 'Support'),
    ('customer_management', 'Customer Mgt'),
    ('project', 'Project'),
    ('report', 'Report')
]


class Task(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=50, null=False, blank=False)
    #customer = models.CharField(max_length=20, null=False, blank=False)
    customer = models.ForeignKey('business.customer', on_delete=models.SET_NULL, null=True, blank=True)
    area = models.CharField(max_length=20, null=False, blank=False)
    subarea_department = models.CharField(max_length=20, null=False, blank=False)
    type = models.CharField(max_length=20, null=False, blank=False, choices=TASK_TYPE_CHOICES)
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=10, null=False, blank=False, default='open')
    created_at = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(Employee, on_delete=models.CASCADE)
    participants = models.ManyToManyField(Employee, related_name='related_tasks', blank=True)

    def __str__(self):
        if self.customer:
            return f' {self.customer.name}/ {self.name}'
        return self.name
    
    def __repr__(self) -> str:
        return super().__str__()
    

class TaskLog(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=False, blank=False)
    date = models.DateField(null=False, blank=False)
    duration = models.DurationField(null=True, blank=True)