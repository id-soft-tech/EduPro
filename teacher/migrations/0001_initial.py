# Generated by Django 3.1.1 on 2020-10-03 03:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schools', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('likes', models.IntegerField(default=0)),
                ('number_of_tests', models.IntegerField(default=0)),
                ('number_of_lessons', models.IntegerField(default=0)),
                ('tested_pupils', models.IntegerField(default=0)),
                ('sentHomeworks', models.IntegerField(default=0)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schools.school')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(choices=[('1', '1 класс'), ('2', '2 класс'), ('3', '3 класс'), ('4', '4 класс'), ('5', '5 класс'), ('6', '6 класс'), ('7', '7 класс'), ('8', '8 класс'), ('9', '9 класс'), ('10', '10 класс'), ('11', '11 класс')], max_length=255)),
                ('task', models.TextField()),
                ('subject', models.CharField(max_length=255)),
                ('created', models.DateTimeField()),
                ('duration', models.CharField(choices=[('1', '1 день'), ('2', '2 дня'), ('3', '3 дня'), ('4', '4 дня'), ('5', '5 дней'), ('6', '6 дней'), ('7', '7 дней')], max_length=255)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.teacher')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
