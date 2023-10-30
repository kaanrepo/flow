from rest_framework import generics, mixins, permissions
from .models import Request
from .serializers import RequestSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def request_list_api_view(request, uuid, *args, **kwargs):
    qs = Request.objects.all().filter(uuid=uuid).order_by(status='pending')
    serialized_data = RequestSerializer(data=qs, many=True)
    return Response(serialized_data, status=200)
