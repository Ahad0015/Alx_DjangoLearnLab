
from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    # Display these columns in the admin list view
    list_display = ('id', 'title', 'owner', 'status', 'due_date', 'created_at')

    # Quick filters on the right-hand side
    list_filter = ('status',)  # could also filter by owner if needed

    # Searchable fields
    search_fields = ('title', 'description', 'owner__username')

   
