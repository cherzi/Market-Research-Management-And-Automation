from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager



class AbonneProfile(models.Model):

	user = models.ForeignKey("auth.User", limit_choices_to={'groups__name': "Abonné"}, on_delete=models.CASCADE, null=True, blank=True)
	profile_pic = models.ImageField(null=True, blank=True)
	points = models.IntegerField(default = 0)


	
# class User(AbstractBaseUser):

# 	email = models.EmailField(verbose_name="email", max_length=60, unique=True)
# 	username = models.CharField(max_length=30, unique=True)
# 	is_client = models.BooleanField(default=False)
# 	is_abonne = models.BooleanField(default=False)
# 	date_naissance = models.DateTimeField()

# 	def __str__(self):
# 		return self.username


# class Abonne(models.Model):
# 	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


