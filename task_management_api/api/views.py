from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Task
from .serializers import TaskSerializer, UserSerializer
from django.contrib.auth.models import User

# Handles user registration
# TODO: Add password confirmation + email verification later
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]  # open endpoint

# Task CRUD via ViewSet — includes filtering/search/order
class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Filters & searching
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filterset_fields = ['completed']  # True/False filtering
    search_fields = ['title', 'description']  # could add status later
    ordering_fields = ['due_date', 'title']

    def get_queryset(self):
        # Only fetch the current user's tasks
        # NOTE: Could prefetch_related('owner') to optimize admin listing
        user = self.request.user
        return Task.objects.filter(owner=user).order_by('-created_at')  # explicit even if model has ordering

    def perform_create(self, serializer):
        # Set the owner automatically so clients can't mess with it
        serializer.save(owner=self.request.user)
        # print("DEBUG: Created task", serializer.instance.id)  # handy during dev

    # PATCH /tasks/<id>/complete/
    @action(detail=True, methods=['patch'], url_path='complete')
    def mark_complete(self, request, pk=None):
        task = self.get_object()
        if not task.completed:  # avoid unnecessary save if already completed
            task.completed = True
            task.save()
            return Response({'status': 'Task marked as complete'})
        return Response({'status': 'Task was already complete'})
