from django.contrib import admin
# import the post model
from .models import Post
# Register your models here.

# register the model to the admin
admin.site.register(Post)