# Generated by Django 3.1.5 on 2021-01-17 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0007_delete_applicationdetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_status', models.BooleanField()),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebApp.coursename')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebApp.studentdetail')),
                ('uni_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebApp.universitydetail')),
            ],
        ),
    ]