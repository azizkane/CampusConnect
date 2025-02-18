from rest_framework import serializers
from core.models.school import School, Department, Manager, Classroom
from django.conf import settings

class SchoolSerializer(serializers.ModelSerializer):
    admin_email = serializers.EmailField(write_only=True)
    admin_first_name = serializers.CharField(write_only=True)
    admin_last_name = serializers.CharField(write_only=True)
    admin_password = serializers.CharField(write_only=True)

    class Meta:
        model = School
        fields = '__all__'
        extra_fields = ['admin_email', 'admin_first_name', 'admin_last_name', 'admin_password']

    def create(self, validated_data):
        admin_data = {
            'email': validated_data.pop('admin_email'),
            'first_name': validated_data.pop('admin_first_name'),
            'last_name': validated_data.pop('admin_last_name'),
            'password': validated_data.pop('admin_password'),
            'role': 'Admin'
        }
        
        User = settings.AUTH_USER_MODEL
        admin = User.objects.create_user(**admin_data)
        validated_data['admin'] = admin
        validated_data['contact_email'] = admin.email
        validated_data['contact_phone_number'] = admin.phone_number

        return super().create(validated_data)

    def validate_name(self, value):
        if School.objects.filter(name=value).exists():
            raise serializers.ValidationError("A school with this name already exists.")
        return value


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'

class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = '__all__'