from django.db import models

# Create your models here.
class Student(models.Model):
    GENDER = (
        ("F", "Female"),
        ("M", "Male"),
        ("U", "Undisclosed"),
    )
    name = models.CharField(max_length=100)
    roll_number = models.IntegerField(unique=True)
    email = models.EmailField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER)
    percentage = models.FloatField()
    institute = models.ForeignKey('Institute', on_delete=models.CASCADE, null = True, blank = True)
    
    def __str__(self):
        return self.name

class Institute(models.Model):
    TYPES = (
        ("C", "college"),
        ("H", "High School")
    )
    name = models.CharField(max_length=100)
    type_of_institute = models.CharField(max_length=1, choices=TYPES)

    def __str__(self):
        return self.name