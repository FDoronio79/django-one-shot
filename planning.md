# Setup
* [x] Fork and clone the starter project from django-one-shot
  * [x] git clone https://gitlab.com/DoronioF/django-one-shot.git
* [x] Create a new virtual environment in the repository directory for the project
  * [x] python -m venv .venv
* [x] Activate the virtual environment
  * [x] source .venv/bin/activate
* [x] Upgrade pip
  * [x] pip install --upgrade pip
* [x] Install django
  * [x]pip install django
* [x] Install black
  * [x] pip install black
* [x] Install flake8
  * [x] pip install flake8
* [x] Install djlint
  * [x] pip install djlint
* [ ] Install debug toolbar
  * [ ] pip install django-debug-toolbar
* [x] Deactivate your virtual environment
  * [x] deactivate
* [x] Activate your virtual environment
  * [x] source .venv/bin/activate
* [x] Use pip freeze to generate requirements.txt file
  * [x] pip freeze > requirements.txt

# References
* https://learn-2.galvanize.com/cohorts/3352/blocks/1859/content_files/build/02-django-one-shot/65-django-one-shot-01.md

# Feature 2
* [x] Create a Django project named brain_two so that the manage.py file is in the top directory
  * [x] django-admin startproject brain_two .
* [x] Create a Django app named todos
  * [x] python manage.py startapp todos
* [x] Install it into the brain_two Django project in the INSTALLED_APPS list
  * [x] brain_two/settings.py/INSTALLED_APPS
* [x] Run the migrations
  * [x] python manage.py makemigrations
  * [x] python manage.py migrate
* [x] Create super user
  * [x] python manage.py createsuperuser

# Feature 3
* [x]Create a model named TodoList model in todos app
  * [x]todos/models.py
* [x] TodoList model should implicitly convert to a string with the __str__ method that is the value of the name property
  * [x] def __str__(self):
        * return self.name
* [x] Make migrations
  * [x] stage migrations
    * [x] python manage.py makemigrations
  * [x] apply migrations
    * [x] python manage.py migrate

