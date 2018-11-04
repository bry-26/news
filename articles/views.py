from django.shortcuts import render
from django.utils import timezone
from django.views.generic.list import ListView

from articles.models import Article


class ArticleListView(ListView):
    model = Article
    queryset = Article.objects.filter()[:20]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
