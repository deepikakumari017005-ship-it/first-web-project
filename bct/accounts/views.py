from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Task

def register_page(request):
    if request.method == "POST":
        username = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        image = request.FILES.get('image')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')
        
        # Changed variable to 'new_user' to avoid conflict with 'User' model
        new_user = User.objects.create_user(username=username, email=email, password=password)

        if image:
            Task.objects.create(user=new_user, image=image, title="Profile Registration Image")
        
        messages.success(request, "Registration Successful ✅")
        return redirect('login')

    return render(request, 'register.html')

def login_page(request):
    if request.method == "POST":
        # Note: 'username' is used by authenticate, even if you collect email
        u_name = request.POST.get('username') 
        p_word = request.POST.get('password')
        
        user = authenticate(request, username=u_name, password=p_word)
        
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credentials ❌")

    return render(request, 'login.html')

@login_required
def dashboard(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'tasks': tasks})