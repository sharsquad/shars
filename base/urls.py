from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.base, name='main'),
    path('about/', views.about, name='about'),
    path('links/', views.links, name='links'),
    path('database/', views.database, name='database'),
    path('bot', views.bot, name='bot'),
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('logout_view/', views.logout_view, name='logout_view'),
]
