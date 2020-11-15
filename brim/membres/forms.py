from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
	email = forms.EmailField(
		widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'exemple@exemple.com'})
	)

	first_name = forms.CharField(
		max_length=100,
		widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prénom'})
	)

	last_name = forms.CharField(
		max_length=100,
		widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de famille'})
	)

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs={'class':'form-control', 'placeholder': 'Username'}
		self.fields['password1'].widget.attrs={'class':'form-control', 'placeholder': 'Mot de passe'}
		self.fields['password2'].widget.attrs={'class':'form-control', 'placeholder': 'Confirmer le mot de passe'}


class AbonneForm(forms.ModelForm):

	class Meta:

		model = User
		fields = ('username', 'email', 'first_name', 'last_name')

	def __init__(self, *args, **kwargs):
		super(AbonneForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs.update({'class':'form-control'})


class EditProfilForm(UserChangeForm):
	
	username = forms.CharField(
		max_length=100,
		widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom d\'utilisateur'})
	)

	email = forms.EmailField(
		widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'exemple@exemple.com'})
	)

	first_name = forms.CharField(
		max_length=100,
		widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prénom'})
	)

	last_name = forms.CharField(
		max_length=100,
		widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de famille'})
	)

	class Meta:
		model = User
		#fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
		fields = ('username', 'first_name', 'last_name', 'email')


	def __init__(self, *args, **kwargs):
		super(EditProfilForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs.update({'class':'form-control'})



class PasswordChangingForm(PasswordChangeForm):

	old_password = forms.CharField(
		label = 'Ancien mot de passe',
		widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'Ancien mot de passe', 'name': 'ancien'})
	)

	new_password1 = forms.CharField(
		max_length=100,
		label = 'Nouveau mot de passe',
		widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'Nouveau mot de passe'})
	)

	new_password2 = forms.CharField(
		label = 'Confirmer le nouveau mot de passe',
		max_length=100,
		widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'Confirmer le mot de passe'})
	)

	class Meta:
		model = User
		fields = ('password', 'new_password1', 'new_password2')
