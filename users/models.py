from django.db import models
# extend existing model
from django.contrib.auth.models import User
# from pillow library import Image (we want to save images with smaller size)
from PIL import Image

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # this function is to save smaller profile images
    def save(self):
        # save the current instance
        super().save()
        # open image path of the current instance
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            # a var with the tupile with the pixels
            output_size = (300, 300)
            # save this sizes
            img.thumbnail(output_size)
            # save the current image in the path with the new size
            img.save(self.image.path)







