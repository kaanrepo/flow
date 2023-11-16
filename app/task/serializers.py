from rest_framework import serializers
from .models import Task, TaskLog


class TaskSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='task-detail-view',
        lookup_field='pk'
    )

    class Meta:
        model = Task
        fields = '__all__'


class TaskLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = TaskLog
        fields = '__all__'