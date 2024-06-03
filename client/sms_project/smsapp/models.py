from django.db import models
from django.contrib.auth.models import User

class StudentModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rno = models.IntegerField()
    name = models.CharField(max_length=40)
    mobile = models.BigIntegerField(default=1000000000)
    email = models.EmailField(default='')
    marks1 = models.IntegerField(default=0)
    marks2 = models.IntegerField(default=0)
    marks3 = models.IntegerField(default=0)
    marks4 = models.IntegerField(default=0)
    marks5 = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
