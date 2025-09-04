from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "due_date", "completed"]  
        # Adjust fields if your Task model is different
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter task title"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3, "placeholder": "Task details"}),
            "due_date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "completed": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


