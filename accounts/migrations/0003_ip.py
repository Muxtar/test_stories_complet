# Generated by Django 4.1.7 on 2023-06-18 07:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_blockuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=12)),
                ('users', models.ManyToManyField(related_name='ip', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
