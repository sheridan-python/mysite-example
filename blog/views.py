from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic import DetailView, CreateView, FormView, ListView
from . import forms, models


class HomeView(TemplateView):
    template_name = 'blog/home.html'

    def get_context_data(self, **kwargs):
        # Get the parent context
        context = super().get_context_data(**kwargs)
        latest_posts = models.Post.objects.published() \
            .order_by('-published')[:3]

        context.update({'latest_posts': latest_posts})

        return context


class AboutView(TemplateView):
    template_name = 'blog/about.html'


class PostDetailView(DetailView):
    model = models.Post

    def get_queryset(self):
        queryset = super().get_queryset().published()
        if 'pk' in self.kwargs:
            return queryset

        return queryset.filter(
            published__year=self.kwargs['year'],
            published__month=self.kwargs['month'],
            published__day=self.kwargs['day'],
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get the post object
        post = self.get_object()

        # Set the post field on the form
        comment_form = forms.CommentForm(initial={'post': post})
        comments = models.Comment.objects.filter(post=post)

        context['comment_form'] = comment_form
        context['comments'] = comments.order_by('-created')

        return context


class PostListView(ListView):
    model = models.Post
    context_object_name = 'posts'
    queryset = models.Post.objects.published().order_by('-published')


def terms_and_conditions(request):
    return render(request, 'blog/terms_and_conditions.html')


def form_example(request):
    # Handle the POST
    if request.method == 'POST':
        # Pass the POST data into a new form instance for validation
        form = forms.ExampleSignupForm(request.POST)

        # If the form is valid, return a different template.
        if form.is_valid():
            # form.cleaned_data is a dict with valid form data
            cleaned_data = form.cleaned_data

            return render(
                request,
                'blog/form_example_success.html',
                context={'data': cleaned_data}
            )
    # If not a POST, return a blank form
    else:
        form = forms.ExampleSignupForm()

    # Return if either an invalid POST or a GET
    return render(request, 'blog/form_example.html', context={'form': form})


class FormViewExample(FormView):
    template_name = 'blog/form_example.html'
    form_class = forms.ExampleSignupForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Thank you for signing up!'
        )
        return super().form_valid(form)


class ContactFormView(CreateView):
    model = models.Contact
    success_url = reverse_lazy('home')
    fields = [
        'first_name',
        'last_name',
        'email',
        'message',
    ]

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Thank you! Your message has been sent.'
        )
        return super().form_valid(form)
