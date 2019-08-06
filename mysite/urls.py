from django.contrib import admin
from django.urls import path

from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.AboutView.as_view(), name='about'),
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('terms/', views.terms_and_conditions, name='terms-and-conditions'),
    path('', views.HomeView.as_view(), name='home'),
]
