from django.urls import path
from . import views
from .views import ModifierProfilView, PasswordsChangeView
from django.contrib.auth import views as auth_views

app_name = 'membres'

urlpatterns = [
	#path('inscrire/', InscrireView.as_view(), name="inscrire"),
	path('inscrire/', views.inscrire, name="inscrire"),
	#path('profil/', views.profil, name="profil"),
	path('profil/', ModifierProfilView.as_view(), name="profil"),
	path('login', views.loginPage, name="login"),
	path('', views.users, name="users"),
	path('creerabonne', views.creerAbonne, name="creerabonne"),
	path('creerdelegue', views.creerDelegue, name="creerdelegue"),
	path('password/', PasswordsChangeView.as_view(template_name ='registration/changepassword.html')),
]