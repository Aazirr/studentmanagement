from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_form, name='login_form'),
    path('admin_homepage/', views.admin_homepage, name='admin_homepage'),
    path('view/students/', views.view_students, name='view_students'),
    path('view/courses/', views.view_courses, name='view_courses'),
    path('view/instructors/', views.view_instructors, name='view_instructors'),
    path('view/enrollments/', views.view_enrollments, name='view_enrollments'),
    path('edit/instructor/<str:instructor_id>/', views.edit_instructor, name='edit_instructor'),
    path('view/instructors/delete/<str:instructor_id>/', views.delete_instructor, name='delete_instructor'),
    path('add/instructor/', views.add_instructors, name='add_instructor'),
    path('add/course/', views.add_course, name='add_course'),
    path('edit/course/<str:course_id>/', views.edit_course, name='edit_course'),
    path('delete/course/<str:course_id>/', views.delete_course, name='delete_course'),
    path('instructor_dashboard/', views.instructor_dashboard, name='instructor_dashboard'),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('register/', views.register, name='register'),
]
