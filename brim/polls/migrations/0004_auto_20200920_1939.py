# Generated by Django 3.1 on 2020-09-20 18:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0003_sondage_statut'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sondage',
            name='personnes',
            field=models.ManyToManyField(blank=True, limit_choices_to={'groups__name': 'Abonné'}, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
