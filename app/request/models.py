from django.db import models
from numpy import busday_count, is_busday
from business.models import Employee
from .validators import validate_start_end_date, validate_half_day
from django.urls import reverse
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


class RequestManager(models.Manager):

    def get_pending_requests(self):
        query = Request.objects.filter(status='pending')
        return query


class Request(models.Model):
    type = models.CharField(max_length=30, choices=REQUEST_TYPE_CHOICES)
    requested_by = models.ForeignKey(
        Employee, on_delete=models.SET_NULL, null=True, related_name='requestor')
    reviewed_by = models.ForeignKey(
        Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='approver')
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(null=True, blank=True)
    duration_type = models.CharField(
        choices=REQUEST_DURATION_CHOICES, max_length=10)
    status = models.CharField(
        choices=REQUEST_STATUS_CHOICES, max_length=20, default='pending')

    objects = RequestManager()

    @property
    def duration_in_business_days(self) -> float:
        if all([self.start_date == self.end_date, self.duration_type == 'half day']):
            return float(0.5)
        if self.start_date == self.end_date:
            return float(1)
        return busday_count(self.start_date, self.end_date)

    def __str__(self):
        return f'{self.requested_by} / {self.type} / {self.start_date} - {self.end_date} / {self.status}'

    def clean(self):
        if self.start_date and self.end_date:
            validate_start_end_date(self.start_date, self.end_date)
        if self.duration_type:
            validate_half_day(self.start_date, self.end_date,
                              self.duration_type)
        super(Request, self).clean()

    def get_absolute_url(self):
        return reverse("request-retrieve-update-destroy-view", kwargs={"pk": self.pk})
