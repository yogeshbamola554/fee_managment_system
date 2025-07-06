from django.urls import path
from . import views

urlpatterns =[
    path('', views.Login_user.as_view()),
    path("classview/", views.Hello.as_view()),
]