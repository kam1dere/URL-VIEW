from django.urls import path
from .views import SlugListView, SlugDetailView, ABSDetailView, ABSListView


app_name='myns'
urlpatterns = [
    path('slug/', SlugListView.as_view(), name='sluglist'),
    path('slug/<slug:slug>/', SlugDetailView.as_view(), name='detaillist'),
    path('abs/', ABSListView.as_view(), name='abslist'),
    path('abs/<int:pk>/<slug:slug>/', ABSDetailView.as_view(), name='absdetail'),
]