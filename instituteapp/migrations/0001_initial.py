# Generated by Django 2.2.10 on 2020-02-22 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=50)),
                ('start_date', models.DateField(max_length=100)),
                ('trainer_name', models.CharField(max_length=100)),
                ('trainer_exp', models.IntegerField()),
                ('content', models.FileField(upload_to='files')),
            ],
        ),
    ]
