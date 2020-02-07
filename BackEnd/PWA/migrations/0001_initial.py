# Generated by Django 3.0.2 on 2020-02-06 22:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='JoinReqeust',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requset_date', models.DateField()),
                ('request_datej', django_jalali.db.models.jDateField()),
                ('request_state', models.CharField(max_length=15)),
                ('national_code', models.CharField(max_length=10)),
                ('birthday', django_jalali.db.models.jDateField()),
                ('full_name', models.CharField(max_length=50)),
                ('phone_number', phone_field.models.PhoneField(blank=True, help_text='this is mobile number', max_length=31)),
                ('mobile_number', phone_field.models.PhoneField(blank=True, help_text='this is mobile number', max_length=31)),
                ('job_title', models.CharField(max_length=30, null=True)),
                ('home_address', models.TextField(max_length=160, null=True)),
                ('work_address', models.TextField(max_length=160, null=True)),
                ('father_name', models.CharField(max_length=30)),
                ('education', models.CharField(default='bi savad', max_length=30, null=True)),
                ('sick_type1', models.BooleanField(default=False, help_text='بیماری قلبی')),
                ('sick_type2', models.BooleanField(default=False, help_text='کم خونی-ناراحتی خونی')),
                ('sick_type3', models.BooleanField(default=False, help_text='صرع-تشنج')),
                ('sick_type4', models.BooleanField(default=False, help_text='دیابت')),
                ('sick_type5', models.BooleanField(default=False, help_text='ناراحتی تیرویید')),
                ('sick_type6', models.BooleanField(default=False, help_text='هپاتیت-یرقان')),
                ('sick_type7', models.BooleanField(default=False, help_text='فشار خون-تپش قلب')),
                ('sick_type8', models.BooleanField(default=False, help_text='اسم پ بیماری تنفسی')),
                ('sick_type9', models.BooleanField(default=False, help_text='بارداری-مشکوک به بارداری')),
                ('sick_type10', models.BooleanField(default=False, help_text='ایدز')),
                ('sick_type11', models.BooleanField(default=False, help_text='بیماری کلیوی')),
                ('specific_drug', models.CharField(help_text='در صورت مصرف داروی خاص بیان گردد.', max_length=40, null=True)),
                ('surgical_history', models.CharField(help_text='در صورت داشتن سابقه جراحی بیان گردد.', max_length=40, null=True)),
                ('hospitalization', models.CharField(help_text='در صورت داشتن سابه بستم ', max_length=50, null=True)),
                ('medical_allergy', models.CharField(help_text='در صورت داشتن حساسیت دارویی ذکر گردد', max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('national_code', models.CharField(max_length=10)),
                ('verify_state', models.BooleanField(default=False)),
                ('token', models.CharField(max_length=48)),
                ('user_role', models.CharField(max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PatientProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('phone_number', phone_field.models.PhoneField(blank=True, help_text='this is mobile number', max_length=31)),
                ('mobile_number', phone_field.models.PhoneField(blank=True, help_text='this is mobile number', max_length=31)),
                ('job_title', models.CharField(max_length=30, null=True)),
                ('home_address', models.TextField(max_length=160, null=True)),
                ('work_address', models.TextField(max_length=160, null=True)),
                ('father_name', models.CharField(max_length=30)),
                ('education', models.CharField(max_length=30)),
                ('national_code', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='PWA.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='PatientFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('presence_date', models.DateField()),
                ('presence_datej', django_jalali.db.models.jDateField()),
                ('description', models.TextField()),
                ('treatment_cost', models.BigIntegerField(default=0)),
                ('payment', models.BigIntegerField(default=0)),
                ('unpaid_fee', models.BigIntegerField(default=0)),
                ('doctor', models.CharField(max_length=30)),
                ('national_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PWA.UserProfile')),
            ],
        ),
    ]
