from django.contrib import admin
from .models import Instructor, Student, Course, Enrollment, Grade, User, SchoolYear, Semester

admin.site.register(Instructor)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(Grade)
admin.site.register(User)
admin.site.register(SchoolYear)
admin.site.register(Semester)
# Register your models here.
