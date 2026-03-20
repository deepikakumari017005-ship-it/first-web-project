from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

def register_page(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        User.objects.create_user(username=email, email=email, password=password)

        messages.success(request, "Registration Successful ✅")
        return redirect('login')

    return render(request, 'register.html')


def login_page(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(username=email, password=password)

        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credentials ❌")

    return render(request, 'login.html')


def dashboard(request):
    return render(request, 'dashboard.html')