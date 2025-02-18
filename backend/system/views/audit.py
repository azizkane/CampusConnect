from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from ..models import Log
from ..serializers import AuditLogSerializer

class AuditLogListView(generics.ListAPIView):
    queryset = Log.objects.all()
    serializer_class = AuditLogSerializer
    permission_classes = [IsAuthenticated]
