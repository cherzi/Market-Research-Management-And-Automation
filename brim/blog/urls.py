from django.urls import path
from .views import ArticlesView, ArticleDetailView, AjoutArticleView, ModifierArticleView, SupprimerArticleView


app_name = 'blog'
urlpatterns = [
	# path('', views.listeArticles, name='listeArticles'),
	path('', ArticlesView.as_view(), name ="listeArticles"),
	path('article/<int:pk>', ArticleDetailView.as_view(), name="articleDetail"),
	path('ajouter', AjoutArticleView.as_view(), name="ajoutArticle"),
	path('article/modifier/<int:pk>', ModifierArticleView.as_view(), name="modifierArticle"),
	path('article/<int:pk>/supprimer', SupprimerArticleView.as_view(), name="supprimerArticle"),
]