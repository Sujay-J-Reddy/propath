from django.shortcuts import render, redirect
from .forms import InstructorFeedbackForm

# Create your views here.
def teacher_base(request):
    return render(request, 'teacher/base.html',{'user': request.user})

def teacher_profile(request):
    return render(request, 'teacher/teacher_profile.html', {'user': request.user})

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