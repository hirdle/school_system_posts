# Generated by Django 4.0.4 on 2022-07-16 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_profile_user_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_class',
            field=models.CharField(blank=True, max_length=3),
        ),
    ]
