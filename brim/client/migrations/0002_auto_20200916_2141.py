# Generated by Django 3.1 on 2020-09-16 20:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='DATE_CREATION',
            field=models.DateField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='STATUT',
            field=models.CharField(choices=[('Actif', 'actif'), ('Inactif', 'inactif')], default='Actif', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='commande',
            name='CATEGORY',
            field=models.CharField(choices=[('Prédiction de prix', 'prediction_prix'), ('Segmentation des clients', 'seg_client'), ('Sondages', 'sondage')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='commande',
            name='DATE_CREATION',
            field=models.DateField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='commande',
            name='DATE_ECHEANCE',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='commande',
            name='DESCRIPTION',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='commande',
            name='STATUT',
            field=models.CharField(choices=[('En attente', 'en_attente'), ('En cours', 'en_cours'), ('Finie', 'finie')], default='en_attente', max_length=200, null=True),
        ),
    ]
