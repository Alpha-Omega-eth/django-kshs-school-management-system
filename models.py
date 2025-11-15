from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=20, unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    parent_phone = models.CharField(max_length=15)
    address = models.TextField()
    enrollment_date = models.DateField(auto_now_add=True)
    face_encoding = models.BinaryField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} ({self.student_id})'
