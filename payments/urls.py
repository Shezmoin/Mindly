# URLs for payments app
from django.urls import path
from . import views

# App namespace
app_name = 'payments'

# URL patterns for payments app
urlpatterns = [
    path('', views.index_view, name='index'),
]
