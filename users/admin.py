from django.contrib import admin

# we import the Profile model from the models to admin page
from .models import Profile


# Register your models here.

admin.site.register(Profile)
