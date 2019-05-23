# ShopAPI
A simple sales web api
## How to Install:
1. Clone the repository
2. Create a virtual environment and install the requirements.

    pip install -r requirements.txt

3. Create postgreSQL database using postgreSQL command line, download v11.3 here: (https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)

    CREATE DATABASE cart

4. Modify the DATABASES dictionary in __ShopAPI/sales/settings.py__ so that the __'USER', 'PASSWORD', 'HOST', and 'PORT'__ match the postgreSQL database you created.

5. Make your migrations

    python manage.py makemigrations
    python manage.py migrate

6. Run the server

    python manage.py runserver

7. You're good to go!
