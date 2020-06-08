from django.urls import path
from .views import home, new_search

urlpatterns = [
    path('', home, name='home_page'),
    path('new_search', new_search, name='search_page')
]