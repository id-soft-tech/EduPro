from django.db import models
from teacher.models import Teacher

# Create your models here.

class Test(models.Model):
    DURATION_CHOICES = (
        ('15', '15 минут'), ('30', '30 минут'),
        ('60', '1 час'), ('90', '1 час 30 минут'),
        ('120', '2 часа'), ('150', '2 часа 30 минут'),
        ('180', '3 часа'),
    )
    QUANTITY_CHOICES = (
        ('5', '5'), ('10', '10'),
        ('15', '15'), ('20', '20'),
        ('25', '25'), ('30', '30')
    )
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    group_grade = models.IntegerField()
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255) 
    created = models.DateTimeField()
    start_date = models.DateField()
    end_date = models.DateField()
    author = models.CharField(max_length=255)
    duration = models.CharField(max_length=3, choices=DURATION_CHOICES)
    quantity = models.CharField(max_length=2, choices=QUANTITY_CHOICES)
    left = models.IntegerField()

    def __str__(self):
        return '%s - %s' % (self.name, self.subject)
    
    class Meta:
        ordering = ['id']


class Question(models.Model):
    ANSWER_CHOICES = (
        ('1', '1'), ('2', '2'),
        ('3', '3'), ('4', '4'),
    )
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=500)
    answer = models.CharField(max_length=2, choices=ANSWER_CHOICES)

    def __str__(self):
        return '%s' % self.question_text

    class Meta:
        ordering = ['id']


class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option_text = models.CharField(max_length=255)
    option_number = models.IntegerField()

    def __str__(self):
        return '%s' % self.option_text

    class Meta:
        ordering = ['id']
