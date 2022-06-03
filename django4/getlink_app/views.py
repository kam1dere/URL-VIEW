from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .models import Page

#Get_abs
class PageListGetAbs(ListView):
    model = Page
    template_name = 'get_abs/list_get.html'

class PageDetailGetAbs(DetailView):
    model = Page
    template_name = 'get_abs/detail_get.html'

#NS
class PageListNamespace(ListView):
    model = Page
    template_name = 'ns/list_ns.html'

class PageDetailNamespace(DetailView):
    model = Page
    template_name = 'ns/detail_ns.html'

#SLUG
class PageListView(ListView):
    model = Page
    template_name = 'slug_url/list_slug.html'

class PageDetailView(DetailView):
    model = Page
    template_name = 'slug_url/detail_slug.html'


