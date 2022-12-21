# Gift Shop
Gift Shop ECommerce

## Requirements
Tools and packages required to successfully install this project.\
Python 3.8.10 above\
Django 3.2.16

## Installation
1.Create a Virtual Environment in your system\
2.Activate Virtual Environment source env/bin/activate\
3.Install Requirements Package pip install -r requirements.txt\

4.Create your .env file\
In the BASE directory  create a file called ‘.env’\
5.Declare your environment variables in .env\
  same as declare in .env.sample file\
Make sure you don’t use quotations around strings.


6.Migrate Database python manage.py migrate\
7.python manage.py oscar_populate_countries\
8.Create Super User python manage.py createsuperuser\
8.Finally Run The Project python manage.py runserver

