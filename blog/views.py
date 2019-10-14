# import to render the templates
from django.shortcuts import render
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

# just to show that there is a title in the view to be rendered on the window tab from the html contitional
def about(request):
    return render(request,'blog/about.html', {'title':'About'})