from django.urls import path
from api import views

urlpatterns = [
    path('', views.home),
    path('students/', views.StudentListSerializer.as_view()),
    path('students/<int:pk>', views.StudentDetailedView.as_view()),
    path('deletestudent/<int:pk>', views.StudentDestroyView.as_view()),
]
