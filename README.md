# Learning Django
## 1. Useful commands:
* **Django-admin.py:**

>* Startproject:
>>Starts project with a functional structure  
>>\# python django-admin.py startproject

* **Manage.py:**
>* Help:
>>Starts  ‘Manage.py’ command guide  
>>\# 	python manage.py help

>* Startserver:
>>Starts server at the default address: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)  
>>\#	python manage.py runserver

>* Syncdb:
>>Synchronize your project with your database  
>>\#	python manage.py migrate --run-syncdb

>* Startapp:
>>Since Django is divided in apps, this command creates an app template  
>>\#	python manage.py startapp

>* Makemigrations:
>>Add new modifications to DataBase  
>>\#    python manage.py makemigrations

>* Createsuperuser:
>>Add new super user to Database 
>>\#    python manage.py createsuperuser

>* pip freeze:
>>Create requirements file
>>>\#   pip freeze > requirements.txt