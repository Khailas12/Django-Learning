from django.shortcuts import render
from .models import Article
from django.views.generic import (
    CreateView, 
    DetailView, 
    ListView,
    UpdateView,
    DeleteView
)


class ArticleListView(ListView):
    template_name = 'blog/article_list.html'
    queryset = Article.objects.all()