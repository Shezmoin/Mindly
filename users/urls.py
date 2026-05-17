# URLs for users app
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

# App namespace
app_name = 'users'

# URL patterns for users app
urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('register/success/', views.register_success_view, name='register-success'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # Password reset URLs (custom view with username capture)
    path('password-reset/', views.PasswordResetView.as_view(template_name='users/password_reset.html', success_url='/users/password-reset/done/'), name='password-reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password-reset-done'),
    path('password-reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password-reset-confirm'),
    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password-reset-complete'),
    # Profile URLs
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.profile_edit_view, name='profile-edit'),
    path('profile/cancel-premium/', views.cancel_premium_view, name='cancel-premium'),
]
