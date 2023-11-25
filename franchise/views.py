from django.shortcuts import redirect, render, get_object_or_404
from inventory.models import Item, Orders, Kit
from . models import Students
from academy.models import LevelCertificates, Competition
from . forms import StudentForm, UpdateLevelForm

# Create your views here.
def base_page(request):
    return render(request, 'franchise/base.html')

def new_order(request):
    items = Item.objects.filter(kit__isnull=True)
    kits = Kit.objects.all()
    return render(request, 'franchise/new_order.html',{'items':items, 'kits':kits})

def orders(request):
    return render(request, 'franchise/orders.html')

def competitions(request):
    comps = Competition.objects.all()
    return render(request, 'franchise/competitions.html', {'comps':comps})

def orders_completed(request):
    user_franchise = request.user
    print(user_franchise)
    orders = Orders.objects.filter(completed=True,franchise=user_franchise)

    return render(request, 'franchise/orders_completed.html',{'orders':orders})


def orders_pending(request):
    user_franchise = request.user
    print(user_franchise)
    orders = Orders.objects.filter(completed=False,franchise=user_franchise)

    return render(request, 'franchise/orders_pending.html',{'orders':orders})

def students(request):
    user_franchise = request.user
    students = Students.objects.filter(franchise=user_franchise)
    return render(request, 'franchise/students.html', {'students': students})

def register_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.instance.franchise = request.user.username
            form.save()
            return redirect('students')
    else:
        form = StudentForm()
    return render(request, 'franchise/register_student.html', {'form': form})

def edit_student(request, student_id):
    student = get_object_or_404(Students, id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('students')
    else:
        form = StudentForm(instance=student)
    return render(request, 'franchise/register_student.html', {'form': form, 'student': student})

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

def delete_student(request, student_id):
    student = get_object_or_404(Students, id=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('students')
    return render(request, 'franchise/delete_student.html', {'student': student})