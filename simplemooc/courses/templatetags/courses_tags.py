from django import template
from simplemooc.courses.models import Enrollment


register = template.Library()


@register.inclusion_tag('courses/templatetags/my_courses.html')
def my_courses(user):
    enrollments = Enrollment.objects.filter(user=user)
    context = {'enrollments': enrollments}
    return context
