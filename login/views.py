from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import check_password
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.urls import NoReverseMatch
from django.contrib import messages
from .models import Instructor, Course, Student, Grade, Enrollment, User
from .forms import RegistrationForm

def login_form(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.user_type == User.ADMIN:
                return redirect('admin_homepage')
            elif user.user_type == User.INSTRUCTOR:
                return redirect('instructor_dashboard')
            elif user.user_type == User.STUDENT:
                return redirect('student_dashboard')
            else:
                # Handle other user types if needed
                pass
        else:
            print("error1")
            return render(request, 'login_page/login_form.html', {'error': 'Invalid username or password'})
    else:
        print("error2")
        return render(request, 'login_page/login_form.html')

def logout_view(request):
    logout(request)
    return redirect('login_form') 

# Your other view functions remain unchanged


def admin_homepage(request):
    return render(request, 'login_page/admin_homepage.html')

def view_students(request):
    # Add logic to fetch student data from the database
    # and pass it to the template
    return render(request, 'login_page/view_students.html')

def view_courses(request):
    # Fetch all courses from the database
    courses = Course.objects.all()

    # Pass the courses to the template for rendering
    return render(request, 'login_page/view_courses.html', {'courses': courses})

def view_instructors(request):
    # Add logic to fetch instructor data from the database
    # and pass it to the template
    all_instructors = Instructor.objects.all
    return render(request, 'login_page/view_instructors.html', {'all':all_instructors})

def view_enrollments(request):
    # Add logic to fetch enrollment data from the database
    # and pass it to the template
    return render(request, 'login_page/view_enrollments.html')

def add_instructors(request):
    if request.method == 'POST':
        instructor_id = request.POST['instructor_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        
        # Check if an instructor with the same ID already exists
        if Instructor.objects.filter(instructor_id=instructor_id).exists():
            # If the instructor_id already exists, set error flag to True
            return render(request, 'login_page/add_instructors.html', {'error': True})
            
        # Create new Instructor object
        new_instructor = Instructor(
            instructor_id=instructor_id,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number
        )
        
        # Save the new instructor to the database
        new_instructor.save()
        
        # Redirect to the view_instructors page
        return redirect('view_instructors')
    else:
        return render(request, 'login_page/add_instructors.html', {'error': False})

def edit_instructor(request, instructor_id):
    # Get the instructor object from the database
    instructor = get_object_or_404(Instructor, instructor_id=instructor_id)

    if request.method == 'POST':
        # Retrieve the updated data from the form submission
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']

        # Update the instructor object with the new data
        instructor.first_name = first_name
        instructor.last_name = last_name
        instructor.email = email
        instructor.phone_number = phone_number

        # Save the updated instructor object
        instructor.save()

        # Redirect to the view instructors page
        return redirect('view_instructors')
    else:
        # Render the edit instructor form with the existing data
        return render(request, 'login_page/edit_instructor.html', {'instructor': instructor})

def delete_instructor(request, instructor_id):
    instructor = get_object_or_404(Instructor, instructor_id=instructor_id)
    if request.method == 'POST':
        instructor.delete()
        return redirect('view_instructors')
    return render(request, 'login_page/view_instructors.html', {'instructor': instructor})

def add_course(request):
    if request.method == 'POST':
        course_id = request.POST['course_id']
        course_name = request.POST['course_name']
        instructor_id = request.POST['instructor_id']
        credit_hours = request.POST['credit_hours']
        
        # Create new Course object
        new_course = Course(
            course_id=course_id,
            course_name=course_name,
            instructor_id=instructor_id,
            credit_hours=credit_hours
        )
        
        # Save the new course to the database
        new_course.save()
        
        # Redirect to view courses page
        return redirect('view_courses')
    else:
        return render(request, 'login_page/add_course.html')

def edit_course(request, course_id):
    course = get_object_or_404(Course, course_id=course_id)
    if request.method == 'POST':
        # Update the course object with the new data
        course.course_name = request.POST.get('course_name')
        # Assuming you're not updating the instructor_id
        # course.instructor_id = request.POST.get('instructor_id')
        course.credit_hours = request.POST.get('credit_hours')
        # Save the updated course object
        course.save()
        return redirect('view_courses')
    else:
        # Populate the form with the existing data
        context = {
            'course': course
        }
        return render(request, 'login_page/edit_course.html', context)

def view_class(request, course_id):
    enrollments = Enrollment.objects.filter(course_id=course_id)

    return render(request, 'login_page/view_class.html', {'enrollments': enrollments})

def delete_course(request, course_id):
    course = get_object_or_404(Course, course_id=course_id)
    course.delete()
    return redirect('view_courses')

def instructor_dashboard(request):
    instructor = request.user.instructor

    classes_taught = Enrollment.objects.filter(instructor=instructor)

    return render(request, 'login_page/instructor_dashboard.html', {'classes_taught': classes_taught})

def student_dashboard(request):
    # Assuming you have a logged-in user object available in the request
    # Retrieve the logged-in student based on the user object
    student = request.user.student
    
    # Fetch all enrollments for the logged-in student
    enrollments = Enrollment.objects.filter(student_id=student)
    
    # Create an empty list to store course information for the student
    courses_info = []
    
    # Iterate through the enrollments and retrieve course information
    for enrollment in enrollments:
        course = enrollment.course_id
        grade = Grade.objects.filter(enrollment=enrollment).first()
        courses_info.append({
            'course_name': course.course_name,
            'instructor': course.instructor,
            'credit_hours': course.credit_hours,
            'grade': grade.grade_value if grade else None  # Display grade if available
        })
    
    # Pass the courses information to the template for rendering
    return render(request, 'login_page/student_dashboard.html', {'courses_info': courses_info})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print("check 2")
            user = form.save(commit=False)
            user.user_type = 'admin'  # Set default user type
            user.save()
            return redirect('login_form')  # Redirect to login page after successful registration
        else:
            print(form.errors)
    else:
        form = RegistrationForm()
        print("check 3")
    return render(request, 'login_page/register.html', {'form': form})

# W7+1k9Gm1}2< password for ins123