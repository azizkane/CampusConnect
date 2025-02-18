from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from features.models import CalendarSettings, SharedCalendar
from features.serializers import CalendarSettingsSerializer, SharedCalendarSerializer
from rest_framework.permissions import IsAuthenticated
# from core.permissions import IsStudent

class CalendarSettingsListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Filter calendars by the current user
        calendars = SharedCalendar.objects.filter(members=request.user) # --------
        serializer = SharedCalendarSerializer(calendars, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SharedCalendarSerializer(data=request.data)
        if serializer.is_valid():
            # Automatically add the current user as a member
            calendar = serializer.save()
            calendar.members.add(request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CalendarSettingsDetailView(APIView):
    def get(self, request, pk):
        try:
            settings = CalendarSettings.objects.get(pk=pk)
        except CalendarSettings.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = CalendarSettingsSerializer(settings)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            settings = CalendarSettings.objects.get(pk=pk)
        except CalendarSettings.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = CalendarSettingsSerializer(settings, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            settings = CalendarSettings.objects.get(pk=pk)
        except CalendarSettings.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        settings.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SharedCalendarListCreateView(APIView):
    def get(self, request):
        calendars = SharedCalendar.objects.all()
        serializer = SharedCalendarSerializer(calendars, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SharedCalendarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SharedCalendarDetailView(APIView):
    def get(self, request, pk):
        try:
            calendar = SharedCalendar.objects.get(pk=pk)
        except SharedCalendar.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = SharedCalendarSerializer(calendar)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            calendar = SharedCalendar.objects.get(pk=pk)
        except SharedCalendar.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = SharedCalendarSerializer(calendar, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            calendar = SharedCalendar.objects.get(pk=pk)
        except SharedCalendar.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        calendar.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
