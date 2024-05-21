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

class SchoolYear(models.Model):
    year = models.CharField(max_length=9)  # Example: "2024-2025"

    def __str__(self):
        return self.year


class Semester(models.Model):
    name = models.CharField(max_length=20)  # Example: "1st Semester", "2nd Semester", "Summer Term"

    def __str__(self):
        return self.name

class Course(models.Model):
    course_id = models.CharField(max_length=50, primary_key=True)
    course_name = models.CharField(max_length=100)
    credit_hours = models.IntegerField()

    def __str__(self):
        return self.course_name


class Class(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    school_year = models.ForeignKey(SchoolYear, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['course', 'instructor', 'school_year', 'semester']

    def __str__(self):
        return f"{self.course.course_name} - {self.instructor.user.username}"

class Enrollment(models.Model):
    enrollment_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    enrolled_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    enrollment_date = models.DateField()
    midterm_grade = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    final_grade = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    class Meta:
        unique_together = ['student', 'enrolled_class']

    def __str__(self):
        return f"{self.student.first_name} - {self.enrolled_class.course.course_name}"



