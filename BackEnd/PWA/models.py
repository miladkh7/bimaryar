from django.db import models

# Create your models here.
class User(models.Model):
    user_id=models.CharField(max_length=16,blank=False)
    verify_state=models.BooleanField(default=False)
    token=models.CharField(max_length=48,null=False)
    password_hash=models.CharField(max_length=64)
    user_role=models.CharField(max_length=10)
    def __str__(self):
        return "{}-{}".format(self.user_id,self.verify_state)

class PatientFile(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    phone_number=models.CharField(max_length=10)