from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import TaskViewSet   # hmm, maybe I’ll split this file later if it grows

# Using DRF’s DefaultRouter (easier than wiring everything by hand)
api_router = DefaultRouter()

# registering my task endpoints — note: using plural 'tasks'
api_router.register(r"tasks", TaskViewSet, basename="task")

# I might add more stuff later like auth, users, etc.
urlpatterns = [
    path("", include(api_router.urls)),   # root API routes
    # path("tasks/", include("myapp.something"))   # just a thought
]
