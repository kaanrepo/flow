from .models import Employee
from celery import shared_task
from django.utils import timezone


@shared_task
def check_employee_allocation_renewal():
    today = timezone.now().date()
    employees = Employee.objects.all()
    for employee in employees:
        if employee.contract_start.month == today.month and employee.contract_start.day == today.day:
            employee.allocation_balance += employee.yearly_allocation
            employee.last_allocation_update = today
            employee.save()



@shared_task
def check_employee_birthday():
    today = timezone.now().date()
    employees = Employee.objects.all()
    for employee in employees:
        if employee.birthday.month == today.month and employee.birthday.day == today.day:
            pass
            ### send email to employee/office