from functools import wraps
from django.shortcuts import redirect

def admin_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.account_type == 'admin':
            return view_func(request, *args, **kwargs)
        else:
            return redirect('login')  # Redirect to login page if not authenticated or not admin

    return _wrapped_view

def franchisee_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.account_type == 'franchisee':
            return view_func(request, *args, **kwargs)
        else:
            return redirect('login')  # Redirect to login page if not authenticated or not franchisee

    return _wrapped_view


def teacher_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.account_type == 'teacher':
            return view_func(request, *args, **kwargs)
        else:
            return redirect('login')  # Redirect to login page if not authenticated or not franchisee

    return _wrapped_view

def student_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.account_type == 'student':
            return view_func(request, *args, **kwargs)
        else:
            return redirect('login')  # Redirect to login page if not authenticated or not franchisee

    return _wrapped_view