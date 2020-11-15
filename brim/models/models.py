from django.db import models


class MlModel(models.Model):

	name = models.CharField(max_length=200)
	nbvariables = models.IntegerField(default=0)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)


class FichModel(models.Model):

	modelml = models.ForeignKey(MlModel, on_delete=models.CASCADE, null=True)
	chemin = models.CharField(max_length=300)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)


class Variable(models.Model):

	name = models.CharField(max_length=200)
	modelml = models.ForeignKey(MlModel, on_delete=models.CASCADE, null=True)


	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
