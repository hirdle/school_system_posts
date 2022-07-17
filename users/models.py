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
    
    def save(self):
        super().save()

        image = Image.open(self.img.path)

        if image.height > 64 or image.width > 64:
            resize = (64, 64)
            image.thumbnail(resize)
            image.save(self.img.path)