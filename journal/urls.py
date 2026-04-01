# URLs for journal app
from django.urls import path
from . import views

# App namespace
app_name = 'journal'

# URL patterns for journal app
urlpatterns = [
    path('', views.index_view, name='index'),
]
