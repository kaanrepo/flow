from request.models import Request
from request.serializers import RequestSerializer


class RequestService():

    @staticmethod
    def create_request(data):
        request = Request.objects.create(**data)
        return request

    @staticmethod
    def update_request(request, data):
        request_serializer = RequestSerializer(
            request, data=data, partial=True)
        if request_serializer.is_valid():
            request_serializer.save()
        return request

    @staticmethod
    def delete_request(request):
        request.delete()

    @staticmethod
    def approve_request(request, reviewed_by):
        request.status = 'approved'
        request.reviewed_by = reviewed_by
        request.save()

    @staticmethod
    def deny_request(request, reviewed_by):
        request.status = 'denied'
        request.reviewed_by = reviewed_by
        request.save()