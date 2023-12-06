from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import View
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

def landing_page(request):
    return render(request, 'accounts/landing_page.html')
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
            if user.account_type == 'admin': # type: ignore
                return redirect('academy_base')
            elif user.account_type == 'franchisee': # type: ignore
                print(user)
                return redirect('franchise_base')
            elif user.account_type == 'teacher': # type: ignore
                return redirect('teacher_base')
            else:
                return redirect('login')

        # If the user is not authenticated, render the login form again with an error message
        else:
                return render(request, 'accounts/login.html')
