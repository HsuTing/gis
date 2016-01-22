# Geographic Information System

This is base on `geodjango`, and it jsut a simple for `Geographic Information System`. If you wnat to know other details about`geodjango`, you can see [here](https://docs.djangoproject.com/en/1.9/ref/contrib/gis/).

## Start

- [pip](https://pypi.python.org/pypi/pip) must be installed.
- [PostgreSQL](http://www.postgresql.org) must be installed.
- Install virtualenv:
```
  pip install virtualenv
```

- Create and open virtual environment:
```
  virtualenv --no-site-packages venv
  source venv/bin/activate
```

- Install packages:
```
  pip install -r requirement.txt
```
If you can not install `psycopg2`, you need to install `python-psycopg2`, `python-dev` and `libpq-dev`.

- Create a project:
```
  django-admin startproject (project name)
```

## Setting

- Get in project:
```
  cd (project name)
```

- Open project `settings.py`:
```
  vim (project name)/settings.py
```
and modify `INSTALLED_APPS` and `DATABASES`:
```
  ...
  INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
  ]
  ...
  DATABASES = {
    'default': {
      'ENGINE': 'django.contrib.gis.db.backends.postgis',
      'NAME': '(change to your postgres database`s name)',
      'USER': '(change to your postgres user`s name)',
      'HOST': 'locolhost',
      'PASSWORD': '(change to your postgres password)',
    }
  }
```

- Run migrate:
```
  python manage.py migrate
```
If you can not `migrate`, you can try to install `postgresql-9.3-postgis-scripts`.

## Server

- Run server(localhost):
```
  python manage.py runserver
```

- Run server(online):
```
  python manage.py runserver 0.0.0.0:(port)
```

## Add app

- [Here](https://github.com/HsuTing/gis/blob/gh-pages/release/README.md) is app list.
- Download and unzip it to project:
```
  wegt https://hsuting.github.io/gis/release/(app name).tar.gz
  tar -C (project name) -zvxf (app name).tar.gz
```

- Add app to your project `settings.py`:
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    '(app name)',
]
```

- Add url to your project `urls.py`:
```
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^(app name)/', include('(app name).urls')),
]
```

- Run migrate:
```
python manage.py makemigrations
python manage.py sqlmigrate (app name) (number of migrations)
python manage.py migrate
```
When you run makemigrations, you will get a text like `0001_initial.py`. `0001` is number of migrations.

- Add data to database:
```
python manage.py shell
```
Then you will get in django shell.
```
from (app name) import load
load.run()
```
