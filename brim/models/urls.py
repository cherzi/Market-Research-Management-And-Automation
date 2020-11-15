from django.urls import path, include
from .views import allModels, PrixMobiles, PrixMaisons, PrixVoitures, NouveauModelPrix, AdminArea, SegClient, AnalyseSentiment
from . import views

app_name = 'models'
urlpatterns = [

	path('allmodels', views.allModels, name="allModels"),
	#path('prixmobiles', PrixMobiles.as_view(success_url="/models/predire"), name="formPrixMobiles"),
	path('prixmobiles', PrixMobiles.as_view(), name="formPrixMobiles"),
	path('prixmaisons', PrixMaisons.as_view(), name="formPrixMaisons"),
	path('prixvoitures', PrixVoitures.as_view(), name="formPrixVoitures"),
	path('modelchoix', views.modelChoix, name="modelchoix"),
	path('newmodelprix', NouveauModelPrix.as_view(), name="nouveauModelPrix"),
	path('', views.AdminArea, name="adminArea"),
	path('new/<str:pk>/', views.newPrix, name="new"),
	path('success/', views.success, name="success"),
	path('segclient/', SegClient.as_view(), name="segclient"),
	path('segclientk/', views.segClientK, name="segclientk"),
	path('analysesentiment', AnalyseSentiment.as_view(), name="analysesentiment")
	
]