from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.

class User(AbstractUser):
    pass


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=200)
    posts = models.ManyToManyField(Post)









# If not already implemented, create a Tag model in your blog app that includes a name field.
# Establish a many-to-many relationship between Tag and Post models to allow assigning multiple tags to a single post and associating multiple posts with a single tag.
# Use Django’s migrations to create and update the database schema.
