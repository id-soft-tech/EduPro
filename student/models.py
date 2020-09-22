from django.db import models
from teacher.models import Homework
from accounts.models import Student, Test, Question
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='/media/homework/')

# Create your models here.

class EnrolledTesting(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, related_name='test', on_delete=models.CASCADE)
    result = models.IntegerField(default=0)
    started = models.DateTimeField()
    istaken = models.BooleanField(default=False)

class DoneHomework(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE, related_name='done_homework')
    subject = models.CharField(max_length=255)
    done = models.BooleanField(default=False)
    checked = models.BooleanField(default=False)
    checkedDate = models.DateField(null=True)
    note = models.CharField(max_length=255, blank=True)
    mark = models.IntegerField(default=0)

    def __str__(self):
        return self.homework.subject

class ImagesHomework(models.Model):
    name = models.CharField(max_length=50)
    done_homework = models.ForeignKey(DoneHomework, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='homework/')