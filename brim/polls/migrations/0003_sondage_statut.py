# Generated by Django 3.1 on 2020-09-19 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20200919_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='sondage',
            name='statut',
            field=models.CharField(choices=[('Brouillon', 'brouillon'), ('Actif', 'actif'), ('Archivé', 'archive')], default='Brouillon', max_length=200, null=True),
        ),
    ]
