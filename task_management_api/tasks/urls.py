from django.urls import path
from django.shortcuts import render

# Just a quick home view here instead of making a views.py for now
def home(request):
    # Could add some context later if I need to pass data to the template
    return render(request, "home.html")

urlpatterns = [
    path("", home, name="home"),   # main landing page
    # path("about/", about, name="about"),  # might add this later
]
