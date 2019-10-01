from django.db import models
from django.urls import reverse
from django.conf import settings


class CourseManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(models.Q(name__icontains=query) | models.Q(description__icontains=query))


class Course(models.Model):

    name = models.CharField('Name', max_length=100)
    slug = models.SlugField('Shortcut')
    description = models.TextField('Description', blank=True)
    about = models.TextField('Simple Description', blank=True)
    start_date = models.DateField('Start Date', null=True, blank=True)
    image = models.ImageField(upload_to='courses/images', verbose_name='Image', null=True, blank=True)
    created_at = models.DateTimeField('Created at', auto_now_add=True)
    updated_at = models.DateTimeField('Last Modified at', auto_now=True)
    objects = CourseManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('courses:details', args=(self.slug,))

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        ordering = ['name']


class Enrollment(models.Model):
    STATUS_CHOICES = (
        (0, 'Pendent'),
        (1, 'Approved'),
        (2, 'Canceled'),
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name='User', related_name='enrollments', on_delete=models.CASCADE
    )
    course = models.ForeignKey(
        Course, verbose_name='Course', related_name='enrollments', on_delete=models.CASCADE
    )
    status = models.IntegerField('Situation', choices=STATUS_CHOICES, default=1, blank=True)

    created_at = models.DateTimeField('Created at', auto_now_add=True)
    updated_at = models.DateTimeField('Last Modified at', auto_now=True)

    def active(self):
        self.status = 1
        self.save()

    class Meta:
        verbose_name = 'Enrollment'
        verbose_name_plural = 'Enrollments'
        unique_together = (('user', 'course'),)
