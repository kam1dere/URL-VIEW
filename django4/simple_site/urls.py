from django.urls import path
from simple_site.views import ArticleListView, ArticleDetailView

urlpatterns = [
    path('', ArticleListView.as_view(), name = 'list '),
    path('<int:slug>/', ArticleDetailView.as_view(), name = 'article-detail'),
    ]