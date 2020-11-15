from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from client.models import Client
from datetime import datetime, date
from django.utils import timezone



class Sondage(models.Model):

	name = models.CharField(max_length=200)
	nbreponses = models.IntegerField(default=0)
	client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
	personnes = models.ManyToManyField("auth.User", limit_choices_to={'groups__name': "Abonné"}, null=True, blank=True)
	date_creation = models.DateTimeField(default=timezone.now, null=True)
	STATUT_CHOICES = (
		('Brouillon', 'brouillon'),
		('Actif','actif'),
		('Archivé','archive'),
	)

	statut = models.CharField(max_length=200, choices = STATUT_CHOICES, default='Brouillon', null=True)

	def __str__(self):
		return self.name



class Question(models.Model):

	text_q = models.CharField(max_length=200)
	sondage = models.ForeignKey(Sondage, on_delete=models.CASCADE, null=True)


	def __str__(self):
		return self.text_q


class Choix(models.Model):

	question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
	text_ch = models.CharField(max_length=200)
	nbreponses = models.IntegerField(default=0)

	def __str__(self):
		return self.text_ch





