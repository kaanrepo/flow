from django.core.exceptions import ValidationError

def validate_start_end_date(start_date, end_date):
    if start_date > end_date:
        raise ValidationError("End date cannot be earlier than the start date.")

def validate_half_day(start_date, end_date, duration):
    if  duration == 'half day' and start_date != end_date:
        raise ValidationError('Half days can be requested only same day requests.')
