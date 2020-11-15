from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .forms import EditProfilForm, PasswordChangingForm
from django.urls import reverse_lazy
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .decorators import *
from django.utils.decorators import method_decorator
from django.contrib.auth.models import Group, User
from django.contrib.auth.views import PasswordChangeView
from .models import AbonneProfile



def class_view_decorator(function_decorator):
    def deco(View):
        View.dispatch = method_decorator(function_decorator)(View.dispatch)
        return View
    return deco


# @class_view_decorator(nonconnecte_user)
# class InscrireView(generic.CreateView):
# 	form_class = SignUpForm

# 	template_name = 'registration/inscrire.html'
# 	success_url = reverse_lazy('login')
@nonconnecte_user
def inscrire(request):
	if request.user.is_authenticated:
		return redirect('homepage:home')
	else:
		form = SignUpForm()
		if request.method == 'POST':
			form = SignUpForm(request.POST)
			if form.is_valid():
				user = form.save()
				profil = AbonneProfile(user = user, points = 0)
				profil.save()
				group = Group.objects.get(name='Abonné')
				user.groups.add(group)
				user = form.cleaned_data.get('username')
				messages.success(request, 'Compte créé pour ' + user)
				

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'registration/inscrire.html', context)




class ModifierProfilView(generic.UpdateView):
	form_class = EditProfilForm
	template_name = 'registration/profil.html'

	# user1 = User.objects.get(username=user.username)
	# abonne = AbonneProfil.objects.get(user=user1)

	success_url = reverse_lazy('homepage:home')


	def get_object(self):
		return self.request.user


class PasswordsChangeView(PasswordChangeView):
	form_class = PasswordChangingForm
	success_url = reverse_lazy('membres:profil')




@nonconnecte_user
def loginPage(request):
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('homepage:home')
			else:
				messages.info(request, 'Mot de passe ou username incorrect')

		context = {}
		return render(request, 'registration/login.html', context)


def users(request):

	abonneliste = User.objects.filter(groups__name='Abonné')
	delegueliste = User.objects.filter(groups__name='Délégué')
	context = {'abonneliste':abonneliste, 'delegueliste': delegueliste}

	return render(request, 'registration/users.html', context)


def creerAbonne(request):

	form = SignUpForm()

	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			group = Group.objects.get(name='Abonné')
			user.groups.add(group)
			return redirect('/membres/')

	context = {'form': form}
	return render(request, 'registration/creerabonne.html', context)


def creerDelegue(request):

	form = SignUpForm()

	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			group = Group.objects.get(name='Délégué')
			user.groups.add(group)
			return redirect('/membres/')

	context = {'form': form}
	return render(request, 'registration/creerabonne.html', context)
