from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from .models import Task
from .forms import TaskForm


# Show all tasks for the logged-in user
@login_required
def task_list(request):
    # filtering by user explicitly — could’ve used related_name but meh
    user_tasks = Task.objects.filter(owner=request.user).order_by("-created_at")

    # might later paginate this if list grows too big
    return render(request, "tasks/task_list.html", {
        "tasks": user_tasks,
        "page_title": "My Tasks"   # not really needed but feels nice
    })


# Create a new task (basic form handling)
@login_required
def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task_obj = form.save(commit=False)  # need this to attach owner
            task_obj.owner = request.user
            task_obj.save()
            # maybe add a success message later with django.contrib.messages
            return redirect("task_list")
    else:
        form = TaskForm()

    return render(request, "tasks/task_form.html", {
        "form": form,
        "title": "Create Task"
    })


# Edit an existing task (only if it belongs to the user)
@login_required
def task_update(request, pk):
    task_item = get_object_or_404(Task, pk=pk, owner=request.user)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task_item)
        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = TaskForm(instance=task_item)

    # note: same template as create — could separate them but not worth it yet
    return render(request, "tasks/task_form.html", {
        "form": form,
        "title": "Update Task"
    })


# Confirm & delete a task
@login_required
def task_delete(request, pk):
    task_entry = get_object_or_404(Task, pk=pk, owner=request.user)

    if request.method == "POST":
        task_entry.delete()
        return redirect("task_list")

    # using a separate confirm template just to be safe
    return render(request, "tasks/task_confirm_delete.html", {
        "task": task_entry
    })


# Simple registration view (maybe move to accounts app later?)
def register(request):
    if request.method == "POST":
        signup_form = UserCreationForm(request.POST)
        if signup_form.is_valid():
            new_user = signup_form.save()
            auth_login(request, new_user)   # logs them in immediately
            return redirect("task_list")
    else:
        signup_form = UserCreationForm()

    return render(request, "registration/register.html", {
        "form": signup_form
    })
