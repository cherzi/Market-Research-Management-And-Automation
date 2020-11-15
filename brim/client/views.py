from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.forms import inlineformset_factory
from .filters import *
from membres.decorators import *


@connecte_user
@allowed_users(allowed_roles=['Admin'])
def clients(request):

	clientliste = Client.objects.all()
	myFilter = ClientFilter(request.GET, queryset=clientliste)
	clientliste = myFilter.qs

	context =  {'clientliste': clientliste, 'myFilter':myFilter}

	return render(request, 'client/clients.html', context)


@connecte_user
@allowed_users(allowed_roles=['Admin'])
def commandes(request):

	commandeliste = Commande.objects.all()
	nbcommandes = commandeliste.count()
	enattente = commandeliste.filter(STATUT='En attente').count()
	encours = commandeliste.filter(STATUT='En cours').count()

	myFilter = CommandeFilter(request.GET, queryset=commandeliste)
	commandeliste = myFilter.qs

	context = {'commandeliste':commandeliste, 'nbcommandes':nbcommandes, 'encours':encours,'enattente':enattente, 'myFilter':myFilter}
	return render(request, 'client/commandes.html', context)


@connecte_user
@allowed_users(allowed_roles=['Admin', 'Délégué'])

def clientDetail(request, pk):
	client = Client.objects.get(id=pk)

	commandes = client.commande_set.all()
	nbcommandes = commandes.count()

	myFilter = CommandeFilter(request.GET, queryset=commandes)
	commandes = myFilter.qs

	context = {'client': client, 'commandes':commandes, 'nbcommandes': nbcommandes, 'myFilter': myFilter}
	return render(request, 'client/client.html', context)


@connecte_user
@allowed_users(allowed_roles=['Admin'])
def creerCommande(request):

	form = CommandeForm()

	if request.method == 'POST':
		form = CommandeForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/client/commandes')

	context = {'form': form}
	return render(request, 'client/commande.html', context)


@connecte_user
@allowed_users(allowed_roles=['Admin', 'Délégué'])
def creerCommandes(request, pk):

	client = Client.objects.get(id=pk)
	form = CommandeForm(initial={'AUTEUR': client})

	if request.method == 'POST':
		form = CommandeForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('client:client', pk = pk)

	context = {'form': form}
	return render(request, 'client/commande.html', context)



@connecte_user
@allowed_users(allowed_roles=['Admin', 'Délégué'])
def modifierCommande(request, pk):

	commande = Commande.objects.get(id=pk)
	form = CommandeForm(instance=commande)

	if request.method == 'POST':
		form = CommandeForm(request.POST, instance=commande)
		if form.is_valid():
			form.save()
			return redirect('/client/commandes')


	context = {'form': form}
	return render(request, 'client/commande.html', context)


@connecte_user
@allowed_users(allowed_roles=['Admin', 'Délégué'])
def supprimerCommande(request, pk):

	commande = Commande.objects.get(id=pk)

	if request.method == 'POST':
		commande.delete()
		return redirect('/client/commandes')

	name = 'la commande'
	context = {'item': commande, 'name': name}
	return render(request, 'client/supprimer.html', context)


@connecte_user
@allowed_users(allowed_roles=['Admin'])
def creerClient(request):

	form = ClientForm()

	if request.method == 'POST':
		form = ClientForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/client/')

	context = {'form': form}
	return render(request, 'client/creerclient.html', context)


@connecte_user
@allowed_users(allowed_roles=['Admin'])
def modifierClient(request, pk):

	client = Client.objects.get(id=pk)
	form = ClientForm(instance=client)

	if request.method == 'POST':
		form = ClientForm(request.POST, instance=client)
		if form.is_valid():
			form.save()
			return redirect('client:client', pk=pk)

	context = {'form': form}
	return render(request, 'client/creerclient.html', context)


@connecte_user
@allowed_users(allowed_roles=['Admin'])
def supprimerClient(request, pk):

	client = Client.objects.get(id=pk)

	if request.method == 'POST':
		client.delete()
		return redirect('/client/')

	context = {'client': client}
	return render(request, 'client/supprimerclient.html', context)



