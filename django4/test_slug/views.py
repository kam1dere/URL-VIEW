from django.shortcuts import render

from .models import Statya

from django.views.generic import ListView, DetailView

class StatyaListView(ListView):
    model = Statya
    template_name = 'list.html'

class StatyaDetailView(DetailView):
    model = Statya
    template_name = 'detail.html'

# Create your views here.
