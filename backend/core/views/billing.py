from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from core.models.billing.plan import Plan
from core.models.billing.subscription import Subscription
from core.serializers.billing import PlanSerializer, SubscriptionSerializer
from core.permissions import IsSuperAdmin, IsAdmin

class PlanListCreateView(generics.ListCreateAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    permission_classes = [IsAuthenticated, IsSuperAdmin | IsAdmin]

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PlanDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    permission_classes = [IsAuthenticated, IsSuperAdmin | IsAdmin]

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

    def delete(self, request, *args, **kwargs):
        plan = self.get_object()
        plan.is_active = False
        plan.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SubscriptionListCreateView(generics.ListCreateAPIView):
    queryset = Subscription.objects.select_related('school', 'plan').all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated, IsSuperAdmin | IsAdmin]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SubscriptionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subscription.objects.select_related('school', 'plan').all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated, IsSuperAdmin | IsAdmin]

    def delete(self, request, *args, **kwargs):
        subscription = self.get_object()
        subscription.status = 'Cancelled'
        subscription.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
