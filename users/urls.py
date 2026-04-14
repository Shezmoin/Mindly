# URLs for users app
from django.urls import path
from . import views

# App namespace
app_name = 'users'

# URL patterns for users app
urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.profile_edit_view, name='profile-edit'),
    path('logout/', views.logout_view, name='logout'),
]
