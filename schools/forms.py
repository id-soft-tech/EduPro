from django.forms import ModelForm
from .models import School

class SchoolForm(ModelForm):
    class Meta:
        model = School
        fields = ['name', 'alias', 'email']