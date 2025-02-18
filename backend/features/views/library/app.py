from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ...models import Library
from ...serializers import LibrarySerializer
from core.permissions import IsSuperAdmin, IsAdmin
from rest_framework.permissions import IsAuthenticated

class LibraryListCreateView(APIView):
    permission_classes = [IsAuthenticated, IsSuperAdmin | IsAdmin]

    def get(self, request):
        libraries = Library.objects.all()
        serializer = LibrarySerializer(libraries, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LibrarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LibraryDetailView(APIView):
    permission_classes = [IsAuthenticated, IsSuperAdmin | IsAdmin]

    def get(self, request, pk):
        try:
            library = Library.objects.get(pk=pk)
        except Library.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = LibrarySerializer(library)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            library = Library.objects.get(pk=pk)
        except Library.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = LibrarySerializer(library, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            library = Library.objects.get(pk=pk)
        except Library.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        library.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
