from django.urls import path
from . import views
from .views import *

app_name = 'polls'

urlpatterns = [

	path('sondages/', views.sondages, name="sondages"),
	path('', views.nosSondages, name="nossondages"),
	path('sondage/<str:pk>/', views.unSondage, name="unsondage"),
	path('sondage/<str:pk>/resultat', views.resultat, name="resultat"),
	path('archiver/<str:pk>/', views.archiver, name='archiver'),
	path('activer/<str:pk>/', views.activer, name='activer'),
	
	#path('inscrire/', InscrireView.as_view(), name="inscrire"),
	# path('inscrire/', views.inscrire, name="inscrire"),

]