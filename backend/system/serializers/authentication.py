from rest_framework import serializers
from ..models.authentication import AuthToken

class AuthTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthToken
        fields = '__all__'

