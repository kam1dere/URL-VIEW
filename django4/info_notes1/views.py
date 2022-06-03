from django.shortcuts import render
from django.views.generic import ListView

from .models import Site, Nick, Note


class SitesListView(ListView):
    model = Site
    template_name = 'info_notes/sites_list.html'
    context_object_name = 'sites_all_list'

    # queryset = Site.objects.filter(date_added__year=2022)
    #
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return queryset.order_by('name').order_by('-date_added').reverse()[:1]

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["sites_context_all_list"] = Site.objects.all()[1:3]
    #     return context
