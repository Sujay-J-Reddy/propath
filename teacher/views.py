from django.shortcuts import render, redirect
from .forms import InstructorFeedbackForm
from accounts.models import TeacherLevel
from accounts.decorators import teacher_required

# Create your views here.
@teacher_required
def teacher_base(request):
    duedate = TeacherLevel.objects.filter(user=request.user)
    return render(request, 'teacher/base.html',{'user': request.user, 'duedate': duedate})

@teacher_required
def teacher_profile(request):
    return render(request, 'teacher/teacher_profile.html', {'user': request.user})

@teacher_required
def feedback_view(request):
    if request.method == 'POST':
        form = InstructorFeedbackForm(request.POST)
        if form.is_valid():
            # Process the form data if valid
            form.instance.user = request.user
            form.save()
        return redirect('teacher_base')
    else:
        form = InstructorFeedbackForm()

    return render(request, 'teacher/feedback.html', {'form': form})