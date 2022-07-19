from django.db import models
from .settings import abusive_language
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def checkOnMat(string):
    for i in abusive_language:
        if i in string:
            return True
    return False

def validate_mat(value):
    if checkOnMat(value) == True:
        raise ValidationError(
            _('Данный текст содержит нецензурную лексику. Просьба его убрать.'),
            # _('%(value)s содержит нецензурную лексику.'),
            params={'value': value},
        )

class Post(models.Model):
    title = models.CharField(max_length=60, validators=[validate_mat], verbose_name="Заголовок")
    text = models.TextField(blank=True, validators=[validate_mat], verbose_name="Текст")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    visible_all = models.BooleanField(default=False, verbose_name="Видно всем")
    visible_class = models.CharField(max_length=3, default="", blank=True, verbose_name="Определенный класс")
    img = models.ImageField(upload_to="users_photos/", blank=True, verbose_name="Картинка")

    def __str__(self):
        return f'Пост {self.title}, {self.id}'