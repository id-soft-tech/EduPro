from django.db import models
from accounts.models import Teacher

# Create your models here.
class Homework(models.Model):
    GRADE_CHOICES = (
        ('1',"1 класс"), ('2',"2 класс"),
        ('3', "3 класс"), ('4', "4 класс"),
        ('5', "5 класс"), ('6', "6 класс"),
        ('7', "7 класс"), ('8', "8 класс"),
        ('9', "9 класс"), ('10', "10 класс"),
        ('11', "11 класс"),
    )
    DURATION_TIME = (
        ('1', '1 день'), ('2', '2 дня'),
        ('3', '3 дня'), ('4', '4 дня'),
        ('5', '5 дней'), ('6', '6 дней'),
        ('7', '7 дней'),
    )
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    grade = models.CharField(max_length=255, choices=GRADE_CHOICES)
    task = models.TextField()
    subject = models.CharField(max_length=255)
    created = models.DateTimeField()
    duration = models.CharField(max_length=255, choices=DURATION_TIME)

    def __str__(self):
        return self.subject
    
    class Meta:
        ordering = ['id']