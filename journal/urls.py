# URLs for journal app
from django.urls import path
from . import views

# App namespace
app_name = 'journal'

# URL patterns for journal app
urlpatterns = [
    path('', views.index_view, name='index'),
    path('mood/new/', views.mood_create_view, name='mood-create'),
    path('mood/', views.mood_list_view, name='mood-list'),
    path('entries/new/', views.journal_create_view, name='journal-create'),
    path('entries/', views.journal_list_view, name='journal-list'),
]
