# Generated by Django 4.0.4 on 2022-07-19 10:55

from django.db import migrations, models
import mainapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_alter_post_text_alter_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, upload_to='users_photos/', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(blank=True, validators=[mainapp.models.validate_mat], verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=60, validators=[mainapp.models.validate_mat], verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='post',
            name='visible_all',
            field=models.BooleanField(default=False, verbose_name='Видно всем'),
        ),
        migrations.AlterField(
            model_name='post',
            name='visible_class',
            field=models.CharField(blank=True, default='', max_length=3, verbose_name='Определенный класс'),
        ),
    ]
