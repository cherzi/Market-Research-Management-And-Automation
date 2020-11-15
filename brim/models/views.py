from django.shortcuts import render, redirect
from django.urls import reverse
from membres.decorators import *
from django.utils.decorators import method_decorator
from django.views.generic import FormView, TemplateView
from .forms import PrixMobilesForm, PrixMaisonsForm, PrixVoituresForm, NouveauModelPrixForm, ClientSegForm, AnalyseSentimentForm
import numpy as np
import pandas as pd
import pickle
import joblib
import uuid
from django.http import JsonResponse
from sklearn.preprocessing import MinMaxScaler
import csv, io
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
import time
import pickle
from .models import *
import operator
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from itertools import cycle



def class_view_decorator(function_decorator):
    def deco(View):
        View.dispatch = method_decorator(function_decorator)(View.dispatch)
        return View
    return deco


@connecte_user
@allowed_users(allowed_roles=['Admin'])
def allModels(request):

	allmodels = MlModel.objects.all()
	context= {'allmodels': allmodels}
	return render(request, 'models/allModels.html', context)

@connecte_user
@allowed_users(allowed_roles=['Admin'])
def modelChoix(request):
	return render(request, 'models/modelchoix.html')

@connecte_user
@allowed_users(allowed_roles=['Admin'])
def AdminArea(request):
	return render(request, 'models/adminArea.html')


@class_view_decorator(connecte_user)
@class_view_decorator(allowed_users(allowed_roles=['Admin']))
class PrixMobiles(FormView):

	template_name = 'models/formPrixMobiles.html'

	def get(self, request):
		form = PrixMobilesForm()
		return render(request, self.template_name, {'form':form})

	def post(self, request):
		form = PrixMobilesForm(request.POST)

		if 'file' in request.FILES:
			csv_file = request.FILES['file']
			file_data = csv_file.read().decode('UTF-8')

			fields = file_data.split(";")
			data = fields
			
		else:
			data = [
				request.POST['battery_power'], 
				request.POST['blue'], 
				request.POST['clock_speed'], 
				request.POST['dual_sim'],
				request.POST['fc'],
				request.POST['four_g'], 
				request.POST['int_memory'], 
				request.POST['m_dep'], 
				request.POST['mobile_wt'],
				request.POST['n_cores'],
				request.POST['pc'], 
				request.POST['px_height'], 
				request.POST['px_width'],
				request.POST['ram'],
				request.POST['sc_h'],
				request.POST['sc_w'],
				request.POST['talk_time'],
				request.POST['three_g'],
				request.POST['touch_screen'],
				request.POST['wifi']
			]

		tab = np.array(data)
		data2 = tab.reshape(1, -1)
		modelReg = joblib.load("C:/Users/DELL/Desktop/monprojet/brim/models/model_prix_mobiles.pkl")
		df = pd.DataFrame(data2)
		y_pred = modelReg.predict(df)

		y_pred = np.around(y_pred)

		args = {'form': form, 'y_pred': y_pred}
		return render(request, self.template_name, args)



@class_view_decorator(connecte_user)
@class_view_decorator(allowed_users(allowed_roles=['Admin']))
class PrixMaisons(FormView):
	#form_class = PrixMobilesForm
	template_name = 'models/formPrixMaisons.html'

	def get(self, request):
		form = PrixMaisonsForm()
		return render(request, self.template_name, {'form':form})

	def post(self, request):
		form = PrixMaisonsForm(request.POST)
		
		csv_file = request.FILES['file']
		file_data = csv_file.read().decode('UTF-8')
			#lines = file_data.split("\n")

		fields = file_data.split(";")

		tab = np.array(fields)
		data2 = tab.reshape(1, -1)
		modelRF = joblib.load("C:/Users/DELL/Desktop/monprojet/brim/models/model_prix_maisons.pkl")
		df = pd.DataFrame(data2)
		y_pred = modelRF.predict(df)
		
		args = {'form': form, 'y_pred': y_pred }
		return render(request, self.template_name, args)



@class_view_decorator(connecte_user)
@class_view_decorator(allowed_users(allowed_roles=['Admin']))
class PrixVoitures(FormView):

	template_name = 'models/formPrixVoitures.html'

	def get(self, request):
		form = PrixVoituresForm()
		return render(request, self.template_name, {'form':form})

	def post(self, request):
		form = PrixVoituresForm(request.POST)
		
		csv_file = request.FILES['file']
		file_data = csv_file.read().decode('UTF-8')

		fields = file_data.split(";")

		tab = np.array(fields)
		data2 = tab.reshape(1, -1)
		modelRF = joblib.load("C:/Users/DELL/Desktop/monprojet/brim/models/model_prix_voitures.pkl")
		df = pd.DataFrame(data2)
		y_pred = modelRF.predict(df)
		
		args = {'form': form, 'y_pred': y_pred }
		return render(request, self.template_name, args)


	

