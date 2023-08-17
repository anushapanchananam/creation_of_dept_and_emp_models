from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class dept(models.Model):
    dname=models.CharField(max_length=100)
    dloc=models.CharField(max_length=100)
    dept_no = models.IntegerField(primary_key=True)
    def __str__(self):
        return self.dname 

class emp(models.Model):
    eno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    hiredate=models.DateField()
    sal=models.IntegerField()
    com=models.IntegerField(default=None,null=True)
    dept_no = models.ForeignKey(dept, on_delete=models.CASCADE)
    def __str__(self):
        return self.job 