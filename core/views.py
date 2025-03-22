from rest_framework import generics, permissions
from .models import User, Student, Grade, Homework, BonusPoint
from .serializers import UserSerializer, StudentSerializer, GradeSerializer, HomeworkSerializer, BonusPointSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

# Ro‘yxatdan o‘tish
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]   # Buni albatta qo'y!

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'message': 'Login muvaffaqiyatli'}, status=200)
        return Response({'error': 'Username yoki parol noto‘g‘ri'}, status=401)

# Foydalanuvchi ro‘yxati
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# O‘quvchilar ro‘yxati
class StudentListView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# Baholar CRUD
class GradeListCreateView(generics.ListCreateAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer

# Uy vazifalar CRUD
class HomeworkListCreateView(generics.ListCreateAPIView):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer

# Bonus ball CRUD
class BonusPointListCreateView(generics.ListCreateAPIView):
    queryset = BonusPoint.objects.all()
    serializer_class = BonusPointSerializer
