from django.urls import path
from django import urls
from .views import PageListView, PageDetailView, \
    PageListNamespace, PageDetailNamespace, PageDetailGetAbs, \
    PageListGetAbs

app_name = 'yesNS'
urlpatterns = [
    path('slug/', PageListView.as_view(), name='list_slug'),
    path('<slug:slug>/', PageDetailView.as_view(), name='detail_slug'),
    path('slug/slug/', PageListNamespace.as_view(), name='list_ns'),
    path('slug/<int:pk>/detail/', PageDetailNamespace.as_view(),
         name='detail_ns'),
    path('absolute/list/', PageListGetAbs.as_view(), name='list_get'),
    path('absoluteSOSI/<int:pk>/<slug:slug>/', PageDetailGetAbs.as_view(), name='detail_get')

]