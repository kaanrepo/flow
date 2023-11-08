from task.models import Task
from task.serializers import TaskSerializer


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