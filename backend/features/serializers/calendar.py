from rest_framework import serializers
from ..models.calendar import *

class CalendarSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalendarSettings
        fields = '__all__'

class SharedCalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = SharedCalendar
        fields = '__all__'
        
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'