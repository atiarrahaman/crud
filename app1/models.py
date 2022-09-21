from django.db import models

# Create your models here.


class Student(models.Model):
    name= models.CharField(max_length=50)
    email= models.EmailField(max_length=254)
    roll= models.IntegerField()
    address= models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
    
# class Blood(models.Model):
#     name= models.CharField(max_length=50)
#     phone= models.CharField(max_length=50)
#     email= models.CharField(max_length=50)
#     reson= models.CharField(max_length=50)
    