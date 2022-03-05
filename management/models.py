from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=20)
    student_roll =models.IntegerField(null=False)
    
    def __str__(self):
        return self.Name+'-'+str(self.student_id)



class Student_detail(models.Model):
    Student_id = models.AutoField(primary_key=True)
    marks = models.IntegerField(default = 0, null = False)
    Parent_name=models.CharField(max_length=50)
    Address = models.CharField(max_length=100)

    def __str__(self):
        return str(self.Student_id)

        