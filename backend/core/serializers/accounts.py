from rest_framework import serializers
from core.models.accounts import User, UserProfile
from django.contrib.auth.password_validation import validate_password

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['avatar', 'bio', 'preferences']

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    email = serializers.EmailField(required=True)
    profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'role', 'is_active', 'profile', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'validators': []},
        }

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value

    def create(self, validated_data):
        profile_data = validated_data.pop('profile', {})
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        UserProfile.objects.create(user=instance, **profile_data)
        return instance

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', {})
        password = validated_data.pop('password', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password is not None:
            instance.set_password(password)
        instance.save()

        # Update profile
        profile = instance.profile
        for attr, value in profile_data.items():
            setattr(profile, attr, value)
        profile.save()

        return instance

    def validate_role(self, value):
        if value not in dict(User.ROLE_CHOICES):
            raise serializers.ValidationError("Invalid role")
        return value
