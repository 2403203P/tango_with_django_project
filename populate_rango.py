import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():
# First, we will create lists of dictionaries containing the pages 
# we want to add into each category. 
# Then we will create a dictionary of dictionaries for our categories.
# This might seem a little bit confusing, but it allows us to iterate 
# through each data structure, and add the data to our models.
	python_pages=[{'title': 'Official Python Tutorial', 
        'url':'http://docs.python.org/3/tutorial/'}, 
        {'title':'How to Think like a Computer Scientist', 
        'url':'http://www.greenteapress.com/thinkpython/'}, 
        {'title':'Learn Python in 10 Minutes', 
        'url':'http://www.korokithakis.net/tutorials/python/'} ]
 
    django_pages=[ {'title':'Official Django Tutorial', 26 'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/'}, 27 {'title':'Django Rocks', 28 'url':'http://www.djangorocks.com/'}, 29 {'title':'How to Tango with Django', 30 'url':'http://www.tangowithdjango.com/'} ]]