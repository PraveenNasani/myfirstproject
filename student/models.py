from django.db import models

# Create your models here.
class StudentData(models.Model):
    fname=models.CharField(max_length=200)
    lname=models.CharField(max_length=200)
    rollno=models.IntegerField(primary_key=True)
    grade=models.IntegerField()

    def __str__(self):
        return self.fname