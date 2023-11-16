import json

from channels.generic.websocket import AsyncWebsocketConsumer
from request.services.request_services import RequestService


class RequestConsumer(AsyncWebsocketConsumer):

    request_service = RequestService()

    async def connect(self):
        user = self.scope['user']
        self.socket_name = f'request-{user.id}'
        await self.channel_layer.group_add(self.socket_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.socket_name, self.channel_name)
        await self.close()

    async def receive(self, data):
        data = json.loads(data)
        request_id = data.get('request_id')
        request = self.request_service.get_request(request_id)
        action = data.get('request_action')
        if action == 'approve':
            await self.request_service.approve_request(request, self.user.employee)
            await self.channel_layer.group_send(self.socket_name, {'type': 'request.approved', 'request_id': request_id})
        if action == 'deny':
            await self.request_service.deny_request(request, self.user.employee)
            await self.channel_layer.group_send(self.socket_name, {'type': 'request.denied', 'request_id': request_id})
        if action == 'delete':
            await self.request_service.delete_request(request)
            await self.channel_layer.group_send(self.socket_name, {'type': 'request.deleted', 'request_id': request_id})
        if action == 'update':
            await self.request_service.update_request(request, data)

    async def request_approved(self, event):
        request_id = event['request_id']
        await self.send(text_data=json.dumps({
            'request_id': request_id,
            'status': 'approved'
        }))

    async def request_denied(self, event):
        request_id = event['request_id']
        await self.send(text_data=json.dumps({
            'request_id': request_id,
            'status': 'denied'
        }))

    async def request_deleted(self, event):
        request_id = event['request_id']
        await self.send(text_data=json.dumps({
            'request_id': request_id,
            'status': 'deleted'
        }))
