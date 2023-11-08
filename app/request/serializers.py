from rest_framework import serializers
from .models import Request

class RequestSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name='request-retrieve-update-destroy-view', lookup_field='pk')

    class Meta:
        model = Request
        fields = [
            'url',
            'type',
            'requested_by',
            'reviewed_by',
            'start_date',
            'end_date',
            'duration_type',
            'duration',
            'status'
        ]
