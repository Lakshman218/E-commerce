from django.db import models
from Admin.models import *
from Guest.models import *

# Create your models here.

class tbl_Slrproduct(models.Model):
    prdct_name=models.CharField(max_length=50)
    prdct_details=models.CharField(max_length=50)
    prdct_rate=models.IntegerField()
    prdct_image=models.FileField(upload_to='sllrprdctimg/')
    subcategory=models.ForeignKey(tbl_SubCategory,on_delete=models.SET_NULL,null=True)
    seller=models.ForeignKey(tbl_SellerReg,on_delete=models.SET_NULL,null=True)
