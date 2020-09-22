from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.indexPage, name='index_page'),
    path('teacher/', include('teacher.urls')),
    path('student/', include('student.urls')),
    path('login_user/', views.login_user, name='login'),
    path('about/', views.about, name='about'),
    path('list_teachers/', views.list_teachers, name='list_teachers'),
    path('list_students/', views.list_students, name='list_students'),
    path('tested_pupils/', views.tested_pupils, name='tested_pupils'),
    path('homework/', views.list_homework, name='homework'),
    # path('student_achievement/', views.student_achievement, name='student_achievement'),
]
