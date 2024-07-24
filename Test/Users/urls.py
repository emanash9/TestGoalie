from django.urls import path
from . import views

app_name = 'Users'

urlpatterns = [
    path('', views.index, name='index'),  # Add this line to handle the root URL for Users
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),

    path('contact/', views.contact, name='contact'),
]
