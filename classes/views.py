from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import Class, Subject
from .serializers import ClassSerializer, SubjectSerializer


class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer