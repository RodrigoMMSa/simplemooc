from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Course, Enrollment
from .forms import ContactCourse


def index(request):
    courses = Course.objects.all()
    template_name = 'courses/index.html'
    context = {'courses': courses}
    return render(request, template_name, context)


def details(request, slug):
    course = get_object_or_404(Course, slug=slug)
    context = {}
    if request.method == 'POST':
        form = ContactCourse(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form.send_mail(course)
            form = ContactCourse()
    else:
        form = ContactCourse()
    context['course'] = course
    context['form'] = form
    template_name = 'courses/details.html'
    return render(request, template_name, context)


@login_required
def enrollments(request, slug):
    course = get_object_or_404(Course, slug=slug)
    enrollment, created = Enrollment.objects.get_or_create(user=request.user, course=course)
    if created:
        # enrollment.active()
        messages.success(request, "You are successfully enrolled in this course")
    else:
        messages.info(request, "You are already enrolled in this course")
    return redirect('accounts:dashboard')


@login_required
def undo_enrollments(request, slug):
    course = get_object_or_404(Course, slug=slug)
    enrollment = get_object_or_404(Enrollment, user=request.user, course=course)
    template = 'courses/undo_enrollment.html'
    return render(request, template)


@login_required
def announcements(request, slug):
    course = get_object_or_404(Course, slug=slug)
    if not request.user.is_staff:
        enrollment = get_object_or_404(Enrollment, user=request.user, course=course)
        if not enrollment.is_approved():
            messages.error(request, 'Your enrollment is pendent')
            return redirect('accounts:dashboard')
    template = 'courses/announcements.html'
    context = {'course': course}
    return render(request, template, context)
