from django import forms
from .models import *


class CommandeForm(forms.ModelForm):
	class Meta:

		model = Commande
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super(CommandeForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs.update({'class':'form-control'})


class ClientForm(forms.ModelForm):
	class Meta:

		model =  Client
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super(ClientForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs.update({'class':'form-control'})