@class_view_decorator(connecte_user)
@class_view_decorator(allowed_users(allowed_roles=['Admin']))
class NouveauModelPrix(FormView):

	template_name = 'models/nouveauModelPrix.html'

	def get(self, request):
		form = NouveauModelPrixForm()
		return render(request, self.template_name, {'form':form})

	def post(self, request):

		form = NouveauModelPrixForm(request.POST)
		#time.sleep(10)

		fichier_ent = request.FILES.get('file', False)
		df = pd.read_csv(fichier_ent)

		df = df[df.columns.drop(list(df.filter(regex='Name')))]

		if operator.contains(df.columns[0], "ID") or operator.contains(df.columns[0], "id") or operator.contains(df.columns[0], "Id"):
			df = df.drop(df.columns[0], axis=1)

		# cleaning

		#get and drop high correlated features
		corr_matrix = df.corr().abs()
		upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(np.bool))
		to_drop = [column for column in upper.columns if any(upper[column] > 0.95)]
		print(to_drop)
		df = df.drop(df[to_drop], axis=1)


		#drop features with low correlation with price
		correlated_features = set()

		for i in range(len(corr_matrix.columns)):
			if abs(corr_matrix.iloc[i, len(corr_matrix.columns)-1]) < 0.1:
				colname = corr_matrix.columns[i]
				correlated_features.add(colname)

		df.drop(labels=correlated_features, axis=1, inplace=True)

		#transform non numeric into dummy variables
		todummy_list = df.select_dtypes(exclude=['number']).columns

		for x in todummy_list:
			dummies = pd.get_dummies(df[x], prefix=x, dummy_na=False)
			df = df.drop(x, 1)
			df = pd.concat([df, dummies], axis=1)

		X = df.drop('price',axis=1)
		y = df['price']

		X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42, shuffle=True)

		# #Decision tree
		AD = DecisionTreeRegressor()
		AD.fit(X_train, y_train)

		#Random Forest
		rf = RandomForestRegressor(max_depth=10, random_state=42,criterion='mse',n_estimators=90,min_samples_leaf=2)
		rf.fit(X_train,y_train)

		#Linear Regression
		reg = LinearRegression()
		reg.fit(X_train,y_train)

		nbvar = len(X_train.columns)

		mod = MlModel(name = request.POST['name'], nbvariables = nbvar)
		mod.save()

		for col in X.columns:
			var = Variable(name = col, modelml=mod)
			var.save()

		fichier_reg = 'mods/linear_reg_'+str(uuid.uuid4())+'.pkl'
		joblib.dump(reg, fichier_reg)
		fichmodelReg =  FichModel(chemin = fichier_reg, modelml = mod)
		fichmodelReg.save()

		fichier_rf = 'mods/linear_rf_'+str(uuid.uuid4())+'.pkl'
		joblib.dump(rf, fichier_rf)
		fichmodelRf =  FichModel(chemin = fichier_rf, modelml = mod)
		fichmodelRf.save()

		fichier_dt = 'mods/linear_dt_'+str(uuid.uuid4())+'.pkl'
		joblib.dump(AD, fichier_dt)
		fichmodelDt =  FichModel(chemin = fichier_dt, modelml = mod)
		fichmodelDt.save()

		return redirect('/models/allmodels')


@connecte_user
@allowed_users(allowed_roles=['Admin'])
def newPrix(request, pk):

	algo = MlModel.objects.get(id=pk)

	fichiers = algo.fichmodel_set.all()
	variables = algo.variable_set.all()

	chemin_reg = fichiers.filter(chemin__startswith='mods/linear_reg') 
	chemin_dt = fichiers.filter(chemin__startswith='mods/linear_dt') 
	chemin_rf = fichiers.filter(chemin__startswith='mods/linear_rf') 

	if request.method == 'POST':

		fichier_reg = joblib.load(chemin_reg[0].chemin)
		fichier_dt = joblib.load(chemin_dt[0].chemin)
		fichier_rf = joblib.load(chemin_rf[0].chemin)
		data = []

		if 'file' in request.FILES:
			csv_file = request.FILES['file']
			file_data = csv_file.read().decode('UTF-8')

			fields = file_data.split(";")
			data = fields
			
		else:
			for var in variables:
				data.append(request.POST[var.name])


		tab = np.array(data)
		data2 = tab.reshape(1, -1)
		df = pd.DataFrame(data2)

		y_pred_reg = fichier_reg.predict(df)
		y_pred_dt = fichier_dt.predict(df)
		y_pred_rf = fichier_rf.predict(df)

		average = float((float(y_pred_reg) + float(y_pred_rf) + float(y_pred_dt))/3)
		print(average)

		context = {'average': average}
		return render(request, 'models/success.html', context)


	context = {'algo':algo, 'variables':variables}
	return render(request, 'models/new.html', context)


