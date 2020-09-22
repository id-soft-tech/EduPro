from django.db import models

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
class School(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=50)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return '%s' % self.name
    
    class Meta:
        ordering = ['id']

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
    
class Student(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255)
    username = models.CharField(max_length=50)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    grade = models.CharField(max_length=50, choices=GRADE_CHOICES)
    grade_letter = models.CharField(max_length=50, choices=GRADE_LETTER_CHOICES)

    def __str__(self):
        return '%s - %s класс' % (self.fullname, self.grade)

    class Meta:
        ordering = ['id']


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
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255) 
    created = models.DateTimeField()
    grade = models.CharField(max_length=255, choices=GRADE_CHOICES)
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