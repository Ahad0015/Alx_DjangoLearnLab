from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    ListView, 
    CreateView, 
    UpdateView, 
    DetailView, 
    DeleteView, 
    BlogDetailView, 
    CommentCreateView, 
    CommentUpdateView, 
    CommentDeleteView, 
    search_posts,
    PostByTagListView,  # Import the tag-based view
)

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile_view, name='profile'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('post/', ListView.as_view(), name='posts'),
    path('posts/search/', search_posts, name='search_posts'),  # Search posts
    path('post/new/', CreateView.as_view(), name='new-post'),
    path('post/<int:pk>/detail/', DetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', UpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', DeleteView.as_view(), name='post-delete'),  # Fixed typo in 'name'

    path('posts/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),  
    path('posts/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='comment_create'), 
    path('comments/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment_update'),  
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
    path('posts/tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='post_by_tag'),  # Tag-based view
     # Comment URLs
    path('post/<int:pk>/comments/new/', views.comment_create, name='comment-create'),
    path('comment/<int:pk>/update/', views.comment_update, name='comment-update'),
    path('comment/<int:pk>/delete/', views.comment_delete, name='comment-delete'),
]
]
