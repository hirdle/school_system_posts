# Generated by Django 4.0.4 on 2022-07-16 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('text', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('visible_all', models.BooleanField(default=False)),
                ('visible_class', models.CharField(blank=True, default='', max_length=3)),
                ('img', models.ImageField(upload_to='users_photos/')),
            ],
        ),
    ]
