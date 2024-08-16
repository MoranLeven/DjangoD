from django.db import models

# Create your models here.
class msgboard(models.Model):
    userId=models.IntegerField(primary_key=True)
    profilePic=models.TextField()
    permissionLevel=models.CharField(max_length=100, choices=[
        ('admin', 'Admin'),
        ('normal_user', 'Normal User'),
        ('viewer', 'Viewer')
    ])
    age=models.IntegerField()
    gender=models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    mail=models.EmailField(unique=True)
    height=models.DecimalField(max_digits=5,decimal_places=2)
    weight=models.DecimalField(max_digits=5,decimal_places=2)
    bloodgroup=models.CharField(max_length=3,choices=[('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'),
        ('O+', 'O+'), ('O-', 'O-')])
    password=models.TextField(max_length=100)
    username=models.CharField(max_length=200)
    nickname=models.CharField(max_length=200)
    def __str__(self):
        return self.username



