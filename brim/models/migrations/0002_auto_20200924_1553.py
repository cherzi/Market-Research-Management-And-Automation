# Generated by Django 3.1 on 2020-09-24 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='fichModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chemin', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='MlModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('nbvariables', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Variable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('valeur', models.IntegerField(default=0)),
                ('modelml', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='models.mlmodel')),
            ],
        ),
        migrations.DeleteModel(
            name='Model',
        ),
        migrations.AddField(
            model_name='fichmodel',
            name='modelml',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='models.mlmodel'),
        ),
    ]