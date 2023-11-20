import json

from channels.generic.websocket import AsyncWebsocketConsumer
from task.services.task_services import TaskService, TaskLogService
from asgiref.sync import sync_to_async

class TaskConsumer(AsyncWebsocketConsumer):

    task_service = TaskService()

    async def connect(self):
        user = self.scope['user']
        self.socket_name = f'task-{user.id}'
        await self.channel_layer.group_add(self.socket_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.socket_name, self.channel_name)
        await self.close()

    async def receive(self, data):
        data = json.loads(data)
        task_id = data.get('task_id')
        task = self.task_service.get_task(task_id)
        action = data.get('task_action')
        if action == 'create':
            new_task = await self.task_service.create_task(data)
            await self.channel_layer.group_send(self.socket_name, {'type': 'task.created', 'task_id': new_task.id})
        if action == 'delete':
            await self.task_service.delete_task(task)
            await self.channel_layer.group_send(self.socket_name, {'type': 'task.deleted'})
        if action == 'update':
            await self.task_service.update_task(task, data)
            await self.channel_layer.group_send(self.socket_name, {'type': 'task.updated', 'task_id': task_id})

    async def task_created(self, event):
        task_id = event['task_id']
        await self.send(text_data=json.dumps({
            'task_id': task_id,
            'status': 'created'
        }))

    async def task_deleted(self, event):
        await self.send(text_data=json.dumps({
            'status': 'deleted'
        }))

    async def task_updated(self, event):
        task_id = event['task_id']
        await self.send(text_data=json.dumps({
            'task_id': task_id,
            'status': 'updated'
        }))

class TaskLogConsumer(AsyncWebsocketConsumer):

    tasklog_service = TaskLogService()

    async def connect(self):
        user = self.scope['user']
        self.socket_name = f'tasklog-{user.id}'
        await self.channel_layer.group_add(self.socket_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.socket_name, self.channel_name)
        await self.close()

    async def receive(self, text_data):
        data = json.loads(text_data)
        tasklog_id = data.get('tasklog_id')
        if tasklog_id:
            tasklog = await sync_to_async(self.tasklog_service.get_tasklog)(tasklog_id)
        action = data.get('task_action')
        serializer_data = {}
        serializer_keys = ['task', 'employee', 'date', 'duration']
        for key in data:
            if key in serializer_keys:
                serializer_data[key] = data[key]
        if action == 'create':
            new_tasklog = await sync_to_async(self.tasklog_service.create_tasklog)(serializer_data)
            await self.channel_layer.group_send(self.socket_name, {'type': 'tasklog.created', 'task_id': new_tasklog.id})
        if action == 'update':
            updated_tasklog = await sync_to_async(self.tasklog_service.update_tasklog)(tasklog, serializer_data)
            await self.channel_layer.group_send(self.socket_name, {'type': 'tasklog.updated', 'task_id': updated_tasklog.id})
        if action == 'delete':
            await sync_to_async(self.tasklog_service.delete_tasklog)(tasklog)
            await self.channel_layer.group_send(self.socket_name, {'type': 'tasklog.deleted'})

    async def tasklog_created(self, event):
        task_id = event['task_id']
        await self.send(text_data=json.dumps({
            'task_id': task_id,
            'status': 'created'
        }))
    async def tasklog_updated(self, event):
        task_id = event['task_id']
        await self.send(text_data=json.dumps({
            'task_id': task_id,
            'status': 'updated'
        }))
    async def tasklog_deleted(self, event):
        await self.send(text_data=json.dumps({
            'status': 'deleted'
        }))