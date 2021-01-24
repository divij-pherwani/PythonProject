from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import StudentRegistrationForm, LoginRegistrationForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from .models import CourseName, CourseDetail, UniversityDetail, StudentDetail, ApplicationDetail
from .filters import UniversityFilter
from django.contrib import messages
from django.db import connection


def index_view(request):
    return render(request, 'Index.html')


@login_required(login_url='login')
def staff_view(request):
    query = ApplicationDetail.objects.raw('SELECT A.id, D.course_name, B.uni_name, C.user_id, C.student_name  FROM WebApp_applicationdetail A JOIN WebApp_universitydetail B ON A.uni_id_id = B.uni_id JOIN WebApp_studentdetail C ON A.student_id_id = C.user_id JOIN WebApp_coursename D ON D.course_id = A.course_id_id WHERE A.uni_id_id = 111;')
    return render(request, 'Staff.html', {'query':query} )


@login_required(login_url='login')
def university_view(request, pk):
    query = CourseDetail.objects.raw(
        'SELECT A.[detail_id_id], B.[course_id], B.[course_name], B.[uni_id_id], A.[course_duration],A.[course_type], A.[course_tuition], C.[uni_name] FROM WebApp_coursename B JOIN WebApp_coursedetail A ON A.detail_id_id = B.course_id JOIN WebApp_universitydetail C ON C.uni_id = B.uni_id_id WHERE uni_id = %s',
        [pk])
    return render(request, 'University.html', {'query': query})


@login_required(login_url='login')
def about_view(request):
    return render(request, 'About.html')


@login_required(login_url='login')
def contact_view(request):
    return render(request, 'Contact.html')


def SignUpView(request):
    if request.method == "POST":
        user_form = LoginRegistrationForm(request.POST)
        profile_form = StudentRegistrationForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('index')
        else:
            print(user_form.errors, profile_form.errors)
    else:
        profile_form = StudentRegistrationForm(request.POST)
        user_form = LoginRegistrationForm(request.POST)

    return render(request, 'registration/SignUp.html', {'user_form': user_form, 'profile_form': profile_form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                if user.is_staff:
                    login(request,user)
                    return redirect('staff')

                else:
                    login(request, user)
                    return redirect('home')

            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Invalid attempt username: {} and password: {}".format(username, password))
            return HttpResponse("Incorrect Login and Password")

    else:
        return render(request, 'registration/Login.html', {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required(login_url='login')
def home_view(request):
    query = UniversityDetail.objects.all().order_by('uni_rank')
    myFilter = UniversityFilter(request.GET, queryset=query)
    query = myFilter.qs
    return render(request, 'Home.html', {'query': query, 'myFilter': myFilter})


@login_required(login_url='login')
def dashboard_view(request):
    query1 = CourseDetail.objects.raw(
        'SELECT A.[detail_id_id], C.[uni_name], B.[course_name],  A.[course_tuition] FROM WebApp_coursename B JOIN WebApp_coursedetail A ON A.detail_id_id = B.course_id JOIN WebApp_universitydetail C ON C.uni_id = B.uni_id_id ORDER BY A.[course_tuition] ASC LIMIT 5')

    query2 = CourseDetail.objects.raw(
        'SELECT A.[detail_id_id], C.[uni_name], B.[course_name],  A.[course_tuition] FROM WebApp_coursename B JOIN WebApp_coursedetail A ON A.detail_id_id = B.course_id JOIN WebApp_universitydetail C ON C.uni_id = B.uni_id_id ORDER BY A.[course_tuition] DESC LIMIT 5')

    query3 = UniversityDetail.objects.raw(
        'SELECT * FROM WebApp_universitydetail ORDER BY uni_studentNumber DESC LIMIT 5')

    query4 = UniversityDetail.objects.raw('SELECT * FROM WebApp_universitydetail ORDER BY uni_intStudents DESC LIMIT 5')
    return render(request, 'Dashboard.html', {'query1': query1, 'query2': query2, 'query3': query3, 'query4': query4})


@login_required(login_url='login')
def profile_view(request):
    current_user = request.user
    key = current_user.id
    query = StudentDetail.objects.raw('Select * FROM WebApp_studentdetail WHERE user_id == %s', [key])
    query2 = ApplicationDetail.objects.raw('Select * FROM WebApp_applicationdetail WHERE student_id_id == %s', [key])
    return render(request, 'Profile.html', {'query': query, 'query2': query2})


def delete(request, pk):
    item = ApplicationDetail.objects.get(pk=pk)
    item.delete()
    messages.success(request, 'Item from Wishlist has been deleted')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    #return redirect('profile')


def add(request, pk):
    current_user = request.user
    key = current_user.id
    cursor = connection.cursor()
    query = CourseName.objects.all().filter(course_id=pk)
    for r in query:
        university_id = r.uni_id_id
    item = ApplicationDetail.objects.raw(
        'SELECT * FROM WebApp_applicationdetail WHERE course_id_id = %s AND student_id_id = %s AND uni_id_id = %s ',
        [pk, key, university_id])
    counter = 0
    for i in item:
        counter = counter + 1
    if counter == 0:
        cursor.execute(
            "INSERT INTO WebApp_applicationdetail (app_status, course_id_id, student_id_id, uni_id_id) VALUES (%s, %s, %s, %s)",
            [True, pk, key, university_id])
        messages.success(request, 'Item added to Wishlist')
    else:
        messages.success(request, 'Item Exists in Wishlist')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='login')
def universityE_view(request):
    query = CourseDetail.objects.raw(
        'SELECT A.[detail_id_id], B.[course_id], B.[course_name], B.[uni_id_id], A.[course_duration],A.[course_type], A.[course_tuition], C.[uni_name] FROM WebApp_coursename B JOIN WebApp_coursedetail A ON A.detail_id_id = B.course_id JOIN WebApp_universitydetail C ON C.uni_id = B.uni_id_id')
    return render(request, 'University.html', {'query': query})

# Create your views here.
