from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    path('', views.items, name='listings'),
    path('new/', views.new, name='new'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.detail, name='delete'),
    path('<int:pk>/edit/', views.detail, name='edit'),
]