from rest_framework.response import Response
from api import models, serializers
from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
    ListCreateAPIView
)

# Create your views here.
def home(request):
    return render(request, 'main/index.html')

# Retriving the data 
# class StudentListSerializer(ListAPIView):
#     queryset = models.Student.objects.all()
#     serializer_class = serializers.StudentSerializer
class StudentListSerializer(ListCreateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer

# class StudentDetailedView(RetrieveAPIView):
#     queryset = models.Student.objects.all()
#     serializer_class = serializers.StudentSerializer
class StudentDetailedView(RetrieveUpdateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer


class StudentDestroyView(DestroyAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer