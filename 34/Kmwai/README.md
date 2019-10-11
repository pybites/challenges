# cat-api
Simple api written in Django

This is challenge 34 on the ['pybites challenges'](https://pybit.es/)

## installation

* Clone repo

   *  ```git clone <URL>```

* Create virtual environment

   * ```virtualenv -p python3 envname```

* Activate venv environment

   * ```source env/bin/activate```

* Install the requirements

   *  ```pip install requirements.txt```

* Migrate to set up database tables for use

   * ```./manage.py migrate``` 

* Create admin user

   * ```./manage.py createsuperuser``` 

* Run

   * ```./manage.py runserver```

## RESTful structure

| Endpoint       | HTTP Method     | Crud method  | Result               |
| -------------  |:---------------:| ------------:| --------------------:|
| cats           | GET             | READ         | Get all cats         | 
| cats/:id       | GET             | READ         | Get a single cat     |  
| cats           | POST            | CREATE       | Add a single cat     |   
| cats/:id       | PUT             | UPDATE       | Update a single cat  |
| cats/:id       | DELETE          | DELETE       | Delete a single cat  |

Deployed on Heroku. [django-cat-api](https://django-cat-api.herokuapp.com)
