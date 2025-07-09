# pdpms-backend

Django-based backend for Public Document and Property Management System with RESTful API.
## Prerequisites
- Python 3.8+
- pip
- Virtualenv (recommended)
- PostgreSQL

### Installation 

1. **Clone the repository**
```
$ git clone https://github.com/wkwk08/pdpms-backend
$ cd pdpms-backend
```

2. **Create and activate a virtual environment**
```
$ python -m venv venv
$ venv\Scripts\activate
```

3. **Install dependencies**
```
$ pip install -r requirements.txt
```

4. **Switch to pdpms/main branch**
```
$ git checkout pdpms/main
```

5. **Configure Database Settings (settings.py)**
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'pdpms-DB',
        'USER': 'postgres',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '5432',
        'OPTIONS': {
            'options': '-c search_path=pdpms'
        }
    }
}
```

6. **Apply Migrations**
```
$ python manage.py makemigrations
$ python manage.py migrate
```

7. **Create a Superuser**
```
$ python manage.py createsuperuser
```

8. **Run server**
```
$ python manage.py runserver
```