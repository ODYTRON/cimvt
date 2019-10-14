from django.db import models
from django.utils import timezone
# users and authors will have a relationship since users will post  (one to many relationship)
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # auto_now = true means to take the date every time you update a post
    # auto_now_add = true means that the creation date not changes
    # the util timezone as default is taking the value of function now and not the execution .now()
    date_posted = models.DateTimeField(default=timezone.now)
    # the user can post many articles but an article can be posted only by one author
    # if we delete the user his her posts deleted also
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
