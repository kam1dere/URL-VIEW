from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Nitik

#SLUG
class SlugListView(ListView):
    model = Nitik
    template_name = 'slug/sluglist.html'

class SlugDetailView(DetailView):
    model = Nitik
    template_name = 'slug/detaillist.html'

#ABS
class ABSListView(ListView):
    model = Nitik
    template_name = 'abs/abslist.html'

class ABSDetailView(DetailView):
    model = Nitik
    template_name = 'abs/absdetail.html'

# Create your views here.
