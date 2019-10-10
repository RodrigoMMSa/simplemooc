from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Course, Enrollment, Announcement, Lesson
from .forms import ContactCourse, CommentForm
from .decorators import enrollment_required


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
def undo_enrollment(request, slug):
    course = get_object_or_404(Course, slug=slug)
    enrollment = get_object_or_404(Enrollment, user=request.user, course=course)
    if request.method == 'POST':
        enrollment.delete()
        messages.success(request, 'Your enrollment was successfully deleted')
        return redirect('accounts:dashboard')
    template = 'courses/undo_enrollment.html'
    context = {'enrollment': enrollment, 'course': course}
    return render(request, template, context)


@login_required
@enrollment_required
def announcements(request, slug):
    course = request.course
    template = 'courses/announcements.html'
    context = {'course': course, 'announcements': course.announcements.all}
    return render(request, template, context)


@login_required
@enrollment_required
def show_announcement(request, slug, pk):
    course = request.course
    announcement = get_object_or_404(course.announcements.all(), pk=pk)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.announcement = announcement
        comment.save()
        form = CommentForm()
        messages.success(request, 'Comment successfully posted')
    template = 'courses/show_announcement.html'
    context = {
        'course': course,
        'announcement': announcement,
        'form': form
    }
    return render(request, template, context)


@login_required
@enrollment_required
def lessons(request, slug):
    course = request.course
    template = 'courses/lessons.html'
    les_sons = course.release_lessons()
    if request.user.is_staff:
        les_sons = course.lessons.all()
    context = {'course': course, 'lessons': les_sons}
    return render(request, template, context)


@login_required
@enrollment_required
def lesson(request, slug, pk):
    course = request.course
    les_son = get_object_or_404(Lesson, pk=pk, course=course)
    if not request.user.is_staff and not lesson.is_available():
        messages.error(request, 'This lesson is not available')
        return redirect('courses:lessons', slug=course.slug)
    template = 'courses/lesson.html'
    context = {'course': course, 'lesson': les_son}
    return render(request, template, context)


