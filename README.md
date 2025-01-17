# django-practice

Create Python virtual environment 

``python -m venv venv``

then enter into virtual env 

``source venv/bin/activate`` or ``source venv/Scripts/activate``

Now

``pip install django``

``django-admin startproject projectname``
Ex: ``django-admin startproject EmployeManagement``

Now move to EmployeeManagement folder then run below cmd

`` python manage.py runserver ``

which will start the server on port 8000

To create independent modules of project 
`` python manage.py startapp app_name ``

ex: `` python manage.py startapp SkillSet``

