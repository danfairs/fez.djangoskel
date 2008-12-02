Introduction
============

fez.djangoskel provides paster templates for creating Django
projects and applications as eggs. Two templates are currently 
provided.


Usage
=====

Install fez.djangoskel using easy_install. This should also install
paster as a dependency. You should then be able to see two new
templates available:

$ paster create --list-templates
Available templates:
  basic_package:   A basic setuptools-enabled package
  django_app:      Template for a basic Django reusable application
  django_project:  Template for a Django project
  paste_deploy:    A web application deployed through paste.deploy
  
Create a Django project using the django_project template:

paster create -t django_project

Answer the questions that paster asks, and it will create a full
Django project with a template settings file and urls.py.

Applications are created in a similar way:

paster create -t django_app


Difference from Django's own templates
======================================

Django provides its own 'template' app and project generation. 
Why use these templates?

- The primary motivation is that the projects and apps generated
  by these templates are eggs. This means that they can be uploaded
  to PyPI, and other developers will be able to easy_install them.
  
- These templates all provide skeleton documentation in the form
  of HISTORY.txt and README.txt files.
  
- The application template also provides a lot more plumbing to get 
  you started writing tests: a tests module, test settings (which can
  be invoked using python manage.py test --settings=project.settings)
  and test URLConfs and settings that the test client can use.

