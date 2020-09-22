from django.shortcuts import render, redirect, reverse
from accounts.models import School, Teacher, Test, Option, Question, Student
from student.models import EnrolledTesting, DoneHomework
from teacher.models import Homework
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core import serializers
from django.contrib.auth import login, authenticate, logout
from .forms import AddingQuestionForm
import datetime, pytz

utc = pytz.UTC  

# Create your views here.
def teacher_main_page(request):
    if request.user.is_authenticated:
        if request.user.last_name == 'teacher':
            tests = Test.objects.all()
            return render(request, 'teacher/teacherMainPage/html', {'tests': tests})
        else:
            return redirect('/')
    else:
        # Redirects to verification page (teacher is asked to type the alias and password of the school)
        return redirect('/teacher/teacher_registration/')


def teacher_registration(request):
    if request.user.is_authenticated:
        if request.user.last_name == 'teacher':
            return render(request, '/teacher/teacherMainPage.html')
        else:
            return redirect('/')
    else:
        if request.method == 'POST':
            fullname = request.POST.get('fullname')
            last_name = 'teacher'
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            alias = request.POST.get('alias')
            school_password = request.POST.get('school_password')
            try:
                u = User.objects.get(username=username)
                if u is not None:
                    messages.info(request, 'Пользователь с именем %s уже существует' % username)
                    return redirect('/teacher/teacher_registration/')
            except User.DoesNotExist:
                school_user = authenticate(username=alias, password=school_password)
                if school_user is not None:
                    school = School.objects.get(alias=alias)
                    school.teacher_set.create(fullname=fullname, last_name=last_name, email=email, username=username)
                    user = User.objects.create_user(password=password, email=email, username=username, first_name=fullname, last_name=last_name)
                    user.save()
                    login(request, user)
                    return redirect('/')
                else:
                    messages.info(request, 'EduName школы или пароль введён неправильно')
                    return redirect('/teacher/teacher_registration/')
        else:
            return render(request, 'teacher/teacherRegistration.html')


def teacher_login(request):
    if request.user.is_authenticated:
        if request.user.last_name == 'teacher':
            return render(request, 'teacher/teacherMainPage.html')
        else:
            return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Введённый пользователь не существует')
                return redirect('/teacher/teacher_login/')
        else:
            return render(request, 'teacher/teacherLogin.html')
            
def teacher_logout(request):
    if request.user.is_authenticated:
        if request.user.last_name == 'teacher':
            logout(request)
            return redirect('/teacher/teacher_registration/')
        else:
            return redirect('/')
    else:
        return redirect('/teacher/teacher_registration/')


def change_password(request):
    if request.user.is_authenticated:
        if request.user.last_name == 'teacher':
            if request.method == 'POST':
                password0 = request.POST.get('password0')
                user = authenticate(username=request.user.username, password=password0)
                if user is not None:
                    password1 = request.POST.get('password1')
                    user.set_password(password1)
                    user.save()
                    login(request, user)
                    messages.info(request, 'Пароль был успешно изменен')
                    return redirect('/teacher/viewing_profile/')
                else:
                    messages.info(request, 'Введеный пароль не совпадает со старым паролем')
                    return redirect('/teacher/viewing_profile/')


def viewing_profile(request):
    if request.user.is_authenticated:
        if request.user.last_name == 'teacher':
            if request.method == 'POST':
                pass                   
            else:
                teacher = Teacher.objects.get(username=request.user.username)
                return render(request, 'teacher/profile.html', {'teacher': teacher})
    else:
        return redirect('/teacher/teacher_registration/')
        

def change_username(request):
    if request.user.is_authenticated:
        if request.user.last_name == 'teacher':
            if request.method == 'POST':
                username = request.POST.get('username')
                try:
                    u = User.objects.get(username=username)
                    messages.info(request, 'Пользователь с введённым именем уже существует')
                    return redirect('/teacher/viewing_profile/')
                except User.DoesNotExist:
                    teacher = Teacher.objects.get(username=request.user.username)
                    user = User.objects.get(username=request.user.username)
                    user.username = username
                    user.save()
                    teacher.username = username
                    teacher.save()
                    messages.info(request, 'Имя пользователя было изменено')
                    return redirect('/teacher/viewing_profile/')


