# Generated by Django 3.2.13 on 2022-05-26 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0006_auto_20220516_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='artist',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='song',
            name='original_artist',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='song',
            name='title',
            field=models.CharField(max_length=25),
        ),
    ]