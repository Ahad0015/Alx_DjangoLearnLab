from rest_framework import viewsets, permissions, filters, status
from .permissions import IsOwner
# ... keep the rest

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]