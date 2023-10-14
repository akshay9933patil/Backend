from rest_framework import views, viewsets
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializer import StudentSerializer, SubjectSerializer
from .models import *


class ExampleView(views.APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def get(self,request):
        return Response(data={'details':'ExampleView'})


class StudentView(viewsets.ModelViewSet):
    """CRUD For Students"""
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


class SubjectsView(viewsets.ModelViewSet):
    """CRUD for subjects"""
    serializer_class = SubjectSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    queryset = Subject.objects.all()


class SubjectsView(viewsets.ModelViewSet):
    """CRUD for subjects"""
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()

