from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from django.utils import timezone



class Client(models.Model):

	NAME = models.CharField(max_length=200, null=True)
	VISAGE = models.ForeignKey("auth.User", limit_choices_to={'groups__name': "Délégué"}, on_delete=models.CASCADE, null=True, blank=True)
	PHONE = models.CharField(max_length=200, null=True)
	EMAIL = models.CharField(max_length=200, null=True)

	STATUT_CHOICES = (
		('Actif','actif'),
		('Inactif','inactif')
	)

	DATE_CREATION = models.DateTimeField(default=timezone.now, null=True)
	STATUT = models.CharField(max_length=200, choices = STATUT_CHOICES, default='Actif', null=True)

	def __str__(self):
		return self.NAME





class Commande(models.Model):

	TITRE = models.CharField(max_length=200, null=True)
	AUTEUR = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
	DATE_CREATION = models.DateTimeField(default=timezone.now, null=True)
	DATE_ECHEANCE = models.DateTimeField(null=True)
	DESCRIPTION = models.TextField(null=True, blank=True)

	CATEGORY_CHOICES = (
		('Prédiction de prix', 'prediction_prix'),
		('Segmentation des clients', 'seg_client'),
		('Sondages','sondage'),
	)

	STATUT_CHOICES = (
		('En attente','en_attente'),
		('En cours', 'en_cours'),
		('Finie','finie'),
	)

	CATEGORY = models.CharField(max_length=200, choices = CATEGORY_CHOICES, null=True)
	STATUT = models.CharField(max_length=200, choices = STATUT_CHOICES, default='en_attente', null=True)

	
