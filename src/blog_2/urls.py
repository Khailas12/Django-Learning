from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView
)


app_name = 'article'
urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('createblog/', ArticleCreateView.as_view(), name='article-create'),
    path('<int:pk>/', ArticleDetailView.as_view(),
         name='article-detail'),    # pk = primary key
    path('<int:id>/update', ArticleUpdateView.as_view(), name='article-update'),
]
