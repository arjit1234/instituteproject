from django.db import models

# Create your models here.

class CourseData(models.Model):
    course_name=models.CharField(max_length=100)
    duration=models.CharField(max_length=50)
    start_date=models.DateField(max_length=100)
    trainer_name=models.CharField(max_length=100)
    trainer_exp=models.IntegerField()

    content=models.FileField(upload_to='files')