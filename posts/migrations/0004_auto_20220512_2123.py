# Generated by Django 3.2.13 on 2022-05-12 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_delete_song'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
