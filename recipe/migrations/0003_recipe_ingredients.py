# Generated by Django 3.1.7 on 2022-01-15 17:51

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_recipe_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=tinymce.models.HTMLField(default=None),
            preserve_default=False,
        ),
    ]