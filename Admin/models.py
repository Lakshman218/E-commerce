from django.db import models
from Guest.models import *

# Create your models here.
class tbl_District(models.Model):
    dis_name = models.CharField(max_length=50)

class tbl_Place(models.Model):
    plc_name = models.CharField(max_length=50,null=True)
    plc_pincode = models.IntegerField(null=True)
    district=models.ForeignKey(tbl_District,on_delete=models.SET_NULL,null=True)

class tbl_Category(models.Model):
    cat_name = models.CharField(max_length=50)

class tbl_SubCategory(models.Model):
    sub_name=models.CharField(max_length=50,null=True)
    category=models.ForeignKey(tbl_Category,on_delete=models.SET_NULL,null=True)

class tbl_complaint(models.Model):
    content=models.CharField(max_length=500)
    user=models.ForeignKey("Guest.tbl_UserReg", on_delete=models.SET_NULL,null=True)
    seller=models.ForeignKey(tbl_SellerReg, on_delete=models.SET_NULL,null=True)
    status=models.IntegerField(default=0)
    reply=models.CharField(max_length=1000,default="Not yet viewed")
    date=models.DateField(auto_now_add=True)

class tbl_feedback(models.Model):
    content=models.CharField(max_length=1000)
    user=models.ForeignKey("Guest.tbl_UserReg", on_delete=models.SET_NULL,null=True)
    seller=models.ForeignKey(tbl_SellerReg, on_delete=models.SET_NULL,null=True)

class Adminlogin(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)