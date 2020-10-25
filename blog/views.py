from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Blog


class BlogListView(ListView):
	model = Blog


class BlogDetailView(DetailView):
	model = Blog


class BlogCreateView(CreateView):
	model = Blog
	fields = ['content',]
	success_url = reverse_lazy('index')
