# django-template

## Neue App
* `django-admin startproject {appname}`
* appname/urls.py
```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view, name="viewname"),
]
```
* django/urls.py add `path('appname/', include('appname.urls')),`
* appname/views.py
```
def view(request):
    return render(request, "appname/appname.html")
```
* templates/appname/appname.html:
```
{% extends "base.html" %}

{% block title %}
appname
{% endblock %}

{% block content %}
<h1>appname</h1>
{% endblock %}
```

## run server
* python packages: `python3 install -r requirements.txt`
* load initial data after generating data.json: `py manage.py loaddata data.json`
* run server: `py manage.py runserver`

## css/sass
* `sudo apt install npm nodejs`
* `npm install`
* `npm run sass`
