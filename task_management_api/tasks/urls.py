
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
]
from django.urls import path
from .views import TaskListCreateView, TaskRetrieveUpdateDestroyView

# Task app endpoints
urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),

    # Endpoint for retrieving, updating, or deleting a single task
    # NOTE: pk = primary key; could rename to <task_id> for clarity, but pk works fine
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyView.as_view(), name='task-rud'),

    # path('tasks/<uuid:id>/', ...)  # TODO: Maybe switch to UUIDs in the future
]
