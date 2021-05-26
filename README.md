# akvelon_python_internship_3_Radif_Kurbanov
REST API finance manager for Akvelon.

In this project used:
Django, Django REST Framework, PostgreSQL.

Clone the GitHub repository:
```
git clone git@github.com:kurrbanov/akvelon_python_internship_3_Radif_Kurbanov.git
```

Create the venv:
```
python3 -m venv venv
source venv/bin/activate
```

Install the Django, DRF etc.
```
pip3 install django django-rest-framework psycopg2
```

Installing PostgreSQL:
```
sudo apt-get install postgresql postgresql-contrib
sudo apt-get install libpq-dev python3-dev
```

Running PostgreSQL:
```
sudo -u postgres psql
```

Create the db and user:
```
CREATE DATABASE akvelon_db;
CREATE USER akvelon_user;
```

Modifying connection parameters:
```
ALTER ROLE akvelon_user SET client_encoding TO 'utf8';
ALTER ROLE akvelon_user SET timezone TO 'UTC';
```

Granting permission to the user:
```
GRANT ALL PRIVILEGES ON DATABASE akvelon_db TO akvelon_user;
```