@connecte_user
@allowed_users(allowed_roles=['Admin'])
def success(request):
	return render(request, 'models/success.html')



@class_view_decorator(connecte_user)
@class_view_decorator(allowed_users(allowed_roles=['Admin']))
class SegClient(FormView):

	template_name = 'models/segclient.html'

	def get(self, request):
		form = ClientSegForm()
		return render(request, self.template_name, {'form':form})

	def post(self, request):
		form = ClientSegForm(request.POST)
		
		csv_file = request.FILES['file']
		df = pd.read_csv(csv_file)

		#k = request.POST['clusters']

		df = df._get_numeric_data()

		if operator.contains(df.columns[0], "ID") or operator.contains(df.columns[0], "id") or operator.contains(df.columns[0], "Id"):
			df = df.drop(df.columns[0], axis=1)

		wcss = []

		for k in range(1,11):
			kmeans = KMeans(n_clusters=k, init="k-means++", random_state = 0)
			kmeans.fit(df.iloc[:,1:])
			wcss.append(kmeans.inertia_)

		#print(df.head())

		plt.figure(figsize=(12,6)) 
		plt.plot(range(1, 11), wcss, linewidth=2, marker ="8")
		plt.title('The Elbow Point Graph')
		plt.xlabel('Number of clusters')
		plt.ylabel('WCSS')
		plt.show()

		plt.close()
		
		#args = {'form': form}
		#return render(request, self.template_name, args)
		return redirect('models:segclientk')


@connecte_user
@allowed_users(allowed_roles=['Admin'])
def segClientK(request):

	if request.method == 'POST':

		k = request.POST['k']
		csv_file = request.FILES['file']
		df = pd.read_csv(csv_file)


		df = df._get_numeric_data()

		if operator.contains(df.columns[0], "ID") or operator.contains(df.columns[0], "id") or operator.contains(df.columns[0], "Id"):
			df = df.drop(df.columns[0], axis=1)

		km = KMeans(n_clusters=int(k), init = 'k-means++', random_state = 42)
		clusters = km.fit_predict(df.iloc[:,0:])
		df["label"] = clusters


		fig = plt.figure(figsize=(20,10))
		ax = fig.add_subplot(111, projection='3d')

		cycol = cycle('bgrcmk')

		for i in range(int(k)):
			ax.scatter(df.iloc[:, 0][df.label == i], df.iloc[:, 1][df.label == i], df.iloc[:, 2][df.label == i], c=next(cycol), s=60)


		# ax.scatter(df.iloc[:, 0][df.label == 0], df.iloc[:, 1][df.label == 0], df.iloc[:, 2][df.label == 0], c='blue', s=60)
		# ax.scatter(df.iloc[:, 0][df.label == 1], df.iloc[:, 1][df.label == 1], df.iloc[:, 2][df.label == 1], c='red', s=60)
		# ax.scatter(df.iloc[:, 0][df.label == 2], df.iloc[:, 1][df.label == 2], df.iloc[:, 2][df.label == 2], c='green', s=60)
		# ax.scatter(df.iloc[:, 0][df.label == 3], df.iloc[:, 1][df.label == 3], df.iloc[:, 2][df.label == 3], c='orange', s=60)
		# ax.scatter(df.iloc[:, 0][df.label == 4], df.iloc[:, 1][df.label == 4], df.iloc[:, 2][df.label == 4], c='purple', s=60)

		ax.view_init(30, 185)
		plt.xlabel("Age")
		plt.ylabel("Annual Income (k$)")
		ax.set_zlabel('Spending Score (1-100)')
		plt.show()

		plt.close(fig)

		return redirect('models:modelchoix')

	return render(request, 'models/segclientk.html')


@class_view_decorator(connecte_user)
@class_view_decorator(allowed_users(allowed_roles=['Admin']))
class AnalyseSentiment(FormView):

	template_name = 'models/analysesentiment.html'

	def get(self, request):
		form = AnalyseSentimentForm()
		return render(request, self.template_name, {'form':form})

	def post(self, request):
		form = AnalyseSentimentForm(request.POST)
		
		# csv_file = request.FILES['file']
		# file_data = csv_file.read().decode('UTF-8')

		# fields = file_data.split(";")

		# tab = np.array(fields)
		# data2 = tab.reshape(1, -1)
		# modelRF = joblib.load("C:/Users/DELL/Desktop/monprojet/brim/models/model_prix_voitures.pkl")
		# df = pd.DataFrame(data2)
		# y_pred = modelRF.predict(df)
		
		# args = {'form': form, 'y_pred': y_pred }
		return render(request, self.template_name)










	
