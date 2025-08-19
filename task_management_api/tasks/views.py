from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer


# ViewSet to deal with tasks (CRUD basically)
class TaskViewSet(viewsets.ModelViewSet):
    # I might come back later and make this docstring more detailed...
    """
    Endpoints for working with tasks.
    Right now it's just the default stuff (list, create, update, delete).
    """

    # I thought about filtering or ordering here, but leaving it simple for now
    queryset = Task.objects.all()

    # serializer takes care of converting model objects to JSON and back
    serializer_class = TaskSerializer

    # keeping it locked down so only logged-in folks can access
    permission_classes = [permissions.IsAuthenticated]

    # NOTE: At some point, I might want to override `get_queryset` to only
    # return tasks owned by the current user, but leaving it wide open for now.
    # def get_queryset(self):
    #     return Task.objects.filter(owner=self.request.user)
