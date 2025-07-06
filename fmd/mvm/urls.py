from django.urls import path
from . import views

urlpatterns =[
    path('', views.Login_user.as_view()),
    path('login/', views.login_view, name='login'),
    path('register',views.register,name='new_user'),
]