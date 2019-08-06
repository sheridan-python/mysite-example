from django.views.generic.base import TemplateView
from . import models


class ContextMixin:
    """
    Provides common context variables for blog views
    """
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authors'] = models.Post.objects.published() \
            .get_authors() \
            .order_by('first_name')

        return context


class HomeView(ContextMixin, TemplateView):
    template_name = 'blog/home.html'

    def get_context_data(self, **kwargs):
        # Get the parent context
        context = super().get_context_data(**kwargs)

        latest_posts = models.Post.objects.published() \
            .order_by('-published')[:3]

        authors = models.Post.objects.published() \
            .get_authors() \
            .order_by('first_name')

        # Update the context with our context variables
        context.update({
            'authors': authors,
            'latest_posts': latest_posts
        })

        return context


class AboutView(ContextMixin, TemplateView):
    template_name = 'blog/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authors'] = models.Post.objects.published() \
            .get_authors() \
            .order_by('first_name')

        return context
