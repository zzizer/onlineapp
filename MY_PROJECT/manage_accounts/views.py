from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from products_manager.models import Product


def home(request):
    return render(request, 'welcome_page.html')

def signin(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user is  not None:
            products = Product.objects.all()
            
            login(request, user)
            first_name = user.first_name
            
            messages.success(request, 'Logged In Successfully')
            return render(request, 'shopping.html', {'first_name':first_name, 'products':products})
        
        else:
            messages.error(request, 'Wrong Credentials, Please Try again Later...!')
            return redirect('/')
            
    return render(request, 'in.html')

def signup(request):
    if request.method =='POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        pass2 = request.POST['pass2']
        
        if User.objects.filter(email=email).exists():
            messages.info(request, 'Email already Used...!')
            return redirect('signup')
        elif User.objects.filter(username=username).exists():
            messages.info(request, 'Username already Used...!')
            return redirect('signup')
        else:
            my_User = User.objects.create_user(username, email, password)
            my_User.first_name = fname
            my_User.last_name = lname

            my_User.save()

            messages.success(request, 'Account Created..!')
            return redirect('signin')
        
    return render(request, 'up.html')

def signout(request):
    logout(request)
    messages.info(request, 'Successfully Logged Out')
    return redirect('/')
