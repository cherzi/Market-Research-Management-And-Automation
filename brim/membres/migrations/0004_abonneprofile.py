# Generated by Django 3.1 on 2020-09-22 20:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('membres', '0003_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbonneProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='')),
                ('user', models.OneToOneField(blank=True, limit_choices_to={'groups__name': 'Délégué'}, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
