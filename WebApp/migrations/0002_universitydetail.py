# Generated by Django 3.1.5 on 2021-01-12 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UniversityDetail',
            fields=[
                ('uni_id', models.IntegerField(primary_key=True, serialize=False)),
                ('uni_name', models.CharField(max_length=250)),
                ('uni_city', models.CharField(max_length=100)),
                ('uni_type', models.CharField(max_length=100)),
                ('uni_rank', models.IntegerField()),
                ('uni_studentNumber', models.IntegerField()),
                ('uni_intStudents', models.IntegerField()),
            ],
        ),
    ]