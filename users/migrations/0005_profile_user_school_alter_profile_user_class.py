# Generated by Django 4.0.4 on 2022-07-16 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_profile_user_class'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user_school',
            field=models.CharField(blank=True, max_length=2),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_class',
            field=models.CharField(blank=True, max_length=2),
        ),
    ]
