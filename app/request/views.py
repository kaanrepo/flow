from rest_framework import generics, status
from .models import Request
from .serializers import RequestSerializer
from rest_framework.response import Response
from .permissions import RequestEditPermission


class RequestListCreateView(generics.ListCreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    authentication_classes = []
    permission_classes = ()
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RequestRetrieveUpdateDestroyView(generics.RetrieveAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    authentication_classes = []
    permission_classes = ()
    lookup_field = 'uuid'

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, context={'request': request}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class EmployeeRequestListView(generics.ListAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        uuid = self.kwargs['uuid']
        return qs.filter(participants__uuid=uuid)
    