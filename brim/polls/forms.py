from .models import *
from django import forms


# class SondageForm(forms.ModelForm):

# 	name = forms.CharField(required=True)

# 	class Meta:
# 		model = Sondage


# 	def __init__(self, *args, **kwargs):

# 		super().__init__(*args, **kwargs)
# 		questions = Question.objects.filter(
# 			sondage = self.instance
# 		)

# 		for i in range(len(questions) + 1):
# 			field_name = 'Question_%s' % (i,)
# 			self.fields[field_name] = forms.CharField(required=False)
# 			try:
# 				self.initial[field_name] = questions[i].text_q
# 			except IndexError:
#                 self.initial[field_name] = ""


#         field_name = 'Question_%s' % (i + 1,)
#         self.fields[field_name] = forms.CharField(required=False)



#     def clean(self):

#         questions = set()
#         i = 0
#         field_name = 'Question_%s' % (i,)
#         while self.cleaned_data.get(field_name):
#            question = self.cleaned_data[field_name]
#            if question in questions:
#                self.add_error(field_name, 'Duplicate')
#            else:
#                questions.add(question)
#            i += 1
#            field_name = 'Question_%s' % (i,)
#        self.cleaned_data[questions] = questions



#     def save(self):
#         sondage = self.instance
#         sondage.name = self.cleaned_data["name"]

#         sondage.question_set.all().delete()

#         for question in self.cleaned_data["questions"]:
#            Question.objects.create(
#                sondage = sondage,
#                text_q = question,
#            )


#     def get_question_fields(self):
#     for field_name in self.fields:
#         if field_name.startswith(‘question_’):
#             yield self[field_name]