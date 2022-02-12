from operator import mod
from pyexpat import model
from turtle import ondrag
from unicodedata import name
from django.db import models

# Create your models here.

class Personal(models.Model):
    p_full_name=models.CharField(max_length=250)
    p_moblie_number=models.CharField(max_length=250)
    p_cnic=models.CharField(max_length=15)
    created_on=models.DateField(auto_now=True)
    deleted_on=models.DateField(auto_now=True)
    update_on=models.DateField(auto_now=True)
    is_deleted=models.IntegerField(default=0)
    def __str__(self):
        return self.p_full_name


class Business(models.Model):
    b_name=models.CharField(max_length=250)
    b_owner=models.ForeignKey(Personal,on_delete=models.CASCADE)
    b_address=models.CharField(max_length=250)
    b_phone=models.CharField(max_length=250)
    b_city=models.CharField(max_length=250)
    b_pass=models.CharField(max_length=250)
    created_on=models.DateField(auto_now=True)
    deleted_on=models.DateField(auto_now=True)
    update_on=models.DateField(auto_now=True)
    is_deleted=models.IntegerField(default=0)
    def __str__(self):
        return self.b_name

class Country(models.Model):
    country_name=models.CharField(max_length=250)
    country_code=models.CharField(max_length=250)
    country_symbol=models.CharField(max_length=250)
    created_on=models.DateField(auto_now=True)
    deleted_on=models.DateField(auto_now=True)
    update_on=models.DateField(auto_now=True)
    is_deleted=models.IntegerField(default=0)
    def __str__(self):
        return self.country_name

class Province(models.Model):
    country_id=models.ForeignKey(Country,on_delete=models.CASCADE)
    province_name=models.CharField(max_length=250)
    created_on=models.DateField(auto_now=True)
    deleted_on=models.DateField(auto_now=True)
    update_on=models.DateField(auto_now=True)
    is_deleted=models.IntegerField(default=0)
    def __str__(self):
        return self.province_name

class Distric(models.Model):
    province_id=models.ForeignKey(Province,on_delete=models.CASCADE)
    distric_name=models.CharField(max_length=250)
    created_on=models.DateField(auto_now=True)
    deleted_on=models.DateField(auto_now=True)
    update_on=models.DateField(auto_now=True)
    is_deleted=models.IntegerField(default=0)
    def __str__(self):
        return self.distric_name

class Tehsil(models.Model):
    distric_id=models.ForeignKey(Distric,on_delete=models.CASCADE)
    tehsil_name=models.CharField(max_length=250)
    created_on=models.DateField(auto_now=True)
    deleted_on=models.DateField(auto_now=True)
    update_on=models.DateField(auto_now=True)
    is_deleted=models.IntegerField(default=0)
    def __str__(self):
        return self.tehsil_name

class Area(models.Model):
    tehsil_id=models.ForeignKey(Tehsil,on_delete=models.CASCADE)
    area_name=models.CharField(max_length=250)
    created_on=models.DateField(auto_now=True)
    deleted_on=models.DateField(auto_now=True)
    update_on=models.DateField(auto_now=True)
    is_deleted=models.IntegerField(default=0)
    def __str__(self):
        return self.area_name



