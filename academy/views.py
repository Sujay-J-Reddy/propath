from datetime import datetime
from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import logout
from franchise.models import Students
from .forms import UserForm, FranchiseDetailsForm, EditUserForm, TeacherDetailsForm, TeacherLevelForm, CompetitionForm
from accounts.models import CustomUser, FranchiseDetails, TeacherDetails, TeacherLevel
from .models import LevelCertificates, CompetitionRegister, Birthdays, TrainingDate
from teacher.models import InstructorFeedback
from django.contrib.auth.hashers import make_password
from accounts.decorators import admin_required

@admin_required
def academy_base(request):
    return render(request, 'academy/base.html')

@admin_required
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
            elif form.cleaned_data['account_type'] == 'teacher':
                return redirect('teacher_details',user_id = user.id)
            return redirect('academy_base')
    else:
        form = UserForm()
    return render(request, 'academy/register_user.html',{'form':form})

@admin_required
def franchise_page(request):
    franchises =  FranchiseDetails.objects.all()
    return render(request, 'academy/franchise_page.html',{'franchises':franchises})

@admin_required
def certificate_requests(request):
    students =  LevelCertificates.objects.all()
    return render(request, 'academy/certificate_requests.html',{'students':students})

@admin_required
def teachers_page(request):
    teachers = TeacherDetails.objects.all()

    teacher_data = []
    for teacher in teachers:
        try:
            teacher_level = TeacherLevel.objects.get(user=teacher.user)
            previous_level_trained = teacher_level.prev_level
            training_date = teacher_level.prev_level_date
            training_due_date = teacher_level.due_date
        except TeacherLevel.DoesNotExist:
            previous_level_trained = "N/A"
            training_date = "N/A"
            training_due_date = "N/A"

        teacher_data.append({
            'teacher': teacher,
            'previous_level_trained': previous_level_trained,
            'training_date': training_date,
            'training_due_date': training_due_date,
        })

    return render(request, 'academy/teachers_page.html', {'teacher_data': teacher_data})

@admin_required
def franchise_details(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    franchise_details_instance = FranchiseDetails.objects.filter(user=user).first()

    if request.method == 'POST':
        form = FranchiseDetailsForm(request.POST, request.FILES, instance=franchise_details_instance)
        if form.is_valid():
            franchise_details_instance = form.save(commit=False)
            franchise_details_instance.user = user
            form.cleaned_data['program_name'] = ','.join(form.cleaned_data['program_name'])
            franchise_details_instance.save()
            return redirect('academy_base')  # Redirect to some other view after saving
    else:
        form = FranchiseDetailsForm(instance=franchise_details_instance)

    return render(request, 'academy/franchise_details.html', {'form': form, 'user': user})

@admin_required
def delete_franchisee(request, user_id):
    franchisee = get_object_or_404(CustomUser, id=user_id)
    if request.method == 'POST':
        franchisee.delete()
        return redirect('franchise_page')
    return render(request, 'academy/delete_franchisee.html', {'franchisee': franchisee})

@admin_required
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

@admin_required
def teacher_details(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    teacher_details_instance = TeacherDetails.objects.filter(user=user).first()

    if request.method == 'POST':
        form = TeacherDetailsForm(request.POST, request.FILES, instance=teacher_details_instance)
        if form.is_valid():
            print("valid")
            teacher_details_instance = form.save(commit=False)
            teacher_details_instance.user = user
            teacher_details_instance.save()
            print("saved")
            return redirect('academy_base')  # Redirect to some other view after saving
    else:
        form = TeacherDetailsForm(instance=teacher_details_instance)
    return render(request, 'academy/teacher_details.html', {'form': form, 'user': user})

@admin_required
def delete_teacher(request, user_id):
    teacher = get_object_or_404(CustomUser, id=user_id)
    if request.method == 'POST':
        teacher.delete()
        return redirect('teachers_page')
    return render(request, 'academy/delete_teacher.html', {'teacher': teacher})

@admin_required
def teacher_level_form(request, user_id):
    teacher = get_object_or_404(TeacherDetails, user__id=user_id)
    
    try:
        teacher_level = TeacherLevel.objects.get(user=teacher.user)
    except TeacherLevel.DoesNotExist:
        teacher_level = None

    if request.method == 'POST':
        # Handle form submission
        form = TeacherLevelForm(request.POST, instance=teacher_level)
        if form.is_valid():
            form.instance.user = teacher.user
            form.save()
            return redirect('teachers_page')
    else:
        # Display the form
        form = TeacherLevelForm(instance=teacher_level)

    return render(request, 'academy/teacher_level_form.html', {'form': form, 'teacher': teacher})

@admin_required
def teacher_feedbacks(request):
    teachers = InstructorFeedback.objects.all()
    return render(request, 'academy/teacher_feedbacks.html', {'teacher_data':teachers})

def logout_user(request):
    logout(request)
    return redirect('/login')

@admin_required
def students_page(request):
    students = Students.objects.all()
    unique_franchises = Students.objects.values_list('franchise', flat=True).distinct()

    # Group students by franchise
    students_by_franchise = {}
    for franchise in unique_franchises:
        students_in_franchise = students.filter(franchise=franchise)
        students_by_franchise[franchise] = students_in_franchise

    return render(request, 'academy/students_page.html', {'students_by_franchise': students_by_franchise, 'franchises': unique_franchises})

@admin_required
def competitions_page(request):
    if request.method == 'POST':
        form = CompetitionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('academy_base')  # Redirect to a success page or any other desired view
    else:
        form = CompetitionForm()

    return render(request, 'academy/competitions_page.html', {'form': form})

@admin_required
def competition_entries(request):
    entries = CompetitionRegister.objects.all()
    return render(request, 'academy/competition_registrations.html', {'entries':entries})

@admin_required
def competition_winners(request):
    return render(request, 'academy/competition_winners')


def check_birthdays(request):
    today = datetime.now().date()

    # Clear existing records in Birthdays model
    Birthdays.objects.all().delete()

    # Check Students
    students_birthdays = Students.objects.filter(dob__month=today.month, dob__day=today.day)
    for student in students_birthdays:
        Birthdays.objects.create(name=student.name, franchise=student.franchise, birthday=student.dob)

    # Check FranchiseDetails
    franchises_birthdays = FranchiseDetails.objects.filter(dob__month=today.month, dob__day=today.day)
    for franchise in franchises_birthdays:
        Birthdays.objects.create(name=f"{franchise.first_name} {franchise.last_name}", franchise=franchise.user.username, birthday=franchise.dob)

    # Check TeacherDetails
    teachers_birthdays = TeacherDetails.objects.filter(dob__month=today.month, dob__day=today.day)
    for teacher in teachers_birthdays:
        Birthdays.objects.create(name=teacher.name, franchise=teacher.franchise.franchise_details.user.username, birthday=teacher.dob)

    teacher_training_due = TeacherLevel.objects.filter(due_date = datetime.today())
    for teacher in teacher_training_due:
        TrainingDate.objects.create(name=teacher.user.teacher_details.name, training_level=teacher.prev_level+1, franchise=teacher.user.teacher_details.franchise.franchise_details.user.username)

    return HttpResponse("Birthdays checked and updated successfully")
