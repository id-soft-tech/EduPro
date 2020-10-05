from django.shortcuts import render, redirect
from teacher.models import Teacher, Homework
from schools.models import School
from test_app.models import Test, Question, Option
from .models import EnrolledTesting, DoneHomework, ImagesHomework, Answer, Student, Group
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.core.paginator import Paginator
import datetime, pytz, hashlib, uuid, sys

# FOR COMPRESSING IMAGE
from django.core.files import File
from io import BytesIO
from PIL import Image


# Create your views here.
def student_main_page(request):
    if request.user.is_authenticated:
        if request.user.last_name == 'student':
            return render(request, 'student/studentMainPage.html')
        else:
            # NEED MODIFICATION. WHETHER IT IS A TEACHER OR A SCHOOL
            pass
    else:
        return redirect('/student/student_registration/')


def student_registration(request):
    if request.user.is_authenticated:
        if request.user.last_name == 'student':
            return render(request, 'student/studentMainPage.html')
        else:
            return redirect('/')
    else:
        if request.method == 'POST':
            fullname = request.POST.get('fullname')
            username = request.POST.get('username')
            try:
                user = User.objects.get(username=username)
                if user is not None:
                    messages.info(request, "Пользователь с именем %s уже существует" % username)
                    return redirect('/student/student_registration/')
            except User.DoesNotExist:
                email = request.POST.get('email')
                password = request.POST.get('password')
                grade = request.POST.get('grade'),
                grade_letter = request.POST.get('grade_letter')
                alias = request.POST.get('alias')
                school_password = request.POST.get('school_password')
                
                school_user = authenticate(username=alias, password=school_password)
                if school_user is not None:
                    school = School.objects.get(alias=alias)
                    try:
                        group = Group.objects.get(grade=grade[0], grade_letter=grade_letter)
                    except:
                        group = Group.objects.create(grade=grade[0], grade_letter=grade_letter,student_username=username)
                        group.save()
                    school.student_set.create(fullname=fullname, last_name='student', email=email, username=username, group_id=group.id)
                    user = User.objects.create_user(password=password, email=email, username=username, first_name=fullname, last_name='student')
                    user.save()
                    login(request, user)
                    return redirect('/')
                else:
                    messages.info(request, 'EduName школы или пароль введён неправильно')
                    return redirect('/student/student_registration/')
        else:
            return render(request, 'student/studentRegistration.html')

def student_login(request):
    if request.user.is_authenticated:
        if request.user.last_name == 'student':
            return render(request, 'student/studentMainPage.html')
        else:
            # Modify to check whether it is a school or a teacher
            pass
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
                return redirect('/student/student_login/')
        else:
            return render(request, 'student/studentLogin.html')

def student_logout(request):
    if request.user.is_authenticated:
        if request.user.last_name == 'student':
            logout(request)
            return redirect('/')
        else:
            # NEED TO CHECK WHETHER IT IS A School OR A TEACHER
            pass
    else:
        return redirect('/student/student_registration/')


def change_password(request):
    if request.user.is_authenticated:
        if request.user.last_name == 'student':
            if request.method == 'POST':
                password0 = request.POST.get('password0')
                user = authenticate(username=request.user.username, password=password0)
                if user is not None:
                    password1 = request.POST.get('password1')
                    user.set_password(password1)
                    user.save()
                    login(request, user)
                    messages.info(request, 'Пароль был успешно изменен')
                    return redirect('/student/viewing_profile/')
                else:
                    messages.info(request, 'Введеный пароль не совпадает со старым паролем')
                    return redirect('/student/viewing_profile/')


def viewing_profile(request):
    if request.user.is_authenticated:
        if request.user.last_name == 'student':
            if request.method == 'POST':
                pass
            else:
                student = Student.objects.get(username=request.user.username)
                return render(request, 'student/profile.html', {"student": student})


def change_username(request):
    if request.user.is_authenticated:
        if request.user.last_name == 'student':
            if request.method == 'POST':
                username = request.POST.get('username')
                try:
                    u = User.objects.get(username=username)
                    messages.info(request, 'Пользователь с введённым именем уже существует')
                    return redirect('/student/viewing_profile/')
                except User.DoesNotExist:
                    student = Student.objects.get(username=request.user.username)
                    user = User.objects.get(username=request.user.username)
                    user.username = username
                    user.save()
                    student.username = username
                    student.save()
                    messages.info(request, 'Имя пользователя было изменено')
                    return redirect('/student/viewing_profile/')


