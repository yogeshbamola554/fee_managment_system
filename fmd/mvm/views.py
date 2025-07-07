from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from .models import NewUserRegistration
from django.contrib.auth.hashers import check_password,make_password


# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = NewUserRegistration.objects.get(username=username)

            if check_password(password, user.password):  # check hashed password
                request.session['custom_user_id'] = user.id  # create custom session
                messages.success(request, "Login successful!")
                return redirect("dashboard")  # your dashboard page
            else:
                messages.error(request, "Invalid password.")

        except NewUserRegistration.DoesNotExist:
            messages.error(request, "User does not exist.")
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        mobile_no = request.POST.get('mobile_no')
        email = request.POST.get('email_address')
        profile_photo = request.POST.get('profile_photo')
        raw_password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        address = request.POST.get('address')

        #Hashing the pasword
        password = make_password(raw_password)

        #Validating that Password and Confirm Password Match or Not
        if raw_password != confirm_password:
            messages.error(request,'Password do no Match.Please try Again!')
            return render(request,'new_user.html')
        #Checking that User doesn't already exist in database
        if User.objects.filter(username=username).exists():
            messages.error(request,'Username already Exists.Please try diffrent Username!')
            return render(request,'new_user.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request,'Email already Exists.Please try again with diffrent Email Address!')
            return render(request,'new_user.html')
        
        # Creating the User Database

        NewUserRegistration.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
            mobile_no = mobile_no,
            email = email,
            profile_photo = profile_photo,
            password = password,
            address = address,
        )
        
        messages.success(request,'Account Created Successfully.You can now Login using mentioned Credentials!')
        
        return redirect('login')
        
    return render(request,'new_user.html')

def dashboard(request):
    return render(request,'dashboard.html')

