import django_filters
from .models import *
from django_filters import DateFilter

class CommandeFilter(django_filters.FilterSet):

	date_debut = DateFilter(field_name="DATE_CREATION", lookup_expr='gte', label='Crée à partir du')
	date_fin = DateFilter(field_name="DATE_ECHEANCE", lookup_expr='gte', label='Date d\'échéance à partir du')

	class Meta:
		model = Commande
		fields = {'AUTEUR', 'STATUT', 'CATEGORY'}


class ClientFilter(django_filters.FilterSet):

	class Meta:

		model = Client
		fields = {'STATUT'}


