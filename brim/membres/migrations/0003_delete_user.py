# Generated by Django 3.1 on 2020-09-18 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membres', '0002_delete_abonne'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]