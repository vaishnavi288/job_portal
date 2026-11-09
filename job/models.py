from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class job(models.Model):
    job_title=models.CharField(max_length=50)
    company_name=models.CharField(max_length=50)
    job_description=models.TextField()
    location=models.CharField(max_length=30)
    salary=models.DecimalField(max_digits=10,decimal_places=2)
    job_type=models.CharField(max_length=40)
    posted_by=models.ForeignKey(User,on_delete=models.CASCADE)