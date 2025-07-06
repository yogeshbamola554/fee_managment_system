from django.shortcuts import render, HttpResponse
from django.views import View

# Create your views here.
def home(request):
    return HttpResponse("Hello World!")

class Hello(View):
    def hello(self,request):
        return HttpResponse("Hello Class Based View")

