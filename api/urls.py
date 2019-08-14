from django.urls import path
from . import views

# Namespace for the API app
app_name = 'api'

urlpatterns = [
    path('comments/', views.CommentListCreateView.as_view(), name='comment-list'),
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('', views.index, name='index'),
]
