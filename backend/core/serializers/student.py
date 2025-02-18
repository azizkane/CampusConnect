from rest_framework import serializers
from core.models import Student, Team

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    # Example of custom validation
    def validate_email(self, value):
        if Student.objects.filter(email=value).exists():
            raise serializers.ValidationError("A student with this email already exists.")
        return value

    # Example of dynamic fields
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        super(StudentSerializer, self).__init__(*args, **kwargs)
        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'