# api/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task

# Serializer for registering new users
# TODO: Might add password confirmation later (double-check before saving)
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # don't expose this in API response

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']  # kept it explicit, just in case

    def create(self, validated_data):
        # Using create_user so it hashes the password
        # NOTE: If we ever add more fields, remember to update here
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),  # fallback if email is missing
            password=validated_data['password']
        )
        # print(f"DEBUG: Created user {user.username}")  # for testing only
        return user


# Serializer for Task model
class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')  # show username, not ID

    class Meta:
        model = Task
        # NOTE: 'completed' field implies a boolean, but check model definition to be sure
        fields = [
            'id', 'title', 'description', 'completed',
            'due_date', 'owner'
        ]
        # Possibly add read_only_fields=['owner'] later if we restrict updates

