from functools import wraps
from django.shortcuts import redirect

def role_required(role, login_url=None):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *arg, **kwargs):
            if not request.user.is_authenticated:
                return redirect(login_url or "log-in")
            if request.user.role not in role:
                return redirect("dashboard")##!главная страница
            return view_func(request, *arg, *kwargs)
        return _wrapped_view
    return decorator