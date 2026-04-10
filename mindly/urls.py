"""
URL configuration for mindly project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from payments.views import checkout_view

# Main URL patterns for Mindly project
urlpatterns = [
    # Django admin interface
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('checkout/', checkout_view, name='checkout'),

    # App URLs
    path('', include('pages.urls')),  # Homepage and static pages
    path('users/', include('users.urls')),  # User authentication
    path('assessments/', include('assessments.urls')),  # Mental health assessments
    path('journal/', include('journal.urls')),  # Personal journaling
    path('payments/', include('payments.urls')),  # Donations and subscriptions
]
