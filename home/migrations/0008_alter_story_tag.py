# Generated by Django 4.1.7 on 2023-05-04 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_story'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='tag',
            field=models.ManyToManyField(blank=True, null=True, related_name='story', to='home.tag'),
        ),
    ]
