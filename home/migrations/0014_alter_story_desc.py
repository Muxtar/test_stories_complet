# Generated by Django 4.1.7 on 2023-05-16 07:27

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_story_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='desc',
            field=ckeditor.fields.RichTextField(),
        ),
    ]