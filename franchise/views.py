import json
from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from inventory.models import Item, Orders, Kit
from . models import Students
from academy.models import LevelCertificates, Competition, CompetitionRegister, Birthdays
from . forms import StudentForm, UpdateLevelForm
from accounts.decorators import franchisee_required
from django.shortcuts import render, redirect
from shared.models import Notification

# Create your views here.
@franchisee_required
def base_page(request):
    return render(request, 'franchise/base.html')

@franchisee_required
def franchise_notifications(request):
    birthdays = Birthdays.objects.filter(franchise=request.user.username)
    return render(request, 'franchise/franchise_notifications.html', {'birthdays': birthdays})

@franchisee_required
def new_order(request):
    items = Item.objects.filter(kit__isnull=True)
    kits = Kit.objects.all()
    return render(request, 'franchise/new_order.html',{'items':items, 'kits':kits})

@franchisee_required
def orders(request):
    return render(request, 'franchise/orders.html')

@franchisee_required
def competitions(request):
    comps = Competition.objects.all()
    return render(request, 'franchise/competitions.html', {'comps':comps})

@franchisee_required
def orders_completed(request):
    user_franchise = request.user
    print(user_franchise)
    orders = Orders.objects.filter(completed=True,franchise=user_franchise)

    for order in orders:
        order.items = json.loads(order.items)

    for order in orders:
        order.kits = json.loads(order.kits)

    return render(request, 'franchise/orders_completed.html',{'orders':orders})

@franchisee_required
def orders_pending(request):
    user_franchise = request.user
    print(user_franchise)
    orders = Orders.objects.filter(completed=False,franchise=user_franchise)

    for order in orders:
        print(order.kits)

    for order in orders:
        order.items = json.loads(order.items)

    for order in orders:
        order.kits = json.loads(order.kits)

    return render(request, 'franchise/orders_pending.html',{'orders':orders})

@franchisee_required
def students(request):
    user_franchise = request.user
    students = Students.objects.filter(franchise=user_franchise)
    return render(request, 'franchise/students.html', {'students': students})

@franchisee_required
def register_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.franchise = request.user.username
            form.save()
            return redirect('students')
    else:
        form = StudentForm()
    return render(request, 'franchise/register_student.html', {'form': form})

@franchisee_required
def edit_student(request, student_id):
    student = get_object_or_404(Students, id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('students')
    else:
        form = StudentForm(instance=student)
    return render(request, 'franchise/register_student.html', {'form': form, 'student': student})

@franchisee_required
def update_level(request, student_id):
    student = get_object_or_404(Students, id=student_id)
    if request.method == 'POST':
        form = UpdateLevelForm(request.POST, instance=student)
        if form.is_valid():
            LevelCertificates.objects.create(
                student=student.name,
                franchise=student.franchise,
                course= student.course,
                programme=student.programme,
                level=student.level - 1,
            )
            form.save()

            return redirect('students')
    else:
        form = UpdateLevelForm(instance=student)
    return render(request, 'franchise/register_student.html', {'form': form, 'student': student})

@franchisee_required
def delete_student(request, student_id):
    student = get_object_or_404(Students, id=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('students')
    return render(request, 'franchise/delete_student.html', {'student': student})

@franchisee_required
def competition_register(request, comp_id):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        user = request.user.username
        franchise = data.get('franchise')
        table_data_json = data.get('tableData')
        students = []
        for row in table_data_json:
            student_id = row.get('item')
            student = Students.objects.get(id=student_id)
            students.append({"student_id": student.id, "student_name": student.name})
        
        entry = CompetitionRegister(circular_no=comp_id, franchise=franchise, students=json.dumps(students))
        entry.save()
        return JsonResponse({'success': 'Data saved successfully'})
    
    else:
        user = request.user.username
        students = Students.objects.filter(franchise=user)
        return render(request, 'franchise/competition_register.html', {'students': students, 'comp_id':comp_id})
    
@franchisee_required
def new_order(request):
    items = Item.objects.filter(kit__isnull=True)
    kits = Kit.objects.all()

    if request.method == 'GET' and 'order_submitted' in request.GET:
        # Save the notification to the shared database
        Notification.objects.create(message='Order submitted successfully!')

        return redirect('franchise:new_order')

    return render(request, 'franchise/new_order.html', {'items': items, 'kits': kits})
