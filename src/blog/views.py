from django.shortcuts import render
from django.http import Http404
from .models import Article



def blog_list_view(request):
    queryset = Article.objects.all()
    context = {
        'blog_list': queryset
    }
    return render(request, 'blog/article_list.html', context)


def blog_detail_view(request):
    object = Article.objects.get(id=1)
    
    context = {
        'article_object': object
    }
    return render(request, 'blog/article_detail.html', context)


def dynamic_look_view(request, id):
    try:
        object = Article.objects.get(id=id)
    except Article.DoesNotExist:
        raise Http404
    
    context = {
        'object': object
    }
    return render(request, 'blog/article_detail', context)