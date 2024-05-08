from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ADMIN = 'admin'
    INSTRUCTOR = 'instructor'
    STUDENT = 'student'
    USER_TYPES = [
        (ADMIN, 'Admin'),
        (INSTRUCTOR, 'Instructor'),
        (STUDENT, 'Student'),
    ]
    
    user_type = models.CharField(max_length=20, choices=USER_TYPES, default='Admin')

    def __str__(self):
        return f"{self.username} ({self.user_type})"

class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    instructor_id = models.CharField(max_length=50, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.instructor_id

class Student(models.Model):
    student_id = models.CharField(max_length=50, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.student_id

class Course(models.Model):
    course_id = models.CharField(max_length=50, primary_key=True)
    course_name = models.CharField(max_length=100)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    credit_hours = models.IntegerField()

class Enrollment(models.Model):
    enrollment_id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, null=True)
    enrollment_date = models.DateField()


class Grade(models.Model):
    grade_id = models.AutoField(primary_key=True)
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    grade_value = models.CharField(max_length=50)