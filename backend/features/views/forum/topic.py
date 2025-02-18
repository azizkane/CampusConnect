from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ...models import Topic
from ...serializers import TopicSerializer

class TopicListCreateView(APIView):
    def get(self, request):
        topics = Topic.objects.all()
        serializer = TopicSerializer(topics, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TopicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TopicDetailView(APIView):
    def get(self, request, pk):
        try:
            topic = Topic.objects.get(pk=pk)
        except Topic.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = TopicSerializer(topic)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            topic = Topic.objects.get(pk=pk)
        except Topic.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = TopicSerializer(topic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            topic = Topic.objects.get(pk=pk)
        except Topic.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        topic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