def change_fullname(request):
    if request.user.is_authenticated:
        if request.user.last_name == 'student':
            if request.method == 'POST':
                fullname = request.POST.get('fullname')
                student = Student.objects.get(username=request.user.username)
                student.fullname= fullname
                student.save()
                user = User.objects.get(username=request.user.username)
                user.first_name = fullname
                user.save()
                messages.info(request, 'Полное имя было изменено')
                return redirect('/student/viewing_profile/')


def tests(request):
    if request.user.is_authenticated:
        if request.user.last_name == 'student':
            if request.method == 'POST':
                pass
            else:
                testings = Test.objects.filter(left=0)
                parsed_tests = list()
                now = datetime.datetime.now()
                student = Student.objects.get(username=request.user.username)
                grade = student.group.grade
                for test in testings:
                    try:
                        enrolled_testing = EnrolledTesting.objects.get(student_id=student.id, test_id=test.id)
                    except EnrolledTesting.DoesNotExist:
                        if test.end_date >= now.date():
                            parsed_tests.append(test)
                return render(request, 'student/tests.html', {'tests': parsed_tests, 'grade': grade,})


def results_tests(request):
    if request.user.is_authenticated:
        if request.user.last_name == 'student':
            student = Student.objects.get(username=request.user.username)
            if request.method == 'GET':
                enrolled_testings = EnrolledTesting.objects.filter(student_id=student.id, istaken=True)

                availableResults = list()
                now = datetime.datetime.now()
                for en in enrolled_testings:
                    if en.test.end_date <= now.date():
                        availableResults.append(en)

                answersOfTestings = list()
                for enrolledTest in availableResults:
                    answersOfTestings.append(enrolledTest.answer_set.all())
                return render(request, 'student/resultsOfTesting.html', {'enrolledTestings': availableResults, 'answersOfTestings': answersOfTestings})


def enroll_student(request, test_id):
    if request.user.is_authenticated:
        if request.user.last_name == 'student':
            if request.method == 'POST':
                pass
            else:
                utc = pytz.UTC
                test = Test.objects.get(id=test_id)
                teacher = Teacher.objects.get(id=test.teacher_id)
                teacher.tested_pupils += 1
                teacher.save()
                student = Student.objects.get(username=request.user.username)
                student.enrolledtesting_set.create(test_id=test_id, istaken=True, started=utc.localize(datetime.datetime.now()))
                return redirect('/student/%s/solving_test/' % test_id)

def solving_test(request, test_id):
    if request.user.is_authenticated:
        if request.user.last_name == 'student':
            if request.method == 'POST':
                pass
            elif request.method == 'GET':
                test = Test.objects.get(id=test_id)
                questions = test.question_set.all()
                paginator = Paginator(questions, 1)
                try:
                    page = int(request.GET.get('page', '1'))
                except:
                    page = 1
                try:
                    ques = paginator.page(page)
                except(EmptyPage, InvalidPage):
                    ques = paginator.page(paginator.num_pages)
                context = {
                    'questions': questions,
                    'ques': ques,
                    'test': test,
                }
                return render(request, 'student/solving_test.html',context)
    else:
        return redirect('/')


def resultWarning(request):
    if request.user.is_authenticated:
        if request.user.last_name == 'student':
            if request.method == 'GET':
                return render(request, 'student/resultWarning.html')


def get_timer(request, test_id):
    if request.user.is_authenticated:
        if request.user.last_name == 'student':
            if request.method == 'GET':
                student = Student.objects.get(username=request.user.username)
                enrolled_testing = EnrolledTesting.objects.get(test_id=test_id, student_id=student.id)
                test = Test.objects.get(id=test_id)
                
                now = datetime.datetime.now()
                now_compare= now.strftime('%Y%H%M%S')

                test_started = enrolled_testing.started
                test_duration = test.duration
                test_started_compare = test_started.strftime('%Y%H%M%S')
                if int(now_compare) >= (int(test_started_compare) + int(test_duration) * 60):
                    return JsonResponse({'isfinished': True})
                else:
                    return JsonResponse({'isfinished': False,'time': ((int(test_started_compare) + int(test_duration) * 60) - int(now_compare))})

