from django.urls import path
from .views import StatyaListView, StatyaDetailView

urlpatterns = [
    path('slug/', StatyaListView.as_view(), name='list'),
    path('<int:slug>/', StatyaDetailView.as_view(), name='detail'),
]