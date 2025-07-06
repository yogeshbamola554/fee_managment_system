from django.shortcuts import render, HttpResponse
from django.views import View

# Create your views here.
class Login_user(View):
    def post(self,request):
        return render(request, "login.html")

class Hello(View):
    def post(self,request):
        return HttpResponse("Hello Class Based View")

