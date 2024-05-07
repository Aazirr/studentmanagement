from django.contrib import admin
from .models import Instructor, Student, Course, Enrollment, Grade

admin.site.register(Instructor)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(Grade)
# Register your models here.
