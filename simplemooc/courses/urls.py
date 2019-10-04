from django.urls import path
from . import views


app_name = 'courses'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:slug>/', views.details, name='details'),
    path('<str:slug>/enrollment/', views.enrollments, name='enrollment'),
    path('<str:slug>/announcements/', views.announcements, name='announcements')
]
