from django.urls import path
from . import views

urlpatterns = [
    path('', views.teacher_main_page, name='teacher_main_page'),
    path('teacher_registration/', views.teacher_registration, name='teacher_registration'),
    path('teacher_login/', views.teacher_login, name='teacher_login'),
    path('logout/', views.teacher_logout, name='teacher_logout'),
    path('viewing_profile/', views.viewing_profile, name='viewing_profile'),
    path('change_fullname/', views.change_fullname, name='change_fullname'),
    path('change_username/', views.change_username, name='change_username'),
    path('change_password/', views.change_password, name='change_password'),
    path('creating_test/', views.creating_test, name='creating_test'),
    path('homework/', views.homework, name='homework'),
    path('<int:test_id>/adding_questions/', views.adding_questions, name='adding_questions'),
    path('<int:test_id>/viewing_questions/', views.viewing_questions, name='viewing_questions'),
    path('<int:test_id>/<int:question_id>/changing_question/', views.changing_question, name='changing_question'),
    path('<int:test_id>/deleting_test/', views.deleting_test, name='deleting_test'),
    path('<int:test_id>/results/', views.results, name='results'),
    path('<int:hw_id>/viewing_homework/', views.viewing_homework, name='viewing_homework'),
    path('<int:hw_id>/deleting_homework/', views.deleting_homework, name='deleting_homework'),
    path('<int:done_hw_id>/<int:student_id>/student_homework/', views.student_homework, name='student_homework'),
]