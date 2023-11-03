from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Request

class RequestSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name='request-retrieve-update-destroy-view', lookup_field='uuid')

    class Meta:
        model = Request
        fields = [
            'url',
            'type',
            'requested_by',
            'reviewed_by',
            'start_date',
            'end_date',
            'description',
            'duration',
            'status'
        ]
