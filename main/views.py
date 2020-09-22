from django.shortcuts import render, redirect
from accounts.models import Test, Teacher, School, Student
from teacher.models import Homework
from student.models import DoneHomework, ImagesHomework
from django.contrib import messages
from django.core import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import JsonResponse

import datetime
# Create your views here.
def indexPage(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            school = School.objects.get(alias=request.user.username)
            context = {
                'isVisible': True,
            }
            numberOfStudents = Student.objects.filter(school_id=school.id)
            numberOfTeachers = Teacher.objects.filter(school_id=school.id)
            if len(numberOfStudents) == 0 and len(numberOfTeachers) == 0:
                context['isVisible'] = False

            return render(request, 'schools/schoolMainPage.html', context)
        else:
            if request.user.last_name == 'teacher':
                tests = Test.objects.all()
                now = datetime.datetime.now()
                now_after_week = now.replace(day=now.day + 7)
                teacher = Teacher.objects.get(username=request.user.username)
                homeworks = Homework.objects.filter(teacher_id=teacher.id)
                return render(request, 'teacher/teacherMainPage.html', {'tests': tests, 'now': now, 'teacher':teacher, 'now_after_week': now_after_week, 'homeworks': homeworks})
            elif request.user.last_name == 'student':
                student = Student.objects.get(username=request.user.username)
                if request.method == 'POST':
                    pass
                else:
                    list_homeworks = Homework.objects.filter(grade=student.grade)
                    homeworks = list(list_homeworks)
                    finishedHomeworks = DoneHomework.objects.filter(student_id=student.id)
                    for i in range(len(finishedHomeworks)):
                        if finishedHomeworks[i].done:
                            if finishedHomeworks[i].homework in list_homeworks:
                                homeworks.remove(finishedHomeworks[i].homework)
                return render(request, 'student/studentMainPage.html', {'homeworks': homeworks})
    else:
        return render(request, 'main/index.html')

def login_user(request):
    if request.user.is_authenticated:
        if request.user.last_name == 'teacher':
                tests = Test.objects.all()
                now = datetime.datetime.now()
                teacher = Teacher.objects.get(username=request.user.username)
                return render(request, 'teacher/teacherMainPage.html', {'tests': tests, 'now': now, 'teacher':teacher})
        elif request.user.last_name == 'student':
            return render(request, 'student/studentMainPage.html')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Введеный пользователь не существует')
                return redirect('/')

def about(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'main/about.html')

def list_teachers(request):
    if request.user.is_authenticated:
        if request.user.last_name == 'school':
            school = School.objects.get(alias=request.user.username)
            teachers = Teacher.objects.filter(school_id=school.id)
            teacher_list = serializers.serialize('json',  teachers)
            return JsonResponse(teacher_list, safe=False)


def list_students(request):
    if request.user.is_authenticated:
        if request.user.last_name == 'school':
            school = School.objects.get(alias=request.user.username)
            students = Student.objects.filter(school_id=school.id)
            student_list = serializers.serialize('json',  students)
            return JsonResponse(student_list, safe=False)


def tested_pupils(request):
    if request.user.is_authenticated:
        if request.user.last_name == 'teacher':
            teacher = Teacher.objects.get(username=request.user.username)
            tested_pupils = teacher.tested_pupils
            tests = Test.objects.filter(teacher_id=teacher.id)
            context = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            for test in tests:
                if int(test.created.date().month) == 9:
                    context[0] += 1
                elif int(test.created.date().month) == 10:
                    context[1] += 1
                elif int(test.created.date().month) == 11:
                    context[2] += 1
                elif int(test.created.date().month) == 12:
                    context[3] += 1
                elif int(test.created.date().month) == 1:
                    context[4] += 1
                elif int(test.created.date().month) == 2:
                    context[5] += 1
                elif int(test.created.date().month) == 3:
                    context[6] += 1
                elif int(test.created.date().month) == 4:
                    context[7] += 1
                elif int(test.created.date().month) == 5:
                    context[8] += 1

            return JsonResponse(context, safe=False)


def list_homework(request):
    if request.user.is_authenticated:
        if request.user.last_name == 'teacher':
            teacher = Teacher.objects.get(username=request.user.username)
            homeworks = Homework.objects.filter(teacher_id=teacher.id)
            context = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            for hw in homeworks:
                if int(hw.created.date().month) == 9:
                    context[0] += 1
                elif int(hw.created.date().month) == 10:
                    context[1] += 1
                elif int(hw.created.date().month) == 11:
                    context[2] += 1
                elif int(hw.created.date().month) == 12:
                    context[3] += 1
                elif int(hw.created.date().month) == 1:
                    context[4] += 1
                elif int(hw.created.date().month) == 2:
                    context[5] += 1
                elif int(hw.created.date().month) == 3:
                    context[6] += 1
                elif int(hw.created.date().month) == 4:
                    context[7] += 1
                elif int(hw.created.date().month) == 5:
                    context[8] += 1
            return JsonResponse(context, safe=False)


def student_achievement(request):
    if request.user.is_authenticated:
        if request.user.last_name == 'student':
            student = Student.objects.get(username=request.user.username)

