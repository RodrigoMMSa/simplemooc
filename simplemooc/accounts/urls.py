from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from . import views


app_name = 'accounts'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('password-reset/', views.password_reset, name='password_reset'),
    path('edit/', views.edit, name='edit'),
    path('edit-password/', views.edit_password, name='edit_password'),
    path('logout/', LogoutView.as_view(next_page='core:home'), name='logout'),
]

