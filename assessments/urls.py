# URLs for assessments app
from django.urls import path
from . import views

# App namespace
app_name = 'assessments'

# URL patterns for assessments app
urlpatterns = [
    path('', views.index_view, name='index'),
    path('<str:tool>/', views.assessment_view, name='detail'),
]
