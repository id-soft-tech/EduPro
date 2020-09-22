from django.contrib import admin
from .models import School, Teacher, Student

# Register your models here.
admin.site.register((School, Teacher, Student))