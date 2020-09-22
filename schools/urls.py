from django.urls import path
from . import views

urlpatterns = [
    path('', views.schoolMainPage, name='school_main_page'),
    path('school_registration/', views.school_registration, name='school_registration'),
    path('school_login/', views.school_login, name='school_login'),
    path('logout/', views.logout_school, name='logout_school'),
    path('teachers/', views.list_teachers, name='list_teachers'),
    path('students/', views.list_students, name='list_students'),
    path('<int:teacher_id>/deleting_teacher/', views.deleting_teacher, name='deleting_teacher'),
    path('<int:student_id>/deleting_student/', views.deleting_student, name='deleting_student'),
]
