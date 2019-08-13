from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path(
        'posts/<int:year>/<int:month>/<int:day>/<slug:slug>/',
        views.PostDetailView.as_view(),
        name='post-detail',
    ),
    path(
        'posts/<int:pk>/',
        views.PostDetailView.as_view(),
        name='post-detail'
    ),
    path('terms/', views.terms_and_conditions, name='terms-and-conditions'),
    path('form-example/', views.form_example, name='form-example'),
    path(
        'formview-example/',
        views.FormViewExample.as_view(),
        name='formview-example'
    ),
    path('api/', include('api.urls')),
    path('', views.HomeView.as_view(), name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
