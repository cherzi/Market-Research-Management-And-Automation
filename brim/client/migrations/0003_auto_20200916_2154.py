# Generated by Django 3.1 on 2020-09-16 20:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_auto_20200916_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='DATE_CREATION',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='commande',
            name='DATE_CREATION',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='commande',
            name='DATE_ECHEANCE',
            field=models.DateTimeField(null=True),
        ),
    ]
