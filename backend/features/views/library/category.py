from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ...models.library.category import Category
from ...serializers.library import CategorySerializer
from core.permissions import IsSuperAdmin, IsAdmin
from rest_framework.permissions import IsAuthenticated

class CategoryListCreateView(APIView):
    permission_classes = [IsAuthenticated, IsSuperAdmin | IsAdmin]

    def get(self, request):
        categories = Category.objects.filter(school=request.user.school)
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(school=request.user.school)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryDetailView(APIView):
    permission_classes = [IsAuthenticated, IsSuperAdmin | IsAdmin]

    def get(self, request, pk):
        try:
            category = Category.objects.get(pk=pk, school=request.user.school)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            category = Category.objects.get(pk=pk, school=request.user.school)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            category = Category.objects.get(pk=pk, school=request.user.school)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
