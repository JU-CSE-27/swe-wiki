# Generated by Django 3.1.7 on 2022-01-07 09:49

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_comment', '0002_delete_unlikemodel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LikeModel',
            new_name='UserLikeModel',
        ),
    ]
