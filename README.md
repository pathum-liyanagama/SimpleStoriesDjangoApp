# Simple Stories

A simple web application using Django where it allows anyone to create small
“stories” where a story consists of a title, content/description and a rating. On the index
page, 5 most recent stories will be listed in the descending order of created date time,
latest being at the top. Readers can submit a rating for stories.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

1. Python 3.4.x or later
2. pip
3. virtualenv or pyenv
4. Django 2.0.1
5. Database SQLite


### Installing

A step by step series of examples that tell you have to get a development env running

Create a virtual environment

```
pyenv install 3.5.0
```
```
pyenv virtualenv 3.5.0 simplestories
```
```
pyenv activate simplestories
```
Install Django

```
pip install django
```
Goto inside the project folder and run
```
python manage.py runserver
```

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [SQLite](https://www.sqlite.org/) - Database Management

## Authors

* **Pathum Liyanagama** - *Initial work*
## License



## Acknowledgments
* [David Miller](http://davidmiller.io/) for Bootstrap templates and themes.
* Thank you for everyone who's code was used
