from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ...models.library.document import Document
from ...serializers.library import DocumentSerializer
from core.permissions import IsSuperAdmin, IsAdmin
from rest_framework.permissions import IsAuthenticated

class DocumentListCreateView(APIView):
    permission_classes = [IsAuthenticated, IsSuperAdmin | IsAdmin]

    def get(self, request, category_pk, library_pk):
        documents = Document.objects.filter(library_id=library_pk)
        serializer = DocumentSerializer(documents, many=True)
        return Response(serializer.data)

    def post(self, request, category_pk, library_pk):
        data = request.data.copy()
        data['library'] = library_pk
        data['uploaded_by'] = request.user.id
        serializer = DocumentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DocumentDetailView(APIView):
    permission_classes = [IsAuthenticated, IsSuperAdmin | IsAdmin]

    def get(self, request, category_pk, library_pk, pk):
        try:
            document = Document.objects.get(pk=pk, library_id=library_pk)
        except Document.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = DocumentSerializer(document)
        return Response(serializer.data)

    def put(self, request, category_pk, library_pk, pk):
        try:
            document = Document.objects.get(pk=pk, library_id=library_pk)
        except Document.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        data = request.data.copy()
        data['library'] = library_pk
        data['uploaded_by'] = request.user.id
        serializer = DocumentSerializer(document, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, category_pk, library_pk, pk):
        try:
            document = Document.objects.get(pk=pk, library_id=library_pk)
        except Document.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        document.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
