from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='task-detail-view',
        lookup_field='uuid'
    )

    class Meta:
        model = Task
        fields = '__all__'
