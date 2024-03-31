from django.urls import path
from . import views

app_name = 'property'

urlpatterns = [
    path('', views.property, name='properties'),
    path('new/', views.new, name='new'),
    path('fav/<int:id>/', views.favourite_add, name='favourite_add' ),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
]
