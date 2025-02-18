from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from features.models import Event
from features.serializers import EventSerializer

class EventListCreateView(APIView):
    def get(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EventDetailView(APIView):
    def get(self, request, pk):
        try:
            event = Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = EventSerializer(event)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            event = Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            event = Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
