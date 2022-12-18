# Generated by Django 4.1.4 on 2022-12-14 03:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_comment_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reel',
            name='uploader',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='uploaded by'),
        ),
    ]
