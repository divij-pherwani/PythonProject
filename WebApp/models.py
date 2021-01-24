from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class StudentDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    student_name = models.CharField(max_length=50)
    student_dob = models.DateField()
    student_qualification = models.CharField(max_length=15)
    student_gender = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username


class UniversityDetail(models.Model):
    uni_id = models.IntegerField(primary_key=True)
    uni_name = models.CharField(max_length=250)
    uni_city = models.CharField(max_length=100)
    uni_type = models.CharField(max_length=100)
    uni_rank = models.IntegerField()
    uni_studentNumber = models.IntegerField()
    uni_intStudents = models.IntegerField()

    def __str__(self):
        return self.uni_name


class CourseName(models.Model):
    uni_id = models.ForeignKey(UniversityDetail, on_delete=models.CASCADE)
    course_id = models.IntegerField(primary_key=True)
    course_name = models.CharField(max_length=50)

    def __str__(self):
        return self.course_name


class CourseDetail(models.Model):
    detail_id = models.OneToOneField(CourseName, on_delete=models.CASCADE, primary_key=True)
    course_type = models.CharField(max_length=20)
    course_duration = models.FloatField()
    course_tuition = models.IntegerField()

    def __str__(self):
        return self.detail_id.course_name


class ApplicationDetail(models.Model):
    uni_id = models.ForeignKey(UniversityDetail, on_delete=models.CASCADE)
    student_id = models.ForeignKey(StudentDetail, on_delete=models.CASCADE)
    course_id = models.ForeignKey(CourseName, on_delete=models.CASCADE)
    app_status = models.BooleanField()

# Create your models here.
