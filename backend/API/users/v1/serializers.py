from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as DjoserUserCreateSerializer
from users.models import UserProfile, CustomUser
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions as django_exceptions
from rest_framework.settings import api_settings


# Serializer for registering the user 
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        # Fields to be serialized
        fields = ['user_guid', 'user_type', 'wallet_balance', 'created_at', 'updated_at']
        # Fields that are read-only, meaning they won't be modified by the user
        read_only_fields = ['user_guid', 'created_at', 'updated_at']


# Custom serializer for user creation, extending Djoser's UserCreateSerializer
class CustomUserCreateSerializer(DjoserUserCreateSerializer):
    # Nesting the UserProfileSerializer to handle related UserProfile data
    userProfile = UserProfileSerializer()

    class Meta:
        model = CustomUser
        # Fields to be serialized during user creation
        fields = ['id', 'email', 'password','first_name','last_name','is_active','userProfile']

    # Overriding the create method to handle user profile creation along with the user
    def create(self, validated_data):
        # Extracting UserProfile data from the validated data
        profile_data = validated_data.pop('userProfile')
        # Creating the user using Djoser's create_user method
        user = CustomUser.objects.create_user(**validated_data)
        # Creating the UserProfile instance associated with the newly created user
        UserProfile.objects.create(user=user, **profile_data)
        return user

    # Custom validation to handle password validation and add back UserProfile data
    def validate(self, attrs):
        # Extract UserProfile data before validation
        profile_data = attrs.pop("userProfile")
        # Create a temporary CustomUser instance to validate against
        user = CustomUser(attrs)
        # Create a temporary UserProfile instance
        profile = UserProfile(user=user, **profile_data)
        # Get the password from the validated data
        # Get the password from the validated data
        password = attrs.get("password")
        try:
            # Validate the password using Django's built-in validators
            validate_password(password, user)
        except django_exceptions.ValidationError as e:
            # If validation fails, raise a validation error with a descriptive message
            serializer_error = serializers.as_serializer_error(e)
            raise serializers.ValidationError(
                {"password": serializer_error[api_settings.NON_FIELD_ERRORS_KEY]}
            )
        # Add back the UserProfile data after validation
        attrs["userProfile"] = profile_data
        return attrs

# 
class CustomUserUpdateSerializer(serializers.ModelSerializer):
    # Include the nested UserProfileSerializer to update related profile data
    userProfile = UserProfileSerializer()

    class Meta:
        model = CustomUser
        # Fields to be serialized during user update
        fields = ['id', 'email', 'first_name', 'last_name', 'is_active', 'userProfile']
        # Fields that are read-only, meaning they won't be modified by the user
        read_only_fields = ['id', 'email']

    def update(self, instance, validated_data):
        # Handle nested UserProfile update
        user_profile_data = validated_data.pop('userProfile', None)
        if user_profile_data:
            UserProfileSerializer().update(instance.userProfile, user_profile_data)
        return super().update(instance, validated_data)