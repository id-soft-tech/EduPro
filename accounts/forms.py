from django.forms import ModelForm
from .models import School, Teacher, Student

class SchoolForm(ModelForm):
    class Meta:
        model = School
        fields = ['name', 'alias', 'email']

class TeacherForm(ModelForm):
    model = Teacher
    fields = ('fullname', 'username', 'last_name', 'email', 'password')

class StudentForm(ModelForm):
    model = Student
    fields = ('first_name', 'last_name', 'email', 'password', 'grade')
