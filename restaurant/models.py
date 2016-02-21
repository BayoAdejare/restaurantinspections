from django.db import models

# Create your models here.



class Universe(models.Model):
    camis = models.IntegerField(db_column='CAMIS', primary_key=True)
    dba = models.CharField(max_length=200)
    boro = models.CharField(max_length=500)
    building = models.IntegerField
    street = models.CharField(max_length=500)
    zipcode = models.IntegerField
    cuisine_description = models.CharField(max_length=200)
    inspection_date = models.DateField()
    action = models.CharField(max_length=500)
    violation_cd = models.CharField(max_length=10)
    violation_desc = models.TextField()
    critical_flag = models.CharField(max_length=25)
    grade = models.CharField(max_length=2)
    grade_date = models.DateField()






