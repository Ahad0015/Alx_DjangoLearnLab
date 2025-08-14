
# Create your models here.

from django.db import models
from django.contrib.auth import get_user_model

# Using Django's built-in user model
User = get_user_model()

class Task(models.Model):
    class Status(models.TextChoices):
        PENDING = 'pending', 'Pending'
        IN_PROGRESS = 'in_progress', 'In Progress'
        COMPLETED = 'completed', 'Completed'
    

    # Who owns the task — if the user gets deleted, their tasks go with them
    owner = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='tasks'  
    )

    # Main fields
    title = models.CharField(max_length=255)  # might reduce max_length later
    description = models.TextField(blank=True)  

    # Task progress status
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING
    )

    # Optional deadline
    due_date = models.DateField(null=True, blank=True)

    # Auto timestamps
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)      

    class Meta:
        ordering = ['-created_at']  
        verbose_name = "Task"       
        verbose_name_plural = "Tasks"

    def __str__(self):
        return f"{self.title} ({self.status})"

  
