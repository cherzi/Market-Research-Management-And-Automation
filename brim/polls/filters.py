import django_filters
from .models import *
from django_filters import DateFilter

class SondageFilter(django_filters.FilterSet):

	class Meta:
		model = Sondage
		fields = {'client', 'statut'}