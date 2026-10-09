
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('dashboard/', views.index, name='dashboard'),
    path('events/', views.events_page, name='events'),
    path('participants/', views.participants_page, name='participants'),
    path('settings/', views.settings_page, name='settings'),
]
