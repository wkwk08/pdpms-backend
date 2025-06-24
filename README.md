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
<!--
4. **Set Up the Database on Windows (PostgreSQL)** 
First, download the .sql file, which can be found in our repository. Then, open a Command Prompt (cmd) and run the following commands:
```
cd C:\Users\DELL\Downloads  REM This will locate where your .sql file is stored
set PATH=%PATH%;C:\Program Files\PostgreSQL\17\bin
set PGPASSWORD=your_database_password
psql -U postgres -c "CREATE DATABASE accounting_db;"
psql -U postgres -d accounting_db -f accounting_db_dump.sql
```

5. **Configure Database Settings (settings.py)**
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'accounting_db',
        'USER': 'postgres',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '5432',
        'OPTIONS': {
            'options': '-c search_path=accounting'
        }
    }
}
# Found in accounting_backend
```
!-->

4. **Apply Migrations**
```
$ python manage.py makemigrations
$ python manage.py migrate
```

7. **Create a Superuser**
```
$ python manage.py createsuperuser
```

5. **Run server**
```
$ python manage.py runserver
```