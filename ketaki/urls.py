from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('welcome/', views.welcome, name='welcome'),
    path('love/<str:letter>/', views.love_letter, name='love_letter'),
    path('logout/', views.logout_view, name='logout'),
]
