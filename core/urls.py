from django.urls import path
from .views import RegisterView,  LoginView, UserListView, StudentListView, GradeListCreateView, HomeworkListCreateView, BonusPointListCreateView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('students/', StudentListView.as_view(), name='student-list'),
    path('grades/', GradeListCreateView.as_view(), name='grade-list'),
    path('homeworks/', HomeworkListCreateView.as_view(), name='homework-list'),
    path('bonus/', BonusPointListCreateView.as_view(), name='bonus-list'),
]
