# URLs for pages app
from django.urls import path
from . import views

# App namespace
app_name = 'pages'

# URL patterns for pages app
urlpatterns = [
    # Homepage - root path
    path('', views.home_view, name='home'),

    # Resources page
    path('resources/', views.resources_view, name='resources'),

    # Premium-only resources
    path('resources/premium/', views.premium_resources_view, name='premium-resources'),

    # User dashboard
    path('dashboard/', views.dashboard_view, name='dashboard'),

    # About page
    path('about/', views.about_view, name='about'),
]
