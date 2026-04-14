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

    # Resource detail pages
    path('resources/anxiety/', views.resource_anxiety_view, name='resource-anxiety'),
    path('resources/depression/', views.resource_depression_view, name='resource-depression'),
    path('resources/mindfulness/', views.resource_mindfulness_view, name='resource-mindfulness'),
    path('resources/sleep/', views.resource_sleep_view, name='resource-sleep'),
    path('resources/stress/', views.resource_stress_view, name='resource-stress'),
    path('resources/selfcare/', views.resource_selfcare_view, name='resource-selfcare'),
]
