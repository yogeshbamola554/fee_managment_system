from django.urls import path
from . import views

urlpatterns =[
    path('', views.login_view, name='login'),
    path('register/',views.register,name='new_user'),
    path('dashboard/',views.dashboard,name='dashboard'),
]