from django.contrib import admin
from .models import Instructor, Student, Course, Enrollment, User, SchoolYear, Semester, Class

admin.site.register(Instructor)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(User)
admin.site.register(SchoolYear)
admin.site.register(Semester)
admin.site.register(Class)
# Register your models here.
