from django.db import models


# Create your models here.
class Dummy(models.Model):
    number = models.IntegerField()
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    options1 = models.CharField(max_length=100)
    options2 = models.CharField(max_length=100)
    options3 = models.CharField(max_length=100)
    options4 = models.CharField(max_length=100)

class Student_data(models.Model):
    id = models.CharField(max_length=100,primary_key = True)
    Password = models.CharField(max_length=100)
    Time_take = models.IntegerField()
    score = models.IntegerField()

    def __str__(self):
        return self.id
