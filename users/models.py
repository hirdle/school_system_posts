from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_class_number = models.CharField(max_length=2, blank=True)
    user_class_letter = models.CharField(max_length=1, blank=True)
    img = models.ImageField(default="service/default.jpg", upload_to="users_photos")

    def __str__(self):
        return f'Профиль пользователя {self.user.username}'
    
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 200 or img.width > 200:
            output_size = (200, 200)
            img.thumbnail(output_size)
            img.save(self.image.path)