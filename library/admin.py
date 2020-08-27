from django.contrib import admin

# Register your models here.
from .models import Book

# Connecting Book Model to be accessible in Admin Page
admin.site.register(Book)