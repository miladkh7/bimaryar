from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField # a third party library to manage phone numbesrs
from django.core.validators import MinLengthValidator
from django_jalali.db import models as jmodels
# Create your models here.
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    national_code=models.CharField(max_length=10)#,min_length=10, validators=[MinLengthValidator(4)])
    # user_id=models.CharField(max_length=16,blank=False)
    verify_state=models.BooleanField(default=False)
    token=models.CharField(max_length=48,null=False)
    user_role=models.CharField(max_length=10)
    def __str__(self):
        return "{}-{}".format(self.national_code,self.verify_state)

class PatientFile(models.Model):
    national_code=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    presence_date=models.DateField()
    presence_datej=jmodels.jDateField()
    description=models.TextField()
    treatment_cost=models.BigIntegerField(default=0)
    payment=models.BigIntegerField(default=0)
    unpaid_fee=models.BigIntegerField(default=0)
    doctor=models.CharField(max_length=30)

    def __str__(self):
        return "{}-{}".format(self.national_code,self.description)
class PatientProfile(models.Model):
    national_code=models.OneToOneField(UserProfile,on_delete=models.CASCADE)
    full_name=models.CharField(max_length=50)
    # last_name=models.CharField(max_length=30)
    phone_number=PhoneField(blank=True,help_text='this is mobile number')
    mobile_number=PhoneField(blank=True,help_text='this is mobile number')
    job_title=models.CharField(max_length=30,null=True)
    home_address=models.TextField(max_length=160,null=True)
    work_address=models.TextField(max_length=160,null=True)
    father_name=models.CharField(max_length=30)
    education=models.CharField(max_length=30)
    def __str__(self):
        return "{}".format(self.full_name)

# this model use as temp register
class TempRegister(models.Model):
    requset_date=models.DateField()
    request_datej=jmodels.jDateField()
    request_state=models.CharField(max_length=15)
    national_code=models.CharField(max_length=10)
    birthday=jmodels.jDateField()
    full_name=models.CharField(max_length=50)
    # last_name=models.CharField(max_length=30)
    phone_number=PhoneField(blank=True,help_text='this is mobile number')
    mobile_number=PhoneField(blank=True,help_text='this is mobile number')
    job_title=models.CharField(max_length=30,null=True)
    home_address=models.TextField(max_length=160,null=True)
    work_address=models.TextField(max_length=160,null=True)
    father_name=models.CharField(max_length=30)
    education=models.CharField(max_length=30,null=True,default='bi savad')
    sick_type1=models.BooleanField(default=False,help_text="بیماری قلبی")
    sick_type2=models.BooleanField(default=False,help_text="کم خونی-ناراحتی خونی")
    sick_type3=models.BooleanField(default=False,help_text="صرع-تشنج")
    sick_type4=models.BooleanField(default=False,help_text="دیابت")
    sick_type5=models.BooleanField(default=False,help_text="ناراحتی تیرویید")
    sick_type6=models.BooleanField(default=False,help_text="هپاتیت-یرقان")
    sick_type7=models.BooleanField(default=False,help_text="فشار خون-تپش قلب")
    sick_type8=models.BooleanField(default=False,help_text="اسم پ بیماری تنفسی")
    sick_type9=models.BooleanField(default=False,help_text="بارداری-مشکوک به بارداری")
    sick_type10=models.BooleanField(default=False,help_text="ایدز")
    sick_type11=models.BooleanField(default=False,help_text="بیماری کلیوی")
    specific_drug=models.CharField(max_length=40,null=True,help_text="در صورت مصرف داروی خاص بیان گردد.")
    surgical_history=models.CharField(max_length=40,null=True,help_text="در صورت داشتن سابقه جراحی بیان گردد.")
    hospitalization=models.CharField(max_length=50,null=True,help_text="در صورت داشتن سابه بستم ")
    medical_allergy=models.CharField(max_length=50,null=True,help_text="در صورت داشتن حساسیت دارویی ذکر گردد")
    
    def __str__(self):
        return "{} {}".format(self.national_code,self.full_name)

# class Disease‌‌‌‌Background(models.Model):
#     national_code=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
