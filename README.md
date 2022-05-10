# Django Rest Framework Practice

A Python repository to practice Django Rest Framework operations.

## Applications

The following are the installed, custom applications and their purpose.

### 1. app_v1

This app is for basic API implementation practice such as:
  
- Create Model Data from json as input data.
- Retrieving Model Data in json as output data.
- Batch Create Model Data from json file using Pandas.
- Rank Model data using query params as input params.

## Development Setup

1. `python -m pip install --upgrade pip`
2. `pip install pip-tools`
3. `pip-compile`
4. `pip install -r requirements.txt`
5. `python manage.py migrate`
6. `python manage.py createsuperuser`
7. `python manage.py runserver`

## .env File Format

```env
## Website Encryption:
SECRET_KEY = ' '

## Local Database Settings:
DATABASE = ' '
USER = ' '
PASSWORD = ' '
HOST = ' '
PORT =  INT

## Site Settings:
DEBUG =  BOOL
LANGUAGE_CODE = ' '
TIME_ZONE = ' '
USE_I18N =  BOOL
USE_TZ =  BOOL
```

## Documentation

Postman documentation can be found [HERE](https://documenter.getpostman.com/view/17779018/UyxepoUT).
