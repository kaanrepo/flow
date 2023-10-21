from django.db import models
from numpy import busday_count, is_busday
from employee.models import Employee

# Create your models here.

REQUEST_TYPE_CHOICES = [
    ('working from office', 'Working from Office'),
    ('remote working', 'Remote Working'),
    ('holiday', 'Holiday'),
    ('sick leave without report', 'Sick leave without report'),
    ('sick leave with report', 'Sick leave with report'),
    ('marriage', 'Marriage'),
    ('childbirth of wife', 'Childbirth of wife'),
    ('funeral 1st degree', 'Funeral 1st degree'),
]

REQUEST_DURATION_CHOICES = [
    ('half day', 'Half Day'),
    ('full day', 'Full Day')
]
REQUEST_STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('approved', 'Approved'),
    ('denied', 'Denied')
]

class Request(models.Model):
    type = models.CharField(max_length=30, choices=REQUEST_TYPE_CHOICES)
    requested_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='requestor')
    assigned_to = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='approver')
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(null=True, blank=True)
    duration = models.CharField(choices=REQUEST_DURATION_CHOICES, max_length=10)
    status = models.CharField(choices=REQUEST_STATUS_CHOICES, max_length=20, default='pending')

    @property
    def duration_in_business_days(self) -> int:
        if self.start_date == self.end_date:
            return int(1)
        return busday_count(self.start_date, self.end_date)