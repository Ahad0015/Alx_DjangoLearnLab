
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet
from rest_framework.authtoken.views import obtain_auth_token

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
router = DefaultRouter()
router.register(r"tasks", TaskViewSet, basename="task")

urlpatterns = [
    path("", include(router.urls)),
    path("token/", obtain_auth_token, name="api_token_auth"),
]