from django.db import models
from Admin.models import *

# Create your models here.
class tbl_SellerReg(models.Model):
    sllrname=models.CharField(max_length=50)
    sllrcontact=models.IntegerField(max_length=50)
    sllremail=models.CharField(max_length=50)
    sllraddress=models.CharField(max_length=50)
    sllrlandmark=models.CharField(max_length=50)
    sllrpassword=models.CharField(max_length=50)
    sllrconformpswd=models.CharField(max_length=50)
    sllrproof=models.FileField(upload_to='sllrprfdocs/')
    sllrphoto=models.FileField(upload_to='sllrphtodocs')
    place=models.ForeignKey("Admin.tbl_Place",on_delete=models.SET_NULL,null=True)
    status=models.IntegerField(default=0)

class tbl_UserReg(models.Model):
    usrname=models.CharField(max_length=50)
    usrcontact=models.IntegerField(max_length=50)
    usremail=models.CharField(max_length=50)
    usrgender=models.CharField(max_length=50)
    usraddress=models.CharField(max_length=50)
    usrpassword=models.CharField(max_length=50)
    usrconformpswd=models.CharField(max_length=50)
    usrphoto=models.FileField(upload_to='userphtodocs')
    place=models.ForeignKey("Admin.tbl_Place",on_delete=models.SET_NULL,null=True)
