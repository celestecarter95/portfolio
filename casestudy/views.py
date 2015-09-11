from django.shortcuts import render
from django.views import generic

from .models import CaseStudy, Item

# Create your views here.

class IndexView(generic.ListView):
	template_name = 'base.html'
	template_name = 'casestudy/index.html'
	model = CaseStudy

class DetailView(generic.DetailView):
	model = CaseStudy
	tempate_name = 'caststudy/detail.html'
