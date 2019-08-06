from django.shortcuts import render
from django.views import View
from . import models


def home(request):
    """
    The Blog homepage
    """
    latest_posts = models.Post.objects.published().order_by('-published')[:3]
    authors = models.Post.objects.published() \
        .get_authors() \
        .order_by('first_name')

    context = {
        'authors': authors,
        'latest_posts': latest_posts
    }

    return render(request, 'blog/home.html', context)


class AboutView(View):
    def get(self, request):
        return render(request, 'blog/about.html')
