from django.urls import path
from . import views


app_name = 'courses'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:slug>/', views.details, name='details'),
    path('<str:slug>/enrollment/', views.enrollments, name='enrollment'),
    path('<str:slug>/announcements/', views.announcements, name='announcements'),
    path('<str:slug>/lessons/', views.lessons, name='lessons'),
    path('<str:slug>/lesson/', views.lesson, name='lesson'),
    path('<str:slug>/undo-enrollment/', views.undo_enrollment, name='undo_enrollment'),
    path('<str:slug>/show-announcement/<str:pk>/', views.show_announcement, name='show_announcement')
]
