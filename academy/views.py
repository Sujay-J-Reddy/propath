from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import logout
from franchise.models import Students
from .forms import UserForm, FranchiseDetailsForm, EditUserForm
from accounts.models import CustomUser, FranchiseDetails
from django.contrib.auth.hashers import make_password

from accounts.models import Franchisee
# from .tasks import check_and_add_birthdays

# def schedule_birthday_check(request):
#     check_and_add_birthdays(repeat=60*60*24)  # Schedule the task to repeat every 6 hours
#     return HttpResponse("Birthday check scheduled.")

def academy_base(request):
    return render(request, 'academy/base.html')

def register_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # Don't save the user yet, just set the password
            user.set_password(form.cleaned_data['password'])
            user.save()
            if form.cleaned_data['account_type'] == 'franchisee':
                return redirect('franchise_details',user_id=user.id)
            return redirect('academy_base')
    else:
        form = UserForm()
    return render(request, 'academy/register_user.html',{'form':form})

def franchise_page(request):
    franchises =  FranchiseDetails.objects.all()
    return render(request, 'academy/franchise_page.html',{'franchises':franchises})

def franchise_details(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    franchise_details_instance = FranchiseDetails.objects.filter(user=user).first()

    if request.method == 'POST':
        form = FranchiseDetailsForm(request.POST, instance=franchise_details_instance)
        if form.is_valid():
            print("valid")
            franchise_details_instance = form.save(commit=False)
            franchise_details_instance.user = user
            franchise_details_instance.save()
            print("saved")
            return redirect('academy_base')  # Redirect to some other view after saving
    else:
        form = FranchiseDetailsForm(instance=franchise_details_instance)
    return render(request, 'academy/franchise_details.html', {'form': form, 'user': user})

def delete_franchisee(request, user_id):
    franchisee = get_object_or_404(CustomUser, id=user_id)
    if request.method == 'POST':
        franchisee.delete()
        return redirect('franchise_page')
    return render(request, 'academy/delete_franchisee.html', {'franchisee': franchisee})


def edit_login(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)

    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            # Check if the password field is updated
            if 'password' in form.changed_data:
                # Update the password using make_password
                form.instance.password = make_password(form.cleaned_data['password'])
            form.save()
            return redirect('franchise_page')
    else:
        form = EditUserForm(instance=user)


    return render(request, 'academy/edit_login.html', {'form': form, 'user': user})

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

