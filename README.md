# django-template

## Neue App
* `django-admin startproject {appname}`
* appname/urls.py
```
from django.urls import path
from . import views

urlpatterns = [
    path('', appname.view, name="viewname"),
    path('oe', appname.view, name="viewname"),
]
```
* django/urls.py add `path('appname/', include('appname.urls')),`
* Beispiel-html:
```
{% extends "base.html" %}

{% block title %}
appname
{% endblock %}

{% block content %}
<h1>appname</h1>
{% endblock %}
```

## Setup
* python packages: `python3 install -r requirements.txt`
* load data: `py manage.py loaddata data.json`
* run server: `py manage.py runserver`

## Development
* `sudo apt install npm nodejs`
* `npm install`
* Styling: `npm run sass`
