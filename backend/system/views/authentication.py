from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from ..models.authentication import AuthToken
from ..serializers import AuthTokenSerializer
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken

class AuthTokenView(generics.GenericAPIView):
    permission_classes = [AllowAny]  # Allow any user to attempt authentication
    serializer_class = AuthTokenSerializer

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)

    def get(self, request):
        tokens = self.get_queryset()
        serializer = self.get_serializer(tokens, many=True)
        return Response(serializer.data)
