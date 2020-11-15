from django.contrib import admin

from .models import *
import nested_admin

admin.site.site_header = "Administration"
admin.site.site_title = "Ajouter un sondage"


class ChoixInline(nested_admin.NestedTabularInline):
	model = Choix
	extra = 1

class QuestionAdmin(nested_admin.NestedModelAdmin):
	fieldsets = [('Titre', {'fields': ['text_q']})]
	inlines = [ChoixInline]


class QuestionInline(nested_admin.NestedTabularInline):

	model = Question
	extra = 1
	inlines = [ChoixInline]

class SondageAdmin(nested_admin.NestedModelAdmin):

	#fieldsets = [(None, {'fields': ['name', 'date_creation', 'statut', 'nbreponses', 'personnes']}), ('Client', {'fields': ['client']})]
	fieldsets = [(None, {'fields': ['name', 'date_creation', 'statut']}), ('Client', {'fields': ['client']})]
	inlines = [QuestionInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Sondage, SondageAdmin)