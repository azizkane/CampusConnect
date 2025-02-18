from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from ...models import School, User
from ...serializers import SchoolSerializer
from django.contrib.auth.models import Group
from core.permissions import IsSuperAdmin
from rest_framework.permissions import IsAuthenticated

class SchoolPagination(PageNumberPagination):
    page_size = 10

class SchoolListCreateView(APIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    pagination_class = SchoolPagination
    permission_classes = [IsAuthenticated, IsSuperAdmin]

    def post(self, request):
        serializer = SchoolSerializer(data=request.data)
        if serializer.is_valid():
            school = serializer.save()
            
            # Create a school admin user
            admin_data = request.data.get('admin')
            if admin_data:
                admin_user = User.objects.create_user(
                    email=admin_data['email'],
                    password=admin_data['password'],
                    first_name=admin_data['first_name'],
                    last_name=admin_data['last_name'],
                    role='Admin',
                    is_staff=True
                )
                # Assign the admin to the school
                school.admin = admin_user
                school.save()

                # Add the user to an 'Admin' group
                admin_group, created = Group.objects.get_or_create(name='School Admin')
                admin_user.groups.add(admin_group)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class SchoolDetailView(APIView):
    permission_classes = [IsAuthenticated, IsSuperAdmin]

    def get(self, request, pk):
        try:
            school = School.objects.get(pk=pk)
        except School.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = SchoolSerializer(school)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            school = School.objects.get(pk=pk)
        except School.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = SchoolSerializer(school, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            school = School.objects.get(pk=pk)
        except School.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        school.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
