from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from core.models.students.app import Student
from core.serializers.student import StudentSerializer
from core.permissions import IsSuperAdmin, IsAdmin, IsManager
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
import logging

logger = logging.getLogger(__name__)

class StudentPagination(PageNumberPagination):
    page_size = 10

class StudentListCreateView(APIView):
    permission_classes = [IsAuthenticated, IsSuperAdmin | IsAdmin | IsManager]
    pagination_class = StudentPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['first_name', 'last_name', 'email']
    search_fields = ['first_name', 'last_name', 'email']

    def get(self, request):
        students = Student.objects.all()
        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(students, request)
        serializer = StudentSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info(f"Student created: {serializer.data}")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error(f"Student creation failed: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentDetailView(APIView):
    permission_classes = [IsAuthenticated, IsSuperAdmin | IsAdmin]

    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return None

    def get(self, request, pk):
        student = self.get_object(pk)
        if not student:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk):
        student = self.get_object(pk)
        if not student:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info(f"Student updated: {serializer.data}")
            return Response(serializer.data)
        logger.error(f"Student update failed: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student = self.get_object(pk)
        if not student:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        student.delete()
        logger.info(f"Student deleted: {pk}")
        return Response(status=status.HTTP_204_NO_CONTENT)
