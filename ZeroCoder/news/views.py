from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import News


class NewsListView(ListView):
    model = News
    template_name = 'news/news_list.html'
    context_object_name = 'news_list'


class NewsDetailView(DetailView):
    model = News
    template_name = 'news/news_detail.html'
    context_object_name = 'news'