def save_answer(request, test_id, question_id):
    if request.user.is_authenticated:
        if request.user.last_name == 'student':
            if request.method == 'POST':
                question = Question.objects.get(id=question_id)
                correctOption = Option.objects.get(question_id=question.id, option_number=question.answer)
                try:
                    answer = request.POST['answer']
                    student = Student.objects.get(username=request.user.username)
                    chosenOption = Option.objects.get(question_id=question.id, option_number=answer)
                    enrolled_testing = EnrolledTesting.objects.get(student_id=student.id, test_id=test_id)
                    answerModal = enrolled_testing.answer_set.create(question_text=question.question_text, answer=chosenOption.option_text, correctAnswer=correctOption)
                    if int(answer) == int(question.answer):
                        enrolled_testing.result += 1
                        enrolled_testing.save()
                    return JsonResponse({'chosen': True})
                except:
                    answerModal = enrolled_testing.answer_set.create(question_text=question.question_text, answer='', correctAnswer=correctOption)
                    return JsonResponse({'chosen': False})


def submit_homework(request, hw_id):
    if request.user.is_authenticated:
        if request.user.last_name == 'student':
            if request.method == 'GET':
                student = Student.objects.get(username=request.user.username)
                done_hw = DoneHomework.objects.get(student_id=student.id, homework_id=hw_id)
                teacher = Teacher.objects.get(id=done_hw.homework.teacher.id)
                teacher.sentHomeworks += 1
                teacher.save()
                done_hw.done = True
                done_hw.save()
                return JsonResponse({'isdone': True})


def instantiate_student_homework(request, hw_id):
    if request.user.is_authenticated:
        if request.user.last_name == 'student':
            if request.method == 'GET':
                student = Student.objects.get(username=request.user.username)
                homework = Homework.objects.get(id=hw_id)
                checkDoneHomework = DoneHomework.objects.filter(homework_id=hw_id, student_id=student.id)
                if len(checkDoneHomework) == 0:
                    student.donehomework_set.create(homework_id=hw_id, subject=homework.subject)
                    return JsonResponse({'isInstantiated': True})
                else:
                    return redirect('/')

# IMAGE COMPRESSION
def compress(image):
        im = Image.open(image)
        # create a BytesIO object
        im_io = BytesIO() 
        # save image to BytesIO object
        #im = im.resize([500,500])
        im = im.convert("RGB")
        im = im.save(im_io,'JPEG', quality=50) 
        # create a django-friendly Files object
        new_image = File(im_io, name=image.name)
        return new_image

def upload(request, hw_id):
    if request.user.is_authenticated:
        if request.user.last_name == 'student':
            if request.method == 'POST':
                photo = request.FILES['file']
                ext = photo.name.split('.')[-1]
                filename = '%s.%s' % (uuid.uuid4(), ext)
                photo.name = filename
                photo = compress(photo)

                student = Student.objects.get(username=request.user.username)
                done_homework = DoneHomework.objects.get(homework_id=hw_id, student_id=student.id)
                imagehw = done_homework.imageshomework_set.create(photo=photo, name=filename)
                return JsonResponse({'photoName': filename})

def delete_upload(request, file_name):
    if request.user.is_authenticated:
        if request.user.last_name == 'student':
            if request.method == 'GET':
                photo = ImagesHomework.objects.filter(name=file_name)
                photo.delete()
                return redirect('/')

def checked_homeworks(request):
    if request.user.is_authenticated:
        if request.user.last_name == 'student':
            student = Student.objects.get(username=request.user.username)
            if request.method == 'POST':
                pass
            else:
                checkedHomeworks = DoneHomework.objects.filter(student_id=student.id, done=True, checked=True)
                now = datetime.datetime.now()
                filtered_checkedHomeworks = list()
                for ch in checkedHomeworks:
                    if ch.checkedDate == now.date():
                        filtered_checkedHomeworks.append(ch)
                return render(request, 'student/checkedHomeworks.html', {'checkedHomeworks': filtered_checkedHomeworks})