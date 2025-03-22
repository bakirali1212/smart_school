from django.db import models
from django.contrib.auth.models import AbstractUser

ROLE_CHOICES = (
    ('admin', 'Admin'),
    ('teacher', 'Teacher'),
    ('student', 'Student'),
)

class User(AbstractUser):
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    sinf = models.CharField(max_length=10, blank=True, null=True)  # Student uchun

    def __str__(self):
        return f"{self.username} - {self.role}"

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bonus_ball = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    fan = models.CharField(max_length=50)
    baho = models.IntegerField()
    sana = models.DateField()
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student} - {self.fan}: {self.baho}"

class Homework(models.Model):
    sinf = models.CharField(max_length=10)
    fan = models.CharField(max_length=50)
    vazifa_matni = models.TextField()
    muddati = models.DateField()
    yuklangan_fayl = models.FileField(upload_to='homeworks/', null=True, blank=True)

    def __str__(self):
        return f"{self.fan} - {self.sinf}"

class BonusPoint(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    ball_miqdori = models.IntegerField()
    sabab = models.CharField(max_length=255)
    sana = models.DateField()

    def __str__(self):
        return f"{self.student} - {self.ball_miqdori} ball"
