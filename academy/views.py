from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import FranchiseeForm, AdminForm

# Create your views here.
def academy_base(request):
    return render(request, 'academy/base.html')

def register_user(request):
    return render(request, 'academy/register_user.html')

def register_franchisee(request):
    if request.method == 'POST':
        form = FranchiseeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('academy_base')
    else:
        form = FranchiseeForm()
    return render(request, 'academy/register_franchisee.html', {'form': form})

def register_admin(request):
    if request.method == 'POST':
        form = AdminForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('academy_base')
    else:
        form = AdminForm()
    return render(request, 'academy/register_admin.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('/accounts/login')

