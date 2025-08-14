from rest_framework import generics, permissions
from .models import Task
from .serializers import TaskSerializer

# List all tasks for the logged-in user OR create a new one
# (Might later add pagination here if tasks grow too large)
class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only return tasks that belong to the current user
        user = self.request.user
        return Task.objects.filter(owner=user).order_by('-created_at')  # Ordering here just to be explicit

    def perform_create(self, serializer):
        # Set owner automatically instead of trusting the client
        serializer.save(owner=self.request.user)
        # print("DEBUG: Task created for", self.request.user.username)  

# Retrieve, update, or delete a specific task (only if it belongs to the logged-in user)
class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Same filtering logic as above — could DRY this up later
        qs = Task.objects.filter(owner=self.request.user)
        # NOTE: Might be worth adding select_related('owner') for performance
        return qs

