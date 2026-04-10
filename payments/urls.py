# URLs for payments app
from django.urls import path
from . import views

# App namespace
app_name = 'payments'

# URL patterns for payments app
urlpatterns = [
    path('', views.index_view, name='index'),
    path('pricing/', views.pricing_view, name='pricing'),
    path('donate/', views.donate_view, name='donate'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('subscribe/', views.subscribe_view, name='subscribe'),
    path('success/', views.success_view, name='success'),
    path('cancel/', views.cancel_view, name='cancel'),
    path('webhook/', views.webhook_handler, name='webhook'),
]
