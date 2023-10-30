from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Request

class RequestSerializer(serializers.Serializer):

    class Meta:
        model = Request
        fields = [
            'type',
            'requested_by',
            'reviewed_by',
            'start_date',
            'end_date',
            'description',
            'duration',
            'status'
        ]
