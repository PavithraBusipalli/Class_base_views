from django.db import models

# Create your models here.


class School(models.Model):
    sclname = models.CharField(max_length = 20)
    sclprince = models.CharField(max_length = 20)
    sclloc = models.CharField(max_length = 20)

    def __str__(self):
        return self.sclname
    
class Student(models.Model):
    sclname = models.ForeignKey(School,on_delete = models.CASCADE)
    stdname = models.CharField(max_length = 20)
    stdage = models.IntegerField()



