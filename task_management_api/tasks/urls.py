from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

# Using DRF's DefaultRouter so I don't have to manually write all the CRUD routes
router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')   # not sure if I really need basename here, but leaving it

urlpatterns = [
    # This will include all the router-generated URLs under the root
    path('', include(router.urls)),

    # TODO: might add some extra custom endpoints here later (e.g. stats or reports)
    # path('tasks/stats/', TaskStatsView.as_view()),  # leaving as a reminder
]
