from django.urls import path

from .views import SitesListView


urlpatterns = [
    path('sites/', SitesListView.as_view(), name='sites_list')
]
