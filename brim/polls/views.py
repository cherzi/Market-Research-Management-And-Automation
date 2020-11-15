from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from membres.decorators import *
from .filters import *
from django.db.models import Count
from django.shortcuts import get_object_or_404
from membres.models import AbonneProfile




# @connecte_user
# @allowed_users(allowed_roles=['Admin'])
def sondages(request):

	sondageliste = Sondage.objects.all()
	myFilter = SondageFilter(request.GET, queryset=sondageliste)
	sondageliste = myFilter.qs

	context =  {'sondageliste': sondageliste, 'myFilter':myFilter}

	return render(request, 'polls/sondages.html', context)


def nosSondages(request):

	liste_sondages = Sondage.objects.filter(statut='Actif').order_by('-date_creation').annotate(nb = Count('question'))

	context = {'liste_sondages': liste_sondages}
	return render(request, 'polls/nossondages.html', context)


def unSondage(request, pk):

	try:
		sondage = Sondage.objects.get(pk=pk)
		questions = sondage.question_set.all()
		context = {'sondage': sondage, 'questions':questions}
	except Sondage.DoesNotExist:
		raise Http404("Sondage n'existe pas")


	if request.method == 'POST':
		form = request.POST
		nbquestions = questions.count()
		
		i=1
		for question in questions:
			choix = question.choix_set.get(pk = request.POST[str(i)])
			choix.nbreponses += 1
			i += 1
			choix.save()
		
		sondage.nbreponses += 1
		sondage.personnes.add(request.user)
		userx = request.user

		#profil = AbonneProfile(user = request.user)
		profil = userx.abonneprofile_set.all()[0]
		profil.points += 10
		# for prof in profil:
		# 	prof.save()

		profil.save()

		print(profil.points)

		sondage.save()
		return redirect('/polls')




	return render(request, 'polls/unsondage.html', context)


def resultat(request, pk):

	sondage = get_object_or_404(Sondage, pk=pk)
	questions = sondage.question_set.all()
	context = {'sondage': sondage, 'questions': questions}
	return render(request, 'polls/sondage.html', context)

def archiver(request, pk):

	sondage = get_object_or_404(Sondage, pk=pk)
	sondage.statut = 'Archive'
	sondage.save()
	questions = sondage.question_set.all()
	context = {'sondage':sondage, 'questions': questions}
	return render(request, 'polls/sondage.html', context)


def activer(request, pk):

	sondage = get_object_or_404(Sondage, pk=pk)
	sondage.statut = 'Actif'
	sondage.save()
	questions = sondage.question_set.all()
	context = {'sondage':sondage, 'questions': questions}
	return render(request, 'polls/sondage.html', context)




