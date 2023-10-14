from django.db import models


class Subject(models.Model):
    subject_name = models.CharField(max_length=30, unique=True)

    def __str__(self) -> str:
        return f"{self.id},{self.subject_name}"
    
    class Meta:
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'

class Student(models.Model):
    roll_number = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dob = models.DateField()
    address = models.TextField(max_length=250)

    def __str__(self) -> str:
        return f"{self.roll_number},{self.first_name},{self.last_name},{self.dob},{self.address},"

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

class Marks(models.Model):
    roll_number = models.ForeignKey(Student,on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    marks = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Mark'
        verbose_name_plural = 'Marks'



