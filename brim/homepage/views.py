from django.shortcuts import render
from membres.decorators import *




def home(request):
	return render(request, 'homepage/home.html')

@nonconnecte_user
def contact(request):
	return render(request, 'homepage/contact.html')