from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views import View
from .form import CustomUserCreationForm
from django.contrib.auth.models import User

# Create your views here.
class Login_user(View):
    def get(self,request):
        return render(request, "login.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('dashboard.html')  # change to your success URL
        else:
            messages.error(request, 'Invalid username or password!')

    return render(request, 'login.html')


# def register(request):
#     if request == 'POST':
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         username = request.POST.get('username')
#         mobile_no = request.POST.get('mobile_no')
#         email = request.POST.get('email_address')
#         profile_photo = request.POST.get('profile_photo')
#         password = request.POST.get('password')
#         confirm_password = request.POST.get('confirm_password')
#         address = request.POST.get('address')
#         #Validating that Password and Confirm Password Match or Not
#         if password != confirm_password:
#             messages.error(request,'Password do no Match.Please try Again!')
#             return render(request,'new_user.html')
#         #Checking that User doesn't already exist in database
#         if User.objects.filter(username=username).exists():
#             messages.error(request,'Username already Exists.Please try diffrent Username!')
#             return render(request,'new_user.html')
        
#         if User.objects.filter(email=email).exists():
#             messages.error(request,'Email already Exists.Please try diffrent Email Address!')
#             return render(request,'new_user.html')
        
#         # Creating the User Database

#         user = User.objects.create_user(
#             first_name = first_name,
#             last_name = last_name,
#             username = username,
#             mobile_no = mobile_no,
#             email = email,
#             profile_photo = profile_photo,
#             password = password,
#             address = address,
#         )
        
#         messages.success(request,'Account Created Successfully.You can now Login using mentioned Credentials!')
#         return redirect('login')
        
#     return render(request,'new_user.html')

