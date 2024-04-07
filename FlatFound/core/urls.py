from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import LoginForm

app_name = 'core'

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='core/login.html',
         authentication_form=LoginForm),  name='login'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('index/', views.index, name='index'),
    path('logout/', auth_views.LogoutView.as_view(template_name='core/logout.html',
         next_page=None), name='logout')
]

# Attempting to make the login screen the default
