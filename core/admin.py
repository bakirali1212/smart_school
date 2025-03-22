from django.contrib import admin
from .models import User, Student, Grade, Homework, BonusPoint

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'role', 'sinf')
    list_filter = ('role', 'sinf')
    search_fields = ('username', 'first_name', 'last_name')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'bonus_ball')

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('student', 'fan', 'baho', 'sana', 'teacher')
    list_filter = ('fan', 'sana')

@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ('sinf', 'fan', 'muddati')

@admin.register(BonusPoint)
class BonusPointAdmin(admin.ModelAdmin):
    list_display = ('student', 'ball_miqdori', 'sabab', 'sana')
