from django.urls import path
from . import views
from .views import ClientChartView


app_name = 'dashboard'
urlpatterns = [
	#path('', views.dashboard, name='dashboard'),
	path('', ClientChartView.as_view(), name="clientdash")
]