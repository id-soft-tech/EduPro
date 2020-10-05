from django.db import models
from student.models import Student

# Create your models here.

class Mark(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	subject = models.CharField(max_length=100)
	important = models.BooleanField(default=False)
	mark = models.IntegerField()
	date = models.DateField(auto_now_add=True)

	class Meta:
		ordering = ['student']