def change_fullname(request):
    if request.user.is_authenticated:
        if request.user.last_name == 'teacher':
            if request.method == 'POST':
                fullname = request.POST.get('fullname')
                teacher = Teacher.objects.get(username=request.user.username)
                teacher.fullname= fullname
                teacher.save()
                user = User.objects.get(username=request.user.username)
                user.first_name = fullname
                user.save()
                messages.info(request, 'Полное имя было изменено')
                return redirect('/teacher/viewing_profile/')


def creating_test(request):
    if request.user.is_authenticated:
        if request.user.last_name == 'teacher':
            if request.method == 'POST':
                name = request.POST.get('name')
                subject = request.POST.get('subject')
                grade = request.POST.get('grade')
                start_date = request.POST.get('start_date')
                end_date = request.POST.get('end_date')
                start_date_data = start_date.replace('-', '')
                end_date_data = end_date.replace('-', '')
                duration = request.POST.get('duration')
                quantity = request.POST.get('quantity')
                author = request.user.first_name
                
                now = datetime.datetime.now()
                now = utc.localize(now)

                # Cheking whether a teacher made a mistake by putting ending date of test earlier than starting date
                if int(end_date_data) - int(start_date_data) < 0:
                    messages.info(request, 'Дата закрытия тестирования не может быть раньше чем дата открытия')
                    return redirect('/teacher/creating_test/')
                try:
                    teacher = Teacher.objects.get(username=request.user.username)
                    teacher.test_set.create(name=name, subject=subject, grade=grade, start_date=start_date, end_date=end_date,duration=duration, quantity=quantity, author=author, left=int(quantity), created=now)
                    teacher.number_of_tests += 1
                    teacher.save()
                    return redirect('/')
                except Teacher.DoesNotExist:
                    return redirect('/teacher/teacher_registration/')
            else:
                return render(request, 'teacher/creatingTest.html')
    else:
        return redirect('/teacher/teacher_registration/')


def deleting_test(request, test_id):
    if request.user.is_authenticated:
        if request.user.last_name == 'teacher':
            if request.method == 'POST':
                try:
                    test = Test.objects.get(id=test_id)
                    test.delete()
                    messages.info(request, 'Тестирование было успешно удалено!')
                    return redirect('/')
                except Test.DoesNotExist:
                    messages.info(request, 'Произошла ошибка')
                    return redirect('/')


def adding_questions(request, test_id):
    if request.user.is_authenticated:
        if request.user.last_name == 'teacher':
            if request.method == 'POST':
                question_text = request.POST.get('question_text')
                option1 = request.POST.get('option1')
                option2 = request.POST.get('option2')
                option3 = request.POST.get('option3')
                option4 = request.POST.get('option4')
                correct_answer = request.POST.get('correct_answer')

                test = Test.objects.get(id=test_id)
                question = test.question_set.create(question_text=question_text, answer=correct_answer)
                question.save()

                question.option_set.create(option_text=option1, option_number=1)
                question.option_set.create(option_text=option2, option_number=2)
                question.option_set.create(option_text=option3, option_number=3)
                question.option_set.create(option_text=option4, option_number=4)
                
                if test.left > 0:
                    test.left -= 1

                test.save()
                return redirect('/')
            elif request.method == 'GET':
                test = Test.objects.get(id=test_id)
                return JsonResponse({'test_left':test.left})
    else:
        return redirect('/teacher/teacher_registration/')


def viewing_questions(request, test_id):
    if request.user.is_authenticated:
        if request.user.last_name == 'teacher':
            if request.method == 'POST':
                pass
            else:
                test = Test.objects.get(id=test_id)
                questions = test.question_set.all()
                return render(request, 'teacher/viewingQuestions.html', {'questions':questions, 'test':test})
    else:
        return redirect('/teacher/teacher_registration/')


