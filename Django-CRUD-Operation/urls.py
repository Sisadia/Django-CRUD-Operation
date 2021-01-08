from django.contrib import admin
from django.urls import path
from student import views as student_view
from teacher import views as teacher_view
from courses import views as course_view

urlpatterns = [

    path('stud/',student_view.all_students),
    path('<str:studentaction>/<str:sid>', student_view.action_handler_for_student),
    path('teacher/',teacher_view.all_teacher),
    path('<str:action>/<str:tid>', teacher_view.action_handler_for_teacher),
    path('course/', course_view.all_courses),
    path('<str:courseaction>/<str:cid>', course_view.action_handler_for_course),
]
