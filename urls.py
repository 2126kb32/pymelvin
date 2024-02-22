# myapp/urls.py
from django.urls import path
from .views import login_view, home_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('', home_view, name='home'),
    # Add more URL patterns as needed
]
