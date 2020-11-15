from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Article
from .forms import ArticleForm
from django.urls import reverse_lazy
from membres.decorators import *
from django.utils.decorators import method_decorator



def class_view_decorator(function_decorator):
    def deco(View):
        View.dispatch = method_decorator(function_decorator)(View.dispatch)
        return View
    return deco



class ArticlesView(ListView):
	model = Article
	template_name = 'blog/listeArticles.html'
	ordering = ['-date_pub']


class ArticleDetailView(DetailView):
	model = Article
	template_name = 'blog/articleDetail.html'



@class_view_decorator(connecte_user)
@class_view_decorator(allowed_users(allowed_roles=['Admin']))
class AjoutArticleView(CreateView):
	model = Article
	form_class = ArticleForm
	template_name = 'blog/ajoutArticle.html'


@class_view_decorator(connecte_user)
@class_view_decorator(allowed_users(allowed_roles=['Admin']))
class ModifierArticleView(UpdateView):
	model = Article
	form_class = ArticleForm
	template_name = 'blog/modifierArticle.html'
	#fields = ['title', 'body']


@class_view_decorator(connecte_user)
@class_view_decorator(allowed_users(allowed_roles=['Admin']))
class SupprimerArticleView(DeleteView):
	model = Article
	template_name = 'blog/supprimerArticle.html'
	success_url = reverse_lazy('blog:listeArticles')
	
		
		
