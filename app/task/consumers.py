import json

from channels.generic.websocket import AsyncWebsocketConsumer
from task.services.task_services import TaskService

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

    tasklog_service = TaskService()

    async def connect(self):
        user = self.scope['user']
        self.socket_name = f'tasklog-{user.id}'
        await self.channel_layer.group_add(self.socket_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.socket_name, self.channel_name)
        await self.close()

    async def receive(self, data):
        data = json.loads(data)
        task_id = data.get('task_id')
        task = self.tasklog_service.get_task(task_id)
        action = data.get('task_action')
        if action == 'create':
            new_tasklog = await self.tasklog_service.create_tasklog(data)
            await self.channel_layer.group_send(self.socket_name, {'type': 'tasklog.created', 'task_id': new_tasklog.id})

    async def tasklog_created(self, event):
        task_id = event['task_id']
        await self.send(text_data=json.dumps({
            'task_id': task_id,
            'status': 'created'
        }))