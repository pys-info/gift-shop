# Gift Shop
This is Gift Shop Project based on E-commerce.\
Gift Shop allows people to buy and sell physical goods, services.\
Through a  Gift Shop website, a business can process orders, accept payments, manage shipping and logistics, and provide customer service.

## License

[MIT](https://choosealicense.com/licenses/mit/)\
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)

## Requirements
Tools and packages required to successfully install this project.\
Python 3.8.10 above\
Django 3.2.16\
django-oscar 3.1

## Installation
1.Create a Virtual Environment in your system\

2.Activate Virtual Environment source env/bin/activate\

3.Install Requirements Package like.\
```bash
pip install -r requirements.txt
```
4.Create your '.env' file in the BASE directory\

5.Declare your environment variables in .env, same as declare in .env.sample file\
Make sure you don’t use " " quotations around strings like this.
```bash
example=test
```
6.Run  Makemigrations Command For Database changes \
```bash
python manage.py makemigrations
```

7.Run  Migrate Command For  Database Create \
```bash
python manage.py migrate
```

8.Populate Countries for project
```bash
python manage.py oscar_populate_countries
```
9.Create Super User 
```bash
python manage.py createsuperuser
```
10.Finally Run The Project 
```bash
python manage.py runserver
```


