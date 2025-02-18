from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from core.models.accounts import User, UserProfile
from core.serializers.accounts import UserSerializer, UserProfileSerializer
from rest_framework.permissions import IsAuthenticated
from core.permissions import IsSuperAdmin, IsAdmin
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination

class UserListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsSuperAdmin | IsAdmin]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['role', 'is_active', 'email']
    pagination_class = PageNumberPagination

    def perform_create(self, serializer):
        serializer.save()

class UserDetailView(APIView):
    permission_classes = [IsAuthenticated, IsSuperAdmin | IsAdmin]

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return None

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        if user is None:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        if user is None:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        if user is None:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserProfileSerializer

    def get_object(self):
        return UserProfile.objects.get(user=self.request.user)
