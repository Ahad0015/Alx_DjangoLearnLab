from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Task
        fields = [
            'id', 'owner', 'title', 'description', 
            'status', 'due_date', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'owner', 'created_at', 'updated_at']

    # Custom title validation
    def validate_title(self, value):
        cleaned_title = value.strip()
        
        if len(cleaned_title) < 3:
            raise serializers.ValidationError(
                'Title must be at least 3 characters long.'
            )

        return cleaned_title
