from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
	class Meta:
		model = Article
		fields = ('title', 'author', 'body')

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Premier article'}),
			'author': forms.Select(attrs={'class': 'form-control'}),
			'body': forms.Textarea(attrs={'class': 'form-control'}),
		}
		