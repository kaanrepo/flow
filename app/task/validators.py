from django.core.exceptions import ValidationError

def validate_task_participant(task, employee):
    if employee not in task.participants.all():
        raise ValidationError(f'{employee} is not a participant of this task.')