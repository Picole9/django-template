FROM python:3-alpine
# init
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /django/
# install requirements
COPY requirements.txt /django/
RUN pip install -r requirements.txt
# copy project
COPY . /django/
# migrate
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput
