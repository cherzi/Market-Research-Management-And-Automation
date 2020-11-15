from django import forms

class PrixMobilesForm(forms.Form):

	battery_power = forms.IntegerField(required=False)
	blue = forms.ChoiceField(required=False, label='Bluetooth', choices = [(0,'NO'), (1, 'YES')])
	clock_speed = forms.FloatField(required=False)
	dual_sim = forms.ChoiceField(required=False, label='Double Sim', choices = [(0,'NO'), (1, 'YES')])
	fc = forms.ChoiceField(required=False, label='Camera avant', choices = [(i,i) for i in range(21)])
	four_g = forms.ChoiceField(required=False, label='4G', choices = [(0,'NO'), (1, 'YES')])
	int_memory = forms.IntegerField(required=False, label='Taille mémoire')
	m_dep = forms.FloatField(required=False, label='Profondeur')
	mobile_wt = forms.IntegerField(required=False, label='Poids')
	n_cores	= forms.ChoiceField(required=False, label='Nombre de coeurs', choices = [(i,i) for i in range(11)])
	pc = forms.ChoiceField(required=False, label='Caméra principale',choices = [(i,i) for i in range(21)])
	px_height = forms.IntegerField(required=False, label='Résolution hauteur')
	px_width = forms.IntegerField(required=False, label='Résolution largeur')
	ram	= forms.IntegerField(required=False, label='RAM')
	sc_h = forms.ChoiceField(required=False, label='Hauteur en cm', choices = [(i,i) for i in range(21)])
	sc_w = forms.ChoiceField(required=False, label='Largeur en cm',choices = [(i,i) for i in range(21)])
	talk_time = forms.ChoiceField(required=False, label='Durée de batterie pendant un appel',choices = [(i,i) for i in range(21)])
	three_g = forms.ChoiceField(required=False, label='3G',choices = [(0,'NO'), (1, 'YES')])
	touch_screen = forms.ChoiceField(required=False, label='Touch Screen',choices = [(0,'NO'), (1, 'YES')])
	wifi = forms.ChoiceField(required=False, label='Wifi',choices = [(0,'NO'), (1, 'YES')])



	def __init__(self, *args, **kwargs):
		super(PrixMobilesForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs.update({'class':'form-control'})



class PrixMaisonsForm(forms.Form):

	file = forms.FileField(label='Données de la maison')

	def __init__(self, *args, **kwargs):
		super(PrixMaisonsForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs.update({'class':'form-control'})


class PrixVoituresForm(forms.Form):

	file = forms.FileField(label='Données de la voiture')

	def __init__(self, *args, **kwargs):
		super(PrixVoituresForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs.update({'class':'form-control'})


class NouveauModelPrixForm(forms.Form):

	name = forms.CharField(max_length=200)
	file = forms.FileField(label='Fichier d\'entrainement')
	# pred = forms.FileField(label='Les données à prédire')
	# type_model = forms.ChoiceField(required=False, label='Type du modèle', choices = [('reg','Linear Regression'), 
	# 	('forest', 'Random Forest Regression'), ('tree', 'Decision Tree Regression')])

	def __init__(self, *args, **kwargs):
		super(NouveauModelPrixForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs.update({'class':'form-control'})


class ClientSegForm(forms.Form):

	file = forms.FileField(label='Fichier des données des clients', required=False)

	def __init__(self, *args, **kwargs):
		super(ClientSegForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs.update({'class':'form-control'})


class AnalyseSentimentForm(forms.Form):

	file = forms.FileField(label='Texte à analyser', required=False)

	def __init__(self, *args, **kwargs):
		super(AnalyseSentimentForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs.update({'class':'form-control'})

