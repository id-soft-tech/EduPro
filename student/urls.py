from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_main_page, name='student_main_page'),
    path('student_registration/', views.student_registration, name='student_registration'),
    path('student_login/', views.student_login, name='student_login'),
    path('logout/', views.student_logout, name='student_logout'),
    path('viewing_profile/', views.viewing_profile, name='viewing_profile'),
    path('<int:test_id>/get_timer/', views.get_timer, name='get_timer'),
    path('change_fullname/', views.change_fullname, name='change_fullname'),
    path('change_username/', views.change_username, name='change_username'),
    path('change_password/', views.change_password, name='change_password'),
    path('tests/', views.tests, name='tests'),
    path('results_tests/', views.results_tests, name='results_tests'),
    path('<int:test_id>/solving_test/', views.solving_test, name='solving_test'),
    path('<int:test_id>/0/solving_test/', views.enroll_student, name='solving_test'),
    path('<int:test_id>/<int:question_id>/save_answer/', views.save_answer, name='save_answer'),
    path('<int:hw_id>/upload/', views.upload, name='upload'),
    path('<str:file_name>/delete_upload/', views.delete_upload, name='delete_upload'),
    path('<int:hw_id>/submit_homework/', views.submit_homework, name='submit_homework'),
    path('<int:hw_id>/instantiate_student_homework/', views.instantiate_student_homework, name='instantiate_student_homework'),
    path('checked_homeworks/', views.checked_homeworks, name='checked_homeworks')
]
