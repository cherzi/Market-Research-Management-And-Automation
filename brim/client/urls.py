from django.urls import path, include
from . import views

app_name = 'client'
urlpatterns = [
	
	path('', views.clients, name="clients"),
	path('commandes/', views.commandes, name="commandes"),
	path('client/<str:pk>/', views.clientDetail, name="client"),
	path('creercommande', views.creerCommande, name="creercommande"),
	path('creercommandes/<str:pk>/', views.creerCommandes, name="creercommandes"),
	path('modifiercommande/<str:pk>/', views.modifierCommande, name="modifiercommande"),
	path('supprimercommande/<str:pk>/', views.supprimerCommande, name="supprimercommande"),
	path('creerclient', views.creerClient, name="creerclient"),
	path('modifierclient/<str:pk>/', views.modifierClient, name="modifierclient"),
	path('supprimerclient/<str:pk>/', views.supprimerClient, name="supprimerclient"),
	
]

