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

# Feature 4
* [x] Register ToDoList model with the admin so that we can use it in the Django admin site
  * [x] todos/admin.py
    * [x] in the admin.py file enter:
      * [x] from todos.models import ToDoList
      * [x] admin.site.register(ToDoList)

# Feature 5
* [x] Create a ToDoItem model in todos app
  * class ToDoItem(models.Model):
  * [x] todos/models.py
    * [x] create attributes with the following features:
        *  Name - Type - Constraints
      * [x] task - string - max leng of 100 characters
          * task = models.CharField(max_length=100, null=True)
      * [x] due_date - date time - should be optional
          * due_date = models.DateTimeField(null=True)
      * [x] is_completed - boolean - should default to False
          * is_completed = models.BooleanField(default=False)
      * [x] list - foreign key - should be related to the TodoList model and have a related name of "items". It should automatically delete if the to-do list is deleted. (This is a cascade.)
          * list = models.ForeignKey(ToDoList, related_name="items", on_delete=models.CASCADE)
    * [x] ToDoItem model should implicitly convert to a string with the __str__ method that is the value of the task property
  * [x] Make migrations
    * [x] stage migration
      * [x] python manage.py makemigrations
    * [x] apply migrations
      * [x] python manage.py migrate

# Featuere 6
* [x] register ToDoItem to admin
  * [x] admin.site.register(ToDoItem) 

# Feature 7
* [x] Create a list view for the ToDoList model and put them in the context for the template
* [x] Register that the view in the todos app for the path "" and the name "todo_list_list" in a new file named todos/urls.py
* [x] Include the URL patterns from the todos app in the brain_two project with the prefix "todos/"
* [ ] Create a template for the list view that complies with the following specifications.
  * [x] fundamental five
  * [x] main tag that contains
    * [x] div tag that contains
      * [x] h1 tag with the content "My List"
        * [x] a table that has two columns:
          * [x] the first with the header "Name" and the rows with the names of the ToDo lists
          * [x] the second with the header "Number of items" and nothin in those rows because they don't yet have tasks

# Feature 8 
* [x] Create a view that show the details of a particular to-do list, including its tasks
* [x] In the todos urls.py file, register the view with the path "<int:pk>/" and the name "todo_list_detail"
* [x] Create a template to show the details of the todolist and a table of its to-do items
* [x] Update the list template to show the number of to-do items for a to-do list
* [x] Update the list template to have a link from the to-do list name to the detail view for that to-do list
* [ ] Template specifications
  * [x] fundamental five
  * [x] main tag containing
    * [x] div tag containing
      * [x] h1 tag with the to-do list's name as its content
      * [x] h2 tag that has the content "Tasks"
        * [x] a table that contains two columns with the headers "Task" and "Due date" with rows for each task in the to-do list

# Feature 9