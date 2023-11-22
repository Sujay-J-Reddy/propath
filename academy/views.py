from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import logout
from .forms import FranchiseeForm, AdminForm
from franchise.models import Students
from accounts.models import Franchisee
# from .tasks import check_and_add_birthdays

# def schedule_birthday_check(request):
#     check_and_add_birthdays(repeat=60*60*24)  # Schedule the task to repeat every 6 hours
#     return HttpResponse("Birthday check scheduled.")

def academy_base(request):
    return render(request, 'academy/base.html')

def register_user(request):
    return render(request, 'academy/register_user.html')

def register_franchisee(request):
    if request.method == 'POST':
        form = FranchiseeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('franchise_page')
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

def students_page(request):
    students = Students.objects.all()
    unique_franchises = Students.objects.values_list('franchise', flat=True).distinct()

    # Group students by franchise
    students_by_franchise = {}
    for franchise in unique_franchises:
        students_in_franchise = students.filter(franchise=franchise)
        students_by_franchise[franchise] = students_in_franchise

    return render(request, 'academy/students_page.html', {'students_by_franchise': students_by_franchise, 'franchises': unique_franchises})

def franchise_page(request):
    franchises = Franchisee.objects.all()
    return render(request, 'academy/franchise_page.html',{'franchises':franchises})

def edit_franchisee(request, franchisee_id):
    franchisee = get_object_or_404(Franchisee, id=franchisee_id)
    if request.method == 'POST':
        form = FranchiseeForm(request.POST, instance=franchisee)
        if form.is_valid():
            form.save()
            return redirect('franchise_page')
    else:
        form = FranchiseeForm(instance=franchisee)
    return render(request, 'academy/edit_franchisee.html', {'form': form, 'franchisee': franchisee})

def delete_franchisee(request, franchisee_id):
    franchisee = get_object_or_404(Franchisee, id=franchisee_id)
    if request.method == 'POST':
        franchisee.delete()
        return redirect('franchise_page')
    return render(request, 'academy/delete_franchisee.html', {'franchisee': franchisee})