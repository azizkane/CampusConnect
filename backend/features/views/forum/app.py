from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ...models import Forum
from ...serializers import ForumSerializer

class ForumListCreateView(APIView):
    def get(self, request):
        forums = Forum.objects.all()
        serializer = ForumSerializer(forums, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ForumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ForumDetailView(APIView):
    def get(self, request, pk):
        try:
            forum = Forum.objects.get(pk=pk)
        except Forum.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ForumSerializer(forum)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            forum = Forum.objects.get(pk=pk)
        except Forum.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ForumSerializer(forum, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            forum = Forum.objects.get(pk=pk)
        except Forum.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        forum.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
