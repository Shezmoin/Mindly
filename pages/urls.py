# URLs for pages app
from django.urls import path
from . import views

# App namespace
app_name = 'pages'

# URL patterns for pages app
urlpatterns = [
    # Homepage - root path
    path('', views.home_view, name='home'),

    # User dashboard
    path('dashboard/', views.dashboard_view, name='dashboard'),

    # About page
    path('about/', views.about_view, name='about'),
]
