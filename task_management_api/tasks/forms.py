from django import forms
from .models import Task

# Okay, so I’m making a form that maps directly to the Task model.
# Honestly, I might add custom validations later but for now this should do.
class TaskForm(forms.ModelForm):

    # Just in case I want to override some fields later, leaving space here.
    # e.g. I could make the title field bigger, but I'll keep it default for now.
    # title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Task
        # Keeping only these three fields for now.
        # NOTE: Might need to add "due_date" if we ever add it to the model.
        fields = ['title', 'description', 'completed']
        # fields = '__all__'   # <-- I was tempted to just use this, but nah, let's be explicit.
