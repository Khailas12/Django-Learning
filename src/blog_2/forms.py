from django import forms
from .models import Article


class ArticleModelForm(forms.ModelForm):
    class Meta:
        models = Article
        fields = [
            'title',
            'content',
            'written_by'
        ]