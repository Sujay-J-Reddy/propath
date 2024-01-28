from datetime import datetime
from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import logout
from franchise.models import Students
from .forms import *
from accounts.models import CustomUser, FranchiseDetails, TeacherDetails, TeacherLevel
from .models import *
from inventory.models import Kit, Item, Orders
from teacher.models import InstructorFeedback
from django.contrib.auth.hashers import make_password
from accounts.decorators import admin_required
from django.shortcuts import render
from django.http import JsonResponse
import json
from inventory.models import *
from franchise.models import *
from typing import List
from django.shortcuts import render

@admin_required
def academy_base(request):
    # Assuming Orders is a queryset of Orders objects
    orders = Orders.objects.all()

    for order in orders:
        # Extracting only the 'franchise' attribute
        order.franchise_only = order.franchise

        try:
            # Attempt to load JSON data only if order.items is a string
            if isinstance(order.items, str):
                order.items = json.loads(order.items)
            else:
                # If order.items is not a string, handle it accordingly
                order.items = {}  # Set a default value or handle it based on your requirements
        except json.JSONDecodeError as e:
            # Handle the JSON decoding error, e.g., log it or set a default value
            order.items = {}  # Set a default value or handle it based on your requirements

        # Save the modified order back to the database
        order.save()

    # Assuming Students is a queryset of Students objects
    students = Students.objects.all()

    for student in students:
        # Extracting only the 'franchise' attribute for Students
        student.franchise_only = student.franchise

        # Handle other logic for the Students model here
        # If there is no 'items' field in the Students model, you can skip the related logic

        # Save the modified student back to the database
        student.save()

    enquiries = list(Enquiry.objects.all())


    return render(request, 'academy/base.html', {'orders': orders, 'students': students})



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
def schools_page(request):
    schools = Schools.objects.all()
    return render(request, 'academy/schools.html', {'schools':schools}) 

def register_school(request):
    if request.method == 'POST':
        form = SchoolRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('schools_page')  # Redirect to a success page or any other desired page after successful registration
    else:
        form = SchoolRegistrationForm()

    return render(request, 'academy/register_school.html', {'form': form})


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
            return redirect('competitions_base')  # Redirect to a success page or any other desired view
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
    TrainingDate.objects.all().delete()

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

def enquiry(request):
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('landing_page')
    else:
        form = EnquiryForm()

    return render(request, 'academy/enquiry.html', {'form': form})

@admin_required
def school_order(request):
    items = Item.objects.filter(kit__isnull=True)
    kits = Kit.objects.all()
    schools = Schools.objects.all()
    return render(request, 'academy/school_order.html',{'kits':kits, 'items':items, 'schools':schools})

@admin_required
def school_students(request, school_id):
    school = get_object_or_404(Schools, id=school_id)
    students = SchoolStudents.objects.filter(school=school)
    
    context = {
        'school': school,
        'students': students,
    }
    
    return render(request, 'academy/school_students.html', context)

@admin_required
def register_student(request, school_id):
    school = get_object_or_404(Schools, id=school_id)

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student_data = form.cleaned_data
            SchoolStudents.objects.create(
                name=student_data['name'],
                level=student_data['level'],
                dob=student_data['dob'],
                contact=student_data['contact'],
                school=school
            )
            return redirect('school_students', school_id=school_id)
    else:
        form = StudentForm()

    context = {
        'school': school,
        'form': form,
    }

    return render(request, 'academy/register_school_student.html', context)

@admin_required
def all_students(request):
    students = SchoolStudents.objects.all()
    return render (request, 'academy/all_students.html', {'students':students})

@admin_required
def enquiry_page(request):
    enquiries = Enquiry.objects.all()
    return render(request, 'academy/enquiry_page.html', {'enquiries':enquiries})

@admin_required
def events_page(request):
    events = Events.objects.all()
    return render(request, 'academy/events_page.html',{'events':events})

@admin_required
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('events_page')
    else:
        form = EventForm()
    return render(request, 'academy/add_event.html', {'form': form})

@admin_required
def edit_event(request, event_id):
    event = get_object_or_404(Events, id=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('events_page')
    else:
        form = EventForm(instance=event)
    return render(request, 'academy/edit_event.html', {'form': form, 'event': event})

@admin_required
def edit_school_student(request, student_id):
    student = get_object_or_404(SchoolStudents, id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('school_students')
    else:
        form = StudentForm(instance=student)
    return render(request, 'academy/edit_school_student.html', {'form': form, 'student': student})

@admin_required
def edit_school(request, school_id):
    school = get_object_or_404(Schools, id=school_id)
    if request.method == 'POST':
        form = SchoolRegistrationForm(request.POST, instance=school)
        if form.is_valid():
            form.save()
            return redirect('schools')
    else:
        form = SchoolRegistrationForm(instance=school)
    return render(request, 'academy/edit_school_student.html', {'form': form, 'school': school})

@admin_required
def competitions_base(request):
    comps = Competition.objects.all()
    return render(request,'academy/competitions.html',{'comps':comps})

@admin_required
def edit_comp(request, comp_id):
    comp = get_object_or_404(Competition, circular_no=comp_id)
    if request.method == 'POST':
        form = CompetitionForm(request.POST, instance=comp)
        if form.is_valid():
            form.save()
            return redirect('competitions_base')
    else:
        form = CompetitionForm(instance=comp)
    return render(request, 'academy/edit_comp.html', {'form': form, 'comp': comp})