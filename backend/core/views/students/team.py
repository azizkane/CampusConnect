from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.models.students.team import Team
from core.serializers import TeamSerializer
from core.permissions import IsSuperAdmin, IsAdmin, IsManager
from rest_framework.permissions import IsAuthenticated

class TeamListCreateView(APIView):
    permission_classes = [IsAuthenticated, IsSuperAdmin | IsAdmin | IsManager]

    def get(self, request):
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeamDetailView(APIView):
    permission_classes = [IsAuthenticated, IsSuperAdmin | IsAdmin | IsManager]

    def get(self, request, pk):
        try:
            team = Team.objects.get(pk=pk)
        except Team.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = TeamSerializer(team)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            team = Team.objects.get(pk=pk)
        except Team.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = TeamSerializer(team, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            team = Team.objects.get(pk=pk)
        except Team.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
