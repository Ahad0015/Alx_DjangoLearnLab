from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm


@login_required
def task_create(request):
    # Handles creating a new task
    if request.method == "POST":
        # Honestly, I usually re-check this twice because I sometimes forget commit=False
        form = TaskForm(request.POST or None)
        if form.is_valid():
            new_task = form.save(commit=False)  # don’t save to DB yet
            new_task.user = request.user        # attach the user manually
            new_task.save()
            # I might want to redirect to a detail page later, but for now just home
            return redirect("home")
    else:
        # if not POST, just show the empty form
        form = TaskForm()

    # using a dictionary explicitly (even though inline would work)
    ctx = {"form": form}
    return render(request, "tasks/task_form.html", ctx)


@login_required
def task_update(request, pk):
    # This fetches the task but also ensures it belongs to the user
    task_obj = get_object_or_404(Task, pk=pk, user=request.user)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task_obj)
        if form.is_valid():
            updated_task = form.save(commit=False)
            updated_task.save()   # kinda redundant since save() already works directly
            return redirect("home")
    else:
        form = TaskForm(instance=task_obj)

    return render(request, "tasks/task_form.html", {"form": form})


@login_required
def task_delete(request, pk):
    # NOTE: maybe add a check for permissions later if needed
    task_to_remove = get_object_or_404(Task, pk=pk, user=request.user)

    if request.method == "POST":
        task_to_remove.delete()
        # Could use reverse_lazy instead of 'home' string, but this is fine
        return redirect("home")

    # I like passing the object itself so the template can show its title
return render(request, "tasks/task_confirm_delete.html", {"task": task_to_remove})


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == "POST":
        task.delete()
        return redirect("task_list")
    return render(request, "tasks/task_confirm_delete.html", {"task": task})