def changing_question(request, question_id, test_id):
    if request.user.is_authenticated:
        if request.user.last_name == 'teacher':
            if request.is_ajax() and request.method == 'POST':
                question_text = request.POST.get('question_text')
                option1 = request.POST.get('option1')
                option2 = request.POST.get('option2')
                option3 = request.POST.get('option3')
                option4 = request.POST.get('option4')
                answer = request.POST.get('correct_answer')

                question = Question.objects.get(test_id=test_id, id=question_id)
                if question.question_text.strip() != question_text.strip():
                    question.question_text = question_text
                if question.answer != answer:
                    question.answer = answer
                question.save()

                old_op_1 = question.option_set.get(option_number=1)
                old_op_2 = question.option_set.get(option_number=2)
                old_op_3 = question.option_set.get(option_number=3)
                old_op_4 = question.option_set.get(option_number=4)
                
                if old_op_1.option_text.strip() != option1.strip():
                    old_op_1.option_text = option1
                    old_op_1.save()

                if old_op_2.option_text.strip() != option2.strip():
                    old_op_2.option_text = option2
                    old_op_2.save()

                if old_op_3.option_text.strip() != option3.strip():
                    old_op_3.option_text = option3
                    old_op_3.save()

                if old_op_4.option_text.strip() != option4.strip():
                    old_op_4.option_text = option4
                    old_op_4.save() 
                
                messages.info(request, 'Вопрос был успешно обновлен')
                return redirect('/')
    else:
        return redirect('/teacher/teacher_registration/')


def results(request, test_id):
    if request.user.is_authenticated:
        if request.user.last_name == 'teacher':
            if request.method == 'POST':
                pass
            else:
                test = Test.objects.get(id=test_id)
                now = datetime.datetime.now()
                if now.date() > test.end_date:
                    testing_results = EnrolledTesting.objects.filter(test_id=test_id)
                    return render(request, 'teacher/results.html', {'results':testing_results, 'test':test})
                else:
                    return redirect('/')


def homework(request):
    if request.user.is_authenticated:
        if request.user.last_name == 'teacher':
            if request.method == 'POST':
                teacher = Teacher.objects.get(username=request.user.username)
                subject = request.POST.get('subject')
                grade = request.POST.get('grade')
                duration = request.POST.get('duration')
                task = request.POST.get('task')
                now = datetime.datetime.now()
                now = utc.localize(now)
                teacher.homework_set.create(subject=subject, grade=grade, duration=duration, task=task,created=now)
                teacher.number_of_lessons += 1
                teacher.save()
                return redirect('/')
            else:
                return render(request, 'teacher/creatingHomework.html')


def viewing_homework(request, hw_id):
    if request.user.is_authenticated:
        if request.user.last_name == 'teacher':
            if request.method == 'POST':
                pass
            else:
                sentHomeworks = DoneHomework.objects.filter(homework_id=hw_id, done=True)
                return render(request, 'teacher/homeworks.html', {'homeworks': sentHomeworks})


def deleting_homework(request, hw_id):
    if request.user.is_authenticated:
        if request.user.last_name == 'teacher':
            if request.method == 'POST':
                hw = Homework.objects.get(id=hw_id)
                hw.delete()
                messages.info(request, 'Домашнее задание успешно удалено')
                return redirect('/')


def student_homework(request, student_id, done_hw_id):
    if request.user.is_authenticated:
        if request.user.last_name == 'teacher':
            student = Student.objects.get(id=student_id)
            if request.method == 'POST':
                mark = request.POST.get('mark')
                note = request.POST.get('note')
                done_homework = DoneHomework.objects.get(id=done_hw_id)
                done_homework.mark = mark
                done_homework.note = note
                done_homework.checked = True

                now = datetime.datetime.now()
                now_date = now.date()
                done_homework.checkedDate = now_date

                done_homework.save()
                messages.info(request, 'Домашнее задание проверено')
                return redirect('/teacher/%s/viewing_homework/' % done_homework.homework.id)
            else:
                try:
                    homework = DoneHomework.objects.get(id=done_hw_id,student_id=student_id, done=True, checked=False)
                    images = homework.imageshomework_set.all()
                    return render(request, 'teacher/studentHomework.html', {'student': student, 'images': images})
                except DoneHomework.DoesNotExist: 
                    return redirect('/')