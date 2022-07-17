from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=60)
    text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    visible_all = models.BooleanField(default=False)
    visible_class = models.CharField(max_length=3, default="", blank=True)
    img = models.ImageField(upload_to="users_photos/", blank=True)

    def __str__(self):
        return f'Пост {self.title}, {self.id}'