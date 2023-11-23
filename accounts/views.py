from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import View
# from .models import Franchisee, Admin
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

class LoginView(View):
    def get(self, request):
        return render(request, 'accounts/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        print(username)
  
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        print(user)

        # If the user is authenticated, log them in and redirect to the homepage
        if user is not None:
            print(user)
            login(request, user)
            if user.account_type == 'admin':
                return redirect('academy_base')
            elif user.account_type == 'franchisee':
                print(user)
                return redirect('franchise_base')
            else:
                return redirect('login')

        # If the user is not authenticated, render the login form again with an error message
        else:
                return render(request, 'accounts/login.html')


class LogoutView(View):
    def get(self, request):
        # Log out the user and redirect to the login page
        logout(request)
        return redirect('login')
    