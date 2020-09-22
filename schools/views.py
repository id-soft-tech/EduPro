from django.shortcuts import render, redirect
from accounts.forms import SchoolForm
from accounts.models import School, Teacher, Student
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.core import serializers
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def schoolMainPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        return redirect('/schools/school_registration')


def school_registration(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            form = SchoolForm(request.POST)
            if form.is_valid():
                form.save()
                name = form.cleaned_data.get('name')
                password = request.POST.get('password')
                email = form.cleaned_data.get('email')
                alias = form.cleaned_data.get('alias')
                try:
                    user = User.objects.create_user(password=password, email=email, username=alias, is_staff=True, first_name=name, last_name='school')
                    user.save()
                    login(request, user)
                except:
                    messages.info(request, 'Введённый EduName существует')
                    return redirect('/schools/school_registration/')
                return redirect('/')
        else:
            return render(request, 'schools/schoolRegistration.html')

def school_login(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            alias = request.POST.get('alias')
            password = request.POST.get('current-password')
            school = authenticate(username=alias, password=password)
            if school is not None:
                login(request, school)
                return redirect('/')
            else:
                messages.info(request, 'Введённая школа не существует')
                return redirect('/schools/school_login/')
        else:
            return render(request, 'schools/schoolLogin.html')

def logout_school(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            logout(request)
            return redirect('/')
        else:
            return redirect('/')
    else:
        return redirect('/')

def list_teachers(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            school = School.objects.get(alias=request.user.username)
            teachers = school.teacher_set.all()
            return render(request, 'schools/teachers.html', {'teachers':teachers})
        else:
            return redirect('/')

def list_students(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            school = School.objects.get(alias=request.user.username)
            students = Student.objects.filter(school_id=school.id)
            return render(request, 'schools/students.html', {'students': students})
        else:
            return redirect('/')

def deleting_teacher(request, teacher_id):
    if request.user.is_authenticated:
        if request.user.is_staff:
            if request.method == 'POST':
                teacher = Teacher.objects.get(id=teacher_id)
                teacher.delete()
                messages.info(request, 'Учитель был успешно удалён')
                return redirect('/schools/teachers/')
        else:
            return redirect('/')

def deleting_student(request, student_id):
    if request.user.is_authenticated:
        if request.user.is_staff:
            if request.method == 'POST':
                student = Student.objects.get(id=student_id)
                student.delete()
                messages.info(request, 'Ученик был успешно удалён')
                return redirect('/')
        else:
            return redirect('/')