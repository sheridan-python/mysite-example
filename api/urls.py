from django.urls import path
from . import views

# Namespace for the API app
app_name = 'api'

urlpatterns = [
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('', views.index, name='index'),
]
