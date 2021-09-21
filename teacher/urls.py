from django.urls import path
from teacher import views
from django.contrib.auth.views import LoginView
from teacher.urls import *
from teacher.views import *

urlpatterns = [
path('teacherclick', views.teacherclick_view),
path('teachersignup', views.teacher_signup_view,name='teachersignup'),
path('teacherlogin', views.teacher_login_attempt,name='teacherlogin'),
path('teacher-dashboard', views.teacher_dashboard_view,name='teacher-dashboard'),
path('teacher-exam', views.teacher_exam_view,name='teacher-exam'),
path('teacher-add-exam', views.teacher_add_exam_view,name='teacher-add-exam'),
path('teacher-view-exam', views.teacher_view_exam_view,name='teacher-view-exam'),
path('delete-exam/<int:pk>', views.delete_exam_view,name='delete-exam'),


path('teacher-question', views.teacher_question_view,name='teacher-question'),
path('teacher-add-question', views.teacher_add_question_view,name='teacher-add-question'),
path('teacher-view-question', views.teacher_view_question_view,name='teacher-view-question'),
path('teacher-view-student-marks', views.teacher_view_student_marks_view,name='teacher-view-student-marks'),
path('teacher-view-marks/<int:pk>', views.teacher_view_marks_view,name='teacher-view-marks'),
path('teacher-check-marks/<int:pk>', views.teacher_check_marks_view,name='teacher-check-marks'),
path('see-question/<int:pk>', views.see_question_view,name='see-question'),
path('remove-question/<int:pk>', views.remove_question_view,name='remove-question'),
]