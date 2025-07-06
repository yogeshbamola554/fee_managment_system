from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views import View
from .form import CustomUserCreationForm

# Create your views here.
class Login_user(View):
    def get(self,request):
        return render(request, "login.html")

def login_view(request):
    if request.mehtod == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('dashboard.html')  # change to your success URL
        else:
            messages.error(request, 'Invalid username or password!')

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST' :
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created. You can Log in Now!')
            return redirect('name')
        else:
            form = CustomUserCreationForm()
        return render(request,'new_user.html',{'form':form})