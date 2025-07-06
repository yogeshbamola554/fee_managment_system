from django.urls import path
from . import views

urlpatterns =[
    path("hello/", views.home),
    path("classview/", views.Hello.as_view()),
]