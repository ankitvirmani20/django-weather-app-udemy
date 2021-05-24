# django-weather-app-udemy
Django and Python course notes
Some of the things to note in here are:

1. The core API that is used to fire this code is taken from : https://www.airnow.gov/
You need to sign up and the email confirmation contains the API key to be used to fecth the data

2. To avoid VM/Machine level version control issues, Django package was installed in a venv (virtual envirnoment) in Python, along with other libraries, to manage package level dependencies at the venv level

3. Python 3 was installed on the VM


sudo apt-get update

sudo apt install python3

sudo apt-get install python3-pip

pip3 install virtualenv

sudo apt-get install python3-venv
-------------------------------------------------------
4. Create a virtual environment
python3 -m venv venv
--------------------------------------------------------
Activate virtual environment
source venv/bin/activate
--------------------------------------------------------

Install Django in the virtual environment
pip3 install django

Create a django project
django-admin.py startproject projectname
Ex- 
django-admin.py startproject weather

---------------------------------------------------------
To check whether django server is running correctly: (venv) ankitvirmani@django-website:~/djangoweather/weather$ python3 manage.py runserver

Now open another instance of the VM using SSH and install lynx
sudo apt-get install lynx

Now try opening the django server on this machine: lynx http://127.0.0.1:8000/
------------------------------------------------------------

Setup administrative user and migrate database
python3 manage.py migrate

python3 manage.py createsuperuser
-----------------------------------------------------------
Create a new app: lookup
python3 manage.py startapp lookup
----------------------------------------------------------
Add the lookup app to the list of apps in the project’s settings.py file
nano weather/settings.py
----------------------------------------------------------



Create urls.py file in the lookup app folder
Copy the following content from the project’s urls.py file and add it to the newly created urls.py file in the app folder
from django.contrib import admin
from django.urls import path
urlpatterns = [
   path('admin/', admin.site.urls),
]
Nano urls.py

Add the app’s urls.py file path to the urls.py file of the project
from django.contrib import admin
from django.urls import path,include
urlpatterns = [
   path('admin/', admin.site.urls),
   path('',include('lookup.urls')),
]

This should be the urls.py file of the weather project

Create templates, url.py and views.py files- all inside the app folder (app in this case is named called lookup)
mkdir templates
This folder contains the html files that are served to the user


