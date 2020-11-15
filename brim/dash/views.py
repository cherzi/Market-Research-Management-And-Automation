from django.shortcuts import render
from client.models import Client, Commande
from polls.models import Sondage
from django.views.generic import TemplateView


def dashboard(request):

	return render(request, 'dash/dashboard.html')



class ClientChartView(TemplateView):

	template_name = 'dash/clientdash.html'


	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["clients"] = Client.objects.all()
		context["commandes"] = Commande.objects.all()
		context["sondages"] = Sondage.objects.all()
		
		return context
