from django.db import models
from schools.models import School

# Create your models here.

class Teacher(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255)
    username = models.CharField(max_length=50)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    likes = models.IntegerField(default=0)
    number_of_tests = models.IntegerField(default=0)
    number_of_lessons = models.IntegerField(default=0)
    tested_pupils = models.IntegerField(default=0)
    sentHomeworks = models.IntegerField(default=0)
    
    def __str__(self):
        return '%s' % self.fullname

    class Meta:
        ordering = ['id']


class Homework(models.Model):
    DURATION_TIME = (
        ('1', '1 день'), ('2', '2 дня'),
        ('3', '3 дня'), ('4', '4 дня'),
        ('5', '5 дней'), ('6', '6 дней'),
        ('7', '7 дней'),
    )
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    group = models.IntegerField()
    task = models.TextField()
    subject = models.CharField(max_length=255)
    created = models.DateTimeField()
    duration = models.CharField(max_length=255, choices=DURATION_TIME)

    def __str__(self):
        return self.subject
    
    class Meta:
        ordering = ['id']