# Generated by Django 3.1 on 2020-09-18 18:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('client', '0003_auto_20200916_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='VISAGE',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
