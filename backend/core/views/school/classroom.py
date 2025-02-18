from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ...models import *
from ...serializers import *
from django.contrib.auth.models import Group 


class ClassroomListCreateView(APIView):
    def get(self, request):
        classrooms = Classroom.objects.all()
        serializer = ClassroomSerializer(classrooms, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClassroomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClassroomDetailView(APIView):
    def get(self, request, pk):
        try:
            classroom = Classroom.objects.get(pk=pk)
        except Classroom.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ClassroomSerializer(classroom)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            classroom = Classroom.objects.get(pk=pk)
        except Classroom.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ClassroomSerializer(classroom, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            classroom = Classroom.objects.get(pk=pk)
        except Classroom.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        classroom.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
