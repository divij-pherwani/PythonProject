from django.contrib import admin
from .models import StudentDetail, UniversityDetail, CourseDetail, CourseName, ApplicationDetail

admin.site.register(StudentDetail)
admin.site.register(UniversityDetail)
admin.site.register(CourseDetail)
admin.site.register(CourseName)
admin.site.register(ApplicationDetail)


# Register your models here.
