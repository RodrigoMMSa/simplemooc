from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

from .models import Course, Enrollment

def enrollment_required(view_func):
    def _wrapper(request, *args, **kwargs):
        slug = kwargs['slug']
        course = get_object_or_404(Course, slug=slug)
        has_permission = request.user.is_staff
