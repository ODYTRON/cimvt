# import to render the templates
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
# we have class based views from now on
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView

)
# import to render the httpresponses
# not so usefull for now
# from django.http import HttpResponse
# import from the current directory the model Post (class Post)
from .models import Post

# Create your views here


# lets pretent we have a DB
# posts = [
#     {
#         'author': 'CoreMS',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'August 27, 2018'
#
#     },
# {
#         'author': 'Jane Doe',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'August 28, 2018'
#     }
# ]


def home(request):
    # create a dictionary called context
    context = {
        # put a key with a value posts
        'posts' : Post.objects.all()
    }
    # as a third argument pass context
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html (it expects a template with that name)
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html' # <app>/<model>_<viewtype>.html (it expects a template with that name)
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('date_posted')




class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    # we create this method in order to automaticaly assign a new post to the logged in user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    # we create this method in order to automaticaly assign a new post to the logged in user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    # test if the post belongs to the author
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    # test if the post belongs to the author
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



# just to show that there is a title in the view to be rendered on the window tab from the html contitional
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})