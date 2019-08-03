# Employee Manager

[![CircleCI](https://circleci.com/gh/djonathanb/employee_manager/tree/master.svg?style=shield)](https://circleci.com/gh/djonathanb/employee_manager/tree/master)



## Running the project

> :bulb: **Tip:** You should run the project from a virtual environment

> Don't forget to install dependencies from `requirements.txt` on your environment

### The first time here

If it's the first time you're running the project, you must run the following commands:

```python manage.py migrate```

You should also create the superuser with the following command:

```python manage.py createsuperuser```


### Getting the project alive

You can get the project alive by running the following command:

```python manage.py runserver```



## Exploring the project

After running the project at **localhost**, you have access to the following endpoints guaranted:


### Root

http://localhost:8000/


### Admin

http://localhost:8000/admin/


### API

http://localhost:8000/api/


### API (Docs)

http://localhost:8000/api/docs/
