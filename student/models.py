from django.db import models
from teacher.models import Homework
from test_app.models import Test
from schools.models import School


GRADE_CHOICES = (
    ('1',"1 класс"), ('2',"2 класс"),
    ('3', "3 класс"), ('4', "4 класс"),
    ('5', "5 класс"), ('6', "6 класс"),
    ('7', "7 класс"), ('8', "8 класс"),
    ('9', "9 класс"), ('10', "10 класс"),
    ('11', "11 класс"),
)
GRADE_LETTER_CHOICES = (
    ("A", "A"), ("Б", "Б"),
    ("В", "В"), ("Г", "Г"),
    ("Д", "Д"), ("Е", "Е"),
    ("Ё", "Ё"), ("Ж", "Ж")
)

# Create your models here.

class Group(models.Model):
    grade = models.CharField(max_length=50, choices=GRADE_CHOICES)
    grade_letter = models.CharField(max_length=50, choices=GRADE_LETTER_CHOICES)


class Student(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='group')
    fullname = models.CharField(max_length=255)
    username = models.CharField(max_length=50)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return '%s - %s класс' % (self.fullname, self.grade)

    class Meta:
        ordering = ['id']


class EnrolledTesting(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, related_name='test', on_delete=models.CASCADE)
    result = models.IntegerField(default=0)
    started = models.DateTimeField()
    istaken = models.BooleanField(default=False)


class Answer(models.Model):
    enrolledTesting = models.ForeignKey(EnrolledTesting, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=500)
    answer = models.CharField(max_length=500)
    correctAnswer = models.CharField(max_length=500)


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