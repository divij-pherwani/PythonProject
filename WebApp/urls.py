from django.urls import path
from WebApp import views
from django.conf.urls import url


urlpatterns = [

    path('signup/', views.SignUpView, name='SignUp'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name="logout"),
    path('home/', views.home_view, name='home'),
    path('university/all/', views.universityE_view, name='universityE'),
    path('university/<str:pk>/', views.university_view, name='university'),
    path('contact/', views.contact_view, name='contact'),
    path('about/', views.about_view, name='about'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('profile/', views.profile_view, name='profile'),
    path('', views.index_view, name='index'),
    path('delete/<pk>', views.delete, name='delete'),
    path('add/<pk>', views.add, name='add'),
    path('staff/', views.staff_view, name='staff')

]