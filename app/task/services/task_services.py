from task.models import Task, TaskLog
from task.serializers import TaskSerializer, TaskLogSerializer
from django.utils import timezone


class TaskService():
    
    @staticmethod
    def create_task(data):
        task = Task.objects.create(**data)
        return task
    
    @staticmethod
    def update_task(task, data):
        task_serializer = TaskSerializer(task, data=data, partial=True)
        if task_serializer.is_valid():
            task_serializer.save()
        return task
    
    @staticmethod
    def delete_task(task):
        task.delete()

    @staticmethod
    def get_task(task_id):
        try:
            task = Task.objects.get(id=task_id)
            return task
        except Task.DoesNotExist:
            return None
    
    @staticmethod
    def create_tasklog(data):
        tasklog = TaskLog.objects.create(**data)
        return tasklog
    
    @staticmethod
    def delete_tasklog(tasklog):
        tasklog.delete()

    @staticmethod
    def update_tasklog(tasklog, data):
        tasklog_serializer = TaskLogSerializer(tasklog, data=data, partial=True)
        if tasklog_serializer.is_valid():
            tasklog_serializer.save()
        return tasklog