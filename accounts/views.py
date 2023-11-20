from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import View
from .models import Franchisee, Admin
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

@login_required
def admin_dashboard_view(request):
    # Your admin dashboard logic here
    return redirect ('/academy/')

@login_required
def franchisee_dashboard_view(request):
    # Your franchisee dashboard logic here
    return redirect ('/franchise/')

@csrf_protect
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if Franchisee.objects.filter(username=username).exists():
                return redirect('franchisee_dashboard')
            elif Admin.objects.filter(username=username).exists():
                return redirect('admin_dashboard')
            else:
                messages.success(request, "Invalid credentials")
                return redirect('login')
    else:
        return render(request, 'accounts/login.html